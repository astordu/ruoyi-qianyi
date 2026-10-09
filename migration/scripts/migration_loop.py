#!/usr/bin/env python3
"""Run one skill per fresh CLI session; coordinate through recorded migration state.

No model/API dependency: invokes the user's installed CLI. The migration state
module remains the authority for inventory, scheduling and verification hashes.
"""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
import uuid

ROOT = Path(__file__).resolve().parents[2]
STATE_SCRIPT = '.agents/skills/migration-plan/scripts/migration_state.py'
SKILLS = {
    'next': 'migration-next-group',
    'implement': 'migration-implement-group',
    'validate': 'migration-validate',
}


class LoopStop(Exception):
    def __init__(self, message, code=2):
        super().__init__(message)
        self.code = code


def utc():
    return datetime.now(timezone.utc).isoformat()


def load_state_module(root):
    spec = importlib.util.spec_from_file_location('migration_state', root / STATE_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@contextmanager
def project_lock(root):
    # A single lock for the checkout, even if --state differs. flock is released
    # by the OS after exit/crash; never unlink a lock another process may hold.
    path = root / 'migration/.migration-loop.lock'
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+') as stream:
        try:
            fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise LoopStop('已有 migration-loop 在这个项目运行。', 3)
        stream.seek(0); stream.truncate()
        json.dump({'pid': os.getpid(), 'started_at': utc()}, stream)
        stream.flush()
        try:
            yield
        finally:
            fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


def cli_command(adapter, prompt, output, model=None):
    if adapter == 'codex':
        command = ['codex', 'exec', '--dangerously-bypass-approvals-and-sandbox',
                   '--json', '--output-last-message', str(output)]
    elif adapter == 'claude':
        command = ['claude', '--dangerously-skip-permissions', '-p']
    else:
        # Current Qoder CLI uses snake_case (afk.sh's older spelling differs).
        command = ['qodercli', '--permission-mode', 'bypass_permissions', '-p']
    if model:
        command.extend(['--model', model])
    return command + [prompt]


def stop_process(process):
    if process.poll() is not None:
        return
    try:
        os.killpg(process.pid, signal.SIGTERM)
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)
        process.wait()
    except ProcessLookupError:
        pass


class MigrationLoop:
    def __init__(self, args, root=ROOT):
        self.args, self.root = args, root.resolve()
        state = Path(args.state)
        self.state = (self.root / state).resolve() if not state.is_absolute() else state.resolve()
        if not self.state.is_relative_to(self.root):
            raise LoopStop('--state 必须位于项目内。')
        if not (self.root / STATE_SCRIPT).is_file():
            raise LoopStop('缺少共享 migration_state.py。')
        self.m = load_state_module(self.root)
        self.control = self.state / 'loop'
        self.run_dir = None
        self.call_index = 0

    def checked(self):
        inventory = self.m.read(self.state / 'inventory.json')
        if Path(inventory['project_root']).resolve() != self.root:
            raise LoopStop(f'状态仍指向旧项目 {inventory["project_root"]}；当前项目为 {self.root}。')
        self.validate_layout(inventory)
        return self.m.load_checked(self.state)

    def validate_layout(self, inventory):
        if any(self.state.is_relative_to(self.root / source) for source in inventory['source_roots']):
            raise LoopStop('状态及循环日志不能写入 Vue 源目录。')
        if self.control.is_relative_to(self.root / inventory['target_root']):
            raise LoopStop('循环日志不能写入 React 目标目录。')

    def relocation(self, dry_run=False):
        """Reanchor a moved checkout only after an exact source-snapshot match.

        Hashes of group scopes, contracts, targets and evidence use relative
        paths and survive a move. Inventory digest includes the absolute root,
        so synchronize only that digest in the plan and saved round metadata.
        A journal makes interruption between atomic file writes recoverable.
        """
        journal_path = self.state / 'root-relocation.pending.json'
        if journal_path.exists():
            journal = self.m.read(journal_path)
            if journal['new_root'] != str(self.root):
                raise LoopStop('上次路径校准尚未完成，且目标位置再次变化；需核对 root-relocation.pending.json。')
        else:
            inv = self.m.read(self.state / 'inventory.json')
            if Path(inv['project_root']).resolve() == self.root:
                return None
            plan = self.m.read(self.state / 'plan.json')
            if plan['inventory_digest'] != inv['digest']:
                raise LoopStop('计划与清单快照不一致，不能只校准路径。')
            new_inv = dict(inv, project_root=str(self.root))
            config = {k:new_inv[k] for k in ('project_root','source_roots','target_root','exclude_dirs')}
            new_inv['digest'] = self.m.digest({'config':config, 'files':inv['files']})
            updates = {'inventory.json':{'old':inv, 'new':new_inv},
                       'plan.json':{'old':plan, 'new':dict(plan, inventory_digest=new_inv['digest'])}}
            for name in ('round.json', 'suspended-round.json'):
                path = self.state / name
                if path.exists():
                    task = self.m.read(path)
                    if task.get('inventory_digest') == inv['digest']:
                        updates[name] = {'old':task, 'new':dict(task, inventory_digest=new_inv['digest'])}
            journal = {'old_root':inv['project_root'], 'new_root':str(self.root), 'at':utc(),
                       'history':'root-relocation-'+uuid.uuid4().hex+'.json', 'updates':updates}
        new_inv = journal['updates']['inventory.json']['new']
        self.validate_layout(new_inv)
        try:
            live, _ = self.m.scan(new_inv)
        except ValueError as error:
            raise LoopStop(f'当前项目 {self.root} 的源码无法核对：{error}；旧清单位置：{journal["old_root"]}。') from error
        expected = new_inv['files']
        changed = sorted(p for p in set(live) | set(expected) if live.get(p) != expected.get(p))
        if changed:
            raise LoopStop('项目位置变化且源快照也有变化，停止路径校准，需重新盘点：'+', '.join(changed[:20]))
        allowed = {'inventory.json','plan.json','round.json','suspended-round.json'}
        for name, update in journal['updates'].items():
            if name not in allowed or self.m.read(self.state / name) not in (update['old'], update['new']):
                raise LoopStop('路径校准期间状态文件被其他操作修改：'+name)
        summary = {'old_root':journal['old_root'], 'new_root':journal['new_root'],
                   'source_files_matched':len(live), 'progress_preserved':True}
        if dry_run:
            return summary
        if not journal_path.exists():
            self.m.write(journal_path, journal)
        self.m.write(self.state / 'history' / journal['history'], journal)
        for name, update in journal['updates'].items():
            self.m.write(self.state / name, update['new'])
        journal_path.unlink()
        print(f'已校准项目路径：{summary["old_root"]} → {summary["new_root"]}；{len(live)} 个源文件快照一致，迁移进度保留。', flush=True)
        return summary

    def event(self, kind, **fields):
        row = {'at': utc(), 'event': kind, **fields}
        with (self.run_dir / 'events.jsonl').open('a') as stream:
            stream.write(json.dumps(row, ensure_ascii=False) + '\n')

    def agent(self, stage, detail):
        self.call_index += 1
        prefix = self.run_dir / f'{self.call_index:03}-{stage}'
        skill = SKILLS[stage]
        attempt = prefix.name
        prompt = f'''使用 ${skill}。先完整读取 .agents/skills/{skill}/SKILL.md，再按其说明执行。
项目根目录：{self.root}
本次状态目录：{self.state.relative_to(self.root)}（所有命令显式传 --state，不使用其他状态目录）。
本次调用标识：{self.run_dir.name}/{attempt}
当前阶段：{detail}
这是用户授权的外层循环调用，本次只完成上述阶段，随后退出；不要调用下一阶段、重新规划、扩大当前组范围或再选第二组。
失败修复必须先读取 plan.json 的 validation.report/note/artifacts 和 progress.md，保留历史证据。
验证报告、日志和截图用本次唯一目录，record --report 指向本次不可覆盖的报告；失败也必须 record failed/blocked。
遇到确需用户输入的阻塞，先保存诊断再结束；不要把缺失验证标为通过。
Vue 源码和后端只读；不修改循环脚本/skills/状态检查脚本；不自动 commit、push、部署或创建聊天/定时任务。
最终文字仅为说明；执行器会以真实落盘状态、报告和证据判定结果。'''
        prefix.with_suffix('.prompt.txt').write_text(prompt, encoding='utf-8')
        command = cli_command(self.args.adapter, prompt, prefix.with_suffix('.last-message.txt'), self.args.model)
        self.event('agent_start', stage=stage, detail=detail, log=str(prefix.with_suffix('.log')))
        print(f'  [{stage}] {detail}\n  日志：{prefix.with_suffix(".log")}', flush=True)
        start = time.monotonic()
        with prefix.with_suffix('.log').open('w') as log:
            process = subprocess.Popen(command, cwd=self.root, stdout=log, stderr=subprocess.STDOUT,
                                       stdin=subprocess.DEVNULL, start_new_session=True)
            try:
                returncode = process.wait(timeout=self.args.timeout)
            except subprocess.TimeoutExpired:
                stop_process(process)
                self.event('agent_timeout', stage=stage, seconds=self.args.timeout)
                raise LoopStop(f'{stage} 超时；已保留日志和现有进度。', 124)
            except BaseException:
                stop_process(process)
                raise
        self.event('agent_exit', stage=stage, exit_code=returncode,
                   seconds=round(time.monotonic()-start, 3))
        if returncode:
            raise LoopStop(f'{stage} 的 CLI 退出码为 {returncode}；停止并保留进度。', 1)

    def assert_round(self, gid):
        inv, plan, root, groups, items, *_ = self.checked()
        round_path = self.state / 'round.json'
        if not round_path.is_file():
            raise LoopStop('选组未落盘 round.json。')
        task = self.m.read(round_path)
        group = groups[gid]
        if (task.get('group') != gid or task.get('inventory_digest') != inv['digest']
                or task.get('contract_sha256') != self.m.file_hash(root / group['contract'])
                or task.get('scope_digest') != self.m.scope_digest(group, items)):
            raise LoopStop('本轮源/合同/范围与落盘任务不一致；需先核对计划。')
        return plan, group, task

    def consume_repair(self, key):
        # Bound automatic repair attempts across restarts, rather than reset
        # the budget whenever the user reruns the shell script.
        path = self.control / 'repair-counts.json'
        counts = self.m.read(path) if path.exists() else {}
        used = counts.get(key, 0)
        if used >= self.args.max_retries:
            raise LoopStop(f'{key} 已达到 {self.args.max_retries} 次自动修复上限；保留失败任务。提高 --max-retries 可续跑。', 3)
        counts[key] = used + 1
        self.m.write(path, counts)
        self.event('repair_attempt', key=key, attempt=used+1)

    def clear_repairs(self, key):
        path = self.control / 'repair-counts.json'
        if path.exists():
            counts = self.m.read(path); counts.pop(key, None)
            self.m.write(path, counts)

    def verification(self, row, previous):
        validation = row.get('validation')
        if (row['status'] not in ('passed', 'failed', 'blocked') or not validation
                or validation == previous or validation.get('result') != row['status']
                or not self.m.evidence_valid(self.root, validation)):
            raise LoopStop('验证没有生成新的有效记账记录；CLI 成功不能代表验证通过。')

    def group_round(self, gid):
        while True:
            plan, group, task = self.assert_round(gid)
            if plan['active_group'] != gid:
                raise LoopStop('active_group 与本轮任务不一致。')
            revalidate = task.get('mode') == 'revalidate' and group['status'] == 'passed'
            if group['status'] != 'implemented' and not revalidate:
                if group['status'] == 'failed':
                    if not self.m.evidence_valid(self.root, group.get('validation')):
                        raise LoopStop('上次失败报告/证据缺失或已改变，无法可靠修复。')
                    self.consume_repair('group:'+gid)
                self.agent('implement', f'只实施或修复当前组 {gid}；读取其最新失败报告，完成后记录 implemented。')
                plan, group, _ = self.assert_round(gid)
                if plan['active_group'] != gid or group['status'] != 'implemented':
                    raise LoopStop('implementation 未将当前组落盘为 implemented。')
            previous = group.get('validation')
            self.agent('validate', f'本组模式：仅验证组 {gid}，执行实际检查并 record passed/failed/blocked。')
            plan, group, _ = self.assert_round(gid)
            self.verification(group, previous)
            result = self.m.check_state(self.state)
            self.event('group_result', group=gid, result=group['status'])
            if group['status'] == 'passed':
                if gid in result['invalidated_groups'] or plan['active_group'] == gid:
                    raise LoopStop('通过记录无效，或通过后 active_group 未释放。')
                self.clear_repairs('group:'+gid)
                return
            if group['status'] == 'blocked':
                if plan['active_group'] == gid:
                    raise LoopStop('阻塞后 active_group 未释放。')
                return
            if plan['active_group'] != gid:
                raise LoopStop('验证失败后没有保留当前组。')
            # Stay on this group. No next-group invocation on the repair path.

    def integration_round(self, remaining):
        *_, checks, order = self.checked()
        available = [cid for cid in remaining if checks[cid]['status'] != 'blocked']
        if not available:
            raise LoopStop('所有剩余集成检查均阻塞，见 plan.json 和验证报告。', 3)
        cid = sorted(available)[0]
        check = checks[cid]
        if check['status'] == 'failed':
            self.consume_repair('integration:'+cid)
        previous = check.get('validation')
        self.agent('validate', f'集成模式：本次只执行 {cid}，合同 {check["contract"]}。使用 record --integration {cid} 记账；不要执行 implementation 或修改业务代码。发现代码缺陷时保存报告并标 blocked，供重新规划修复任务。')
        *_, checks, order = self.checked()
        check = checks[cid]
        self.verification(check, previous)
        self.event('integration_result', integration=cid, result=check['status'])
        if check['status'] == 'passed':
            inv, plan, root, groups, items, checks, order = self.checked()
            passed, _ = self.m.effective_groups(root, inv, groups, items, order)
            if cid not in self.m.effective_checks(root, groups, checks, passed):
                raise LoopStop('集成记录无效。')
            self.clear_repairs('integration:'+cid)

    def finalize(self):
        inv, plan, *_ = self.checked()
        self.m.check_state(self.state, final=True)
        report = self.state / 'final-report.md'
        receipt = self.control / 'finalized.json'
        stamp = self.m.digest({'inventory':inv['digest'],
                              'groups':[g.get('validation') for g in plan['groups']],
                              'integration':[c.get('validation') for c in plan['integration_checks']]})
        old = self.m.read(receipt) if receipt.exists() else {}
        valid = (report.is_file() and report.stat().st_size and old.get('snapshot') == stamp
                 and old.get('report_sha256') == self.m.file_hash(report))
        if not valid:
            before_report = (report.stat().st_mtime_ns, self.m.file_hash(report)) if report.is_file() else None
            self.agent('validate', '收尾模式：全部组与集成已有效通过。执行 check --final 并写本状态目录的 final-report.md，记录真实覆盖/检查/限制，不重新选组或实施代码。')
            self.m.check_state(self.state, final=True)
            if not report.is_file() or not report.stat().st_size:
                raise LoopStop('缺少最终报告。')
            if before_report == (report.stat().st_mtime_ns, self.m.file_hash(report)):
                raise LoopStop('收尾 CLI 没有更新最终报告。')
            # A finalizer must not silently change the verified scope.
            _, after, *_ = self.checked()
            current = self.m.digest({'inventory':inv['digest'],
                                    'groups':[g.get('validation') for g in after['groups']],
                                    'integration':[c.get('validation') for c in after['integration_checks']]})
            if current != stamp:
                raise LoopStop('收尾期间验证范围发生变化，请重新核对。')
            self.m.write(receipt, {'snapshot':stamp, 'report_sha256':self.m.file_hash(report), 'at':utc()})
        return {'status':'complete', 'report':str(report)}

    def run(self):
        if self.args.dry_run:
            relocated = self.relocation(dry_run=True)
            if relocated:
                print(json.dumps({'dry_run':True, 'status':'root_relocation_required',
                                  'relocation':relocated, 'note':'正式运行会校准路径；本次未写状态或调用 agent。'},
                                 ensure_ascii=False, indent=2))
                return 0
            self.checked()
            selection = self.m.select(self.state, False)
            print(json.dumps({'dry_run': True, 'next': selection,
                              'check':self.m.check_state(self.state)}, ensure_ascii=False, indent=2))
            return 0
        with project_lock(self.root):
            self.relocation()
            self.checked()
            for skill in SKILLS.values():
                if not (self.root / '.agents/skills' / skill / 'SKILL.md').is_file():
                    raise LoopStop('缺少 skill：'+skill)
            if not shutil.which(self.args.adapter):
                raise LoopStop('未安装 CLI：'+self.args.adapter)
            self.run_dir = self.control / 'runs' / (datetime.now().strftime('%Y%m%d-%H%M%S')+'-'+uuid.uuid4().hex[:8])
            self.run_dir.mkdir(parents=True)
            print('循环日志：'+str(self.run_dir), flush=True)
            self.event('run_start', adapter=self.args.adapter, max_iterations=self.args.max_iterations,
                       max_retries=self.args.max_retries, timeout=self.args.timeout)
            try:
                for iteration in range(1, self.args.max_iterations+1):
                    selection = self.m.select(self.state, False)
                    self.event('iteration', iteration=iteration, selection=selection)
                    print(f'轮次 {iteration}/{self.args.max_iterations}：{selection["status"]}', flush=True)
                    status = selection['status']
                    if status == 'complete':
                        result = self.finalize(); break
                    if status == 'blocked':
                        raise LoopStop('没有可执行组，阻塞详情已保存到本轮日志。', 3)
                    if status == 'groups_complete':
                        self.integration_round(selection['remaining_integration'])
                    elif status == 'selected':
                        gid = selection['group']
                        plan = self.m.read(self.state / 'plan.json')
                        # Reuse an active task on resume/repair; invoke the next
                        # skill only for a new selection or stale verification.
                        if plan['active_group'] != gid or selection['mode'] == 'revalidate':
                            self.agent('next', f'仅选组并落盘；当前调度候选 {gid}，调用 next --claim。选组后结束。')
                        plan, _, _ = self.assert_round(gid)
                        if plan['active_group'] != gid:
                            raise LoopStop('选组 CLI 未写入预期 active_group。')
                        self.group_round(gid)
                    else:
                        raise LoopStop('未知调度状态：'+status)
                else:
                    remaining = self.m.select(self.state, False)
                    result = self.finalize() if remaining['status'] == 'complete' else {
                        'status':'iteration_limit', 'next':remaining, 'max_iterations':self.args.max_iterations}
                self.m.write(self.run_dir / 'result.json', result)
                print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)
                return 0 if result['status'] == 'complete' else 4
            except BaseException as error:
                self.m.write(self.run_dir / 'result.json', {
                    'status':'interrupted' if isinstance(error, KeyboardInterrupt) else 'needs_attention',
                    'error':str(error), 'at':utc()})
                raise


def positive(value):
    number = int(value)
    if number <= 0: raise argparse.ArgumentTypeError('必须是正整数')
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(description='按落盘状态循环选组/实施/验证；验证失败在同一组修复。')
    parser.add_argument('adapter', nargs='?', choices=['codex','claude','qodercli'], default='codex')
    parser.add_argument('max_iterations', nargs='?', type=positive, default=10,
                        help='最多组/集成轮次，默认10；同组修复计入 --max-retries')
    parser.add_argument('--state', default='migration/state')
    parser.add_argument('--max-retries', type=positive, default=3, help='同组自动修复上限，跨重启保存，默认3')
    parser.add_argument('--timeout', type=positive, default=1800, help='每个 agent 调用秒数上限，默认1800')
    parser.add_argument('--model', help='可选模型；省略时沿用 CLI 配置')
    parser.add_argument('--dry-run', action='store_true', help='只读检查与显示候选，不调用 agent 或写状态')
    args = parser.parse_args(argv)
    def interrupted(signum, frame):
        raise KeyboardInterrupt()
    signal.signal(signal.SIGTERM, interrupted)
    try:
        return MigrationLoop(args).run()
    except KeyboardInterrupt:
        print('已中断；日志和迁移进度保留。', file=sys.stderr)
        return 130
    except (LoopStop, ValueError, KeyError, TypeError, OSError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        return error.code if isinstance(error, LoopStop) else 2


if __name__ == '__main__':
    sys.exit(main())
