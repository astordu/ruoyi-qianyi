"""Temporary fixtures + fake CLI only. Never starts a real agent or migration."""
import argparse
from contextlib import redirect_stdout
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('migration_loop', Path(__file__).with_name('migration_loop.py'))
loop = importlib.util.module_from_spec(spec)
spec.loader.exec_module(loop)

FAKE = '''#!/usr/bin/env python3
import argparse,importlib.util,json,os,re,sys,time
from pathlib import Path
root=Path.cwd(); state=root/'migration/state'; prompt=sys.argv[-1]
spec=importlib.util.spec_from_file_location('migration_state',root/'.agents/skills/migration-plan/scripts/migration_state.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
stage='next' if '$migration-next-group' in prompt else 'implement' if '$migration-implement-group' in prompt else 'validate'
with (root/'calls.jsonl').open('a') as f:f.write(json.dumps({'stage':stage,'prompt':prompt,'argv':sys.argv[1:]})+'\\n')
behavior=os.environ.get('FAKE_BEHAVIOR','pass')
if behavior=='exit':sys.exit(7)
if behavior=='timeout':time.sleep(10)
if behavior=='noop':sys.exit(0)
if behavior=='validate-noop' and stage=='validate':sys.exit(0)
if stage=='next':m.select(state,True)
elif stage=='implement':
 p=m.read(state/'plan.json');gid=p['active_group'];g=next(g for g in p['groups'] if g['id']==gid)
 if behavior=='wrong-group':p['active_group']='G2'
 else:
  for i in p['items']:
   if i.get('group')==gid:
    for target in i['targets']:
     path=root/target;path.parent.mkdir(parents=True,exist_ok=True);path.write_text('translated '+gid)
  g['status']='implemented'
 m.write(state/'plan.json',p)
elif '收尾模式' in prompt:
 (state/'final-report.md').write_text('All fixtures verified; fake CLI, no real business proof.')
else:
 p=m.read(state/'plan.json');integration='集成模式' in prompt
 key=re.search(r'本次只执行 (J\\d+)',prompt).group(1) if integration else p['active_group']
 call_count=sum(1 for line in (root/'calls.jsonl').read_text().splitlines() if json.loads(line)['stage']=='validate')
 result='failed' if behavior=='always-fail' or behavior=='fail-once' and call_count==1 else 'blocked' if behavior=='blocked' else 'passed'
 attempt='migration/state/evidence/'+key+'/'+str(time.time_ns());report=root/(attempt+'/report.md');report.parent.mkdir(parents=True);report.write_text('expected/source/actual/reproduction/result '+result)
 evidence=root/(attempt+'/test.txt');evidence.write_text('fixture check '+result)
 m.record(argparse.Namespace(group=None if integration else key,integration=key if integration else None,result=result,report=str(report.relative_to(root)),evidence=[str(evidence.relative_to(root))],note='failure: retry fixture' if result!='passed' else ''),state)
'''


class MigrationLoopTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='migration loop ')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        state_script = self.root / loop.STATE_SCRIPT
        state_script.parent.mkdir(parents=True)
        shutil.copyfile(loop.ROOT / loop.STATE_SCRIPT, state_script)
        for skill in loop.SKILLS.values():
            p=self.root / '.agents/skills' / skill / 'SKILL.md';p.parent.mkdir(parents=True,exist_ok=True);p.write_text('fixture skill')
        self.m = loop.load_state_module(self.root)
        self.state = self.root / 'migration/state'
        for n in (1,2):self.put(f'vue/{n}.js',f'original {n}')
        self.m.inventory(argparse.Namespace(root=str(self.root),source=['vue'],target='react',exclude_dirs='node_modules'),self.state)
        plan = self.m.read(self.state/'plan.json')
        for review in plan['files'].values():review.update(reviewed=True,review_evidence='full fixture review')
        plan['groups']=[];plan['items']=[]
        for n in (1,2):
            contract=f'migration/state/groups/G{n}/contract.md';self.put(contract,'old fixture behavior and assertions')
            plan['groups'].append(dict(id=f'G{n}',title=f'fixture {n}',feature='shared',entry_priority=0 if n==1 else 2,depends_on=[] if n==1 else ['G1'],contract=contract,status='pending',targets=[]))
            plan['items'].append(dict(id=f'I{n}',source=f'vue/{n}.js',locator='complete fixture',basis='original fixture',disposition='migrate',group=f'G{n}',targets=[f'react/{n}.ts'],target_locator='translated fixture'))
        self.put('migration/state/integration/J1-contract.md','fixture wiring assertions')
        plan['integration_checks']=[dict(id='J1',groups=['G1','G2'],contract='migration/state/integration/J1-contract.md',status='pending')]
        self.m.write(self.state/'plan.json',plan)
        binpath=self.root/'bin';binpath.mkdir()
        for cli in ('codex','claude','qodercli'):
            path=binpath/cli;path.write_text(FAKE);path.chmod(0o755)
        self.env = patch.dict(os.environ, {'PATH':str(binpath)+os.pathsep+os.environ['PATH'],'FAKE_BEHAVIOR':'pass'})
        self.env.start();self.addCleanup(self.env.stop)
        self.args=argparse.Namespace(adapter='codex',max_iterations=10,state='migration/state',max_retries=2,timeout=10,model=None,dry_run=False)

    def put(self,path,text):
        p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text);return p

    def calls(self):
        path=self.root/'calls.jsonl'
        return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []

    def run_loop(self):
        with redirect_stdout(io.StringIO()):
            return loop.MigrationLoop(self.args,self.root).run()

    def fail_current(self):
        self.m.select(self.state,True)
        self.put('migration/state/failure-report.md','I1 expected old, actual broken, reproduce fixture')
        self.put('migration/state/failure.txt','fixture assertion failed')
        self.m.record(argparse.Namespace(group='G1',integration=None,result='failed',report='migration/state/failure-report.md',evidence=['migration/state/failure.txt'],note='fix fixture I1'),self.state)

    def mark_as_moved(self):
        inv=self.m.read(self.state/'inventory.json');plan=self.m.read(self.state/'plan.json')
        inv['project_root']=str(self.root/'missing-old-checkout')
        config={k:inv[k] for k in ('project_root','source_roots','target_root','exclude_dirs')}
        inv['digest']=self.m.digest({'config':config,'files':inv['files']})
        plan['inventory_digest']=inv['digest']
        self.m.write(self.state/'inventory.json',inv);self.m.write(self.state/'plan.json',plan)
        task=self.state/'round.json'
        if task.exists():
            data=self.m.read(task);data['inventory_digest']=inv['digest'];self.m.write(task,data)
        return inv['digest']

    def test_normal_groups_integration_final_and_second_run_no_calls(self):
        self.assertEqual(self.run_loop(),0)
        self.assertEqual([c['stage'] for c in self.calls()],['next','implement','validate','next','implement','validate','validate','validate'])
        self.assertEqual(self.m.check_state(self.state)['status'],'complete')
        count=len(self.calls());self.assertEqual(self.run_loop(),0);self.assertEqual(len(self.calls()),count)

    def test_failure_repairs_same_group_without_reselecting(self):
        os.environ['FAKE_BEHAVIOR']='fail-once';self.args.max_iterations=1
        self.assertEqual(self.run_loop(),4)
        self.assertEqual([c['stage'] for c in self.calls()],['next','implement','validate','implement','validate'])
        self.assertEqual(self.m.read(self.state/'plan.json')['groups'][0]['status'],'passed')
        self.assertEqual(len(list((self.state/'evidence/G1').glob('*/report.md'))),2)

    def test_failed_task_resumes_directly_from_saved_report(self):
        self.fail_current();self.args.max_iterations=1
        self.assertEqual(self.run_loop(),4)
        self.assertEqual([c['stage'] for c in self.calls()],['implement','validate'])
        self.assertIn('validation.report/note/artifacts',self.calls()[0]['prompt'])
        self.assertTrue((self.state/'failure-report.md').exists())

    def test_implemented_resume_only_validates(self):
        self.m.select(self.state,True);p=self.m.read(self.state/'plan.json');p['groups'][0]['status']='implemented';self.m.write(self.state/'plan.json',p);self.put('react/1.ts','translated G1')
        self.args.max_iterations=1;self.assertEqual(self.run_loop(),4)
        self.assertEqual([c['stage'] for c in self.calls()],['validate'])

    def test_retry_limit_persists_across_restarts(self):
        os.environ['FAKE_BEHAVIOR']='always-fail'
        with self.assertRaisesRegex(loop.LoopStop,'修复上限'):self.run_loop()
        self.assertEqual([c['stage'] for c in self.calls()].count('implement'),3)
        count=len(self.calls())
        with self.assertRaisesRegex(loop.LoopStop,'修复上限'):self.run_loop()
        self.assertEqual(len(self.calls()),count)
        self.assertEqual(self.m.read(self.state/'plan.json')['active_group'],'G1')

    def test_zero_exit_without_state_is_not_success(self):
        os.environ['FAKE_BEHAVIOR']='noop'
        with self.assertRaisesRegex(loop.LoopStop,'round.json'):self.run_loop()
        self.assertTrue(list((self.state/'loop/runs').glob('*/result.json')))

    def test_validate_zero_exit_without_new_record_is_rejected(self):
        os.environ['FAKE_BEHAVIOR']='validate-noop'
        with self.assertRaisesRegex(loop.LoopStop,'没有生成新的有效记账'):self.run_loop()
        self.assertEqual(self.m.read(self.state/'plan.json')['groups'][0]['status'],'implemented')

    def test_missing_failure_evidence_stops_before_repair(self):
        self.fail_current();(self.state/'failure.txt').unlink()
        with self.assertRaisesRegex(loop.LoopStop,'失败报告/证据缺失'):self.run_loop()
        self.assertEqual(self.calls(),[])

    def test_cli_error_and_timeout_leave_logs(self):
        os.environ['FAKE_BEHAVIOR']='exit'
        with self.assertRaisesRegex(loop.LoopStop,'退出码'):self.run_loop()
        os.environ['FAKE_BEHAVIOR']='timeout';self.args.timeout=0.1
        with self.assertRaisesRegex(loop.LoopStop,'超时'):self.run_loop()
        self.assertEqual(len(list((self.state/'loop/runs').glob('*/001-next.log'))),2)

    def test_dry_run_is_read_only(self):
        before={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.args.dry_run=True;self.assertEqual(self.run_loop(),0)
        after={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before,after);self.assertEqual(self.calls(),[])

    def test_changed_source_stops_before_agent(self):
        self.put('vue/1.js','source changed')
        with self.assertRaisesRegex(ValueError,'snapshot changed'):self.run_loop()
        self.assertEqual(self.calls(),[])

    def test_project_lock_rejects_second_runner(self):
        with loop.project_lock(self.root):
            with self.assertRaisesRegex(loop.LoopStop,'已有 migration-loop'):self.run_loop()
        # The same lock file is reusable after release.
        self.args.max_iterations=1;self.assertEqual(self.run_loop(),4)

    def test_wrong_group_after_implementation_stops(self):
        os.environ['FAKE_BEHAVIOR']='wrong-group'
        with self.assertRaisesRegex(loop.LoopStop,'未将当前组'):self.run_loop()
        self.assertEqual([c['stage'] for c in self.calls()],['next','implement'])

    def test_all_blocked_stops_and_does_not_run_implementation_again(self):
        os.environ['FAKE_BEHAVIOR']='blocked'
        with self.assertRaisesRegex(loop.LoopStop,'没有可执行组'):self.run_loop()
        self.assertEqual([c['stage'] for c in self.calls()],['next','implement','validate'])
        self.assertIsNone(self.m.read(self.state/'plan.json')['active_group'])

    def test_stale_passed_group_revalidates_without_implementation(self):
        self.args.max_iterations=1;self.run_loop();count=len(self.calls())
        self.put('react/1.ts','changed translated G1')
        self.assertEqual(self.run_loop(),4)
        self.assertEqual([c['stage'] for c in self.calls()[count:]],['next','validate'])

    def test_each_adapter_works_and_model_is_not_silently_selected(self):
        for adapter in ('claude','qodercli'):
            self.args.adapter=adapter;self.args.max_iterations=1
            self.assertEqual(self.run_loop(),4)
            self.assertNotIn('--model',self.calls()[-1]['argv'])
        command=loop.cli_command('codex','prompt',Path('answer'),model='user-choice')
        self.assertEqual(command[command.index('--model')+1],'user-choice')

    def test_shell_entrypoint_help_and_invalid_limit(self):
        entry=loop.ROOT/'migration-loop.sh'
        help_result=subprocess.run(['bash',str(entry),'--help'],capture_output=True,text=True)
        self.assertEqual(help_result.returncode,0);self.assertIn('--dry-run',help_result.stdout)
        invalid=subprocess.run(['bash',str(entry),'codex','0'],capture_output=True,text=True)
        self.assertEqual(invalid.returncode,2)

    def test_shell_uses_its_own_project_from_another_cwd_with_spaces(self):
        entry=self.root/'migration-loop.sh';shutil.copyfile(loop.ROOT/'migration-loop.sh',entry)
        helper=self.root/'migration/scripts/migration_loop.py';helper.parent.mkdir(parents=True)
        shutil.copyfile(Path(loop.__file__),helper)
        result=subprocess.run(['bash',str(entry),'codex','1'],cwd=self.root.parent,capture_output=True,text=True,timeout=10)
        self.assertEqual(result.returncode,4,result.stderr)
        self.assertEqual([c['stage'] for c in self.calls()],['next','implement','validate'])

    def test_moved_project_auto_reanchors_and_preserves_passed_verification(self):
        self.args.max_iterations=1;self.run_loop()
        old_validation=self.m.read(self.state/'plan.json')['groups'][0]['validation']
        old_digest=self.mark_as_moved();controller=loop.MigrationLoop(self.args,self.root)
        with loop.project_lock(self.root),redirect_stdout(io.StringIO()):controller.prepare_state()
        plan=self.m.read(self.state/'plan.json');inv=self.m.read(self.state/'inventory.json')
        self.assertEqual(inv['project_root'],'../..');self.assertNotEqual(inv['digest'],old_digest)
        self.assertEqual(plan['inventory_digest'],inv['digest'])
        self.assertEqual(plan['groups'][0]['validation'],old_validation)
        self.assertEqual(self.m.check_state(self.state)['groups_passed'],1)
        self.assertTrue(list((self.state/'history').glob('portability-*.json')))

    def test_moved_failed_task_resumes_same_group_and_updates_round_digest(self):
        self.fail_current();self.mark_as_moved();self.args.max_iterations=1
        self.assertEqual(self.run_loop(),4)
        self.assertEqual([c['stage'] for c in self.calls()],['implement','validate'])
        self.assertEqual(self.m.read(self.state/'round.json')['inventory_digest'],self.m.read(self.state/'inventory.json')['digest'])
        self.assertTrue((self.state/'failure-report.md').is_file())

    def test_moved_project_dry_run_does_not_rewrite_state(self):
        self.mark_as_moved();self.args.dry_run=True
        before={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(self.run_loop(),0)
        after={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before,after);self.assertEqual(self.calls(),[])

    def test_moved_changed_source_is_not_accepted_as_a_relocation(self):
        self.mark_as_moved();self.put('vue/1.js','changed source')
        before=(self.state/'inventory.json').read_bytes()
        with self.assertRaisesRegex(ValueError,'源快照变化'):self.run_loop()
        self.assertEqual((self.state/'inventory.json').read_bytes(),before)
        self.assertEqual(self.calls(),[])

    def test_interrupted_relocation_finishes_on_restart(self):
        self.fail_current();self.mark_as_moved()
        controller=loop.MigrationLoop(self.args,self.root);original_write=controller.m.write
        def interrupt(path,data):
            if path==self.state/'plan.json':raise OSError('simulated interruption after inventory update')
            original_write(path,data)
        with patch.object(controller.m,'write',side_effect=interrupt),redirect_stdout(io.StringIO()):
            with self.assertRaisesRegex(OSError,'simulated interruption'):controller.prepare_state()
        self.assertTrue((self.state/'root-relocation.pending.json').exists())
        self.args.max_iterations=1;self.assertEqual(self.run_loop(),4)
        self.assertFalse((self.state/'root-relocation.pending.json').exists())
        self.assertEqual([c['stage'] for c in self.calls()],['implement','validate'])

    def test_legacy_absolute_relocation_journal_recovers_to_relative_root(self):
        self.fail_current();self.mark_as_moved()
        inv=self.m.read(self.state/'inventory.json');plan=self.m.read(self.state/'plan.json');task=self.m.read(self.state/'round.json')
        new_inv=dict(inv,project_root=str(self.root));new_inv['digest']=self.m.inventory_digest(new_inv)
        updates={'inventory.json':{'old':inv,'new':new_inv},'plan.json':{'old':plan,'new':dict(plan,inventory_digest=new_inv['digest'])},
                 'round.json':{'old':task,'new':dict(task,inventory_digest=new_inv['digest'])}}
        self.m.write(self.state/'root-relocation.pending.json',{'new_root':str(self.root),'updates':updates})
        self.m.write(self.state/'inventory.json',new_inv)
        self.args.max_iterations=1;self.assertEqual(self.run_loop(),4)
        self.assertEqual(self.m.read(self.state/'inventory.json')['project_root'],'../..')
        self.assertFalse((self.state/'root-relocation.pending.json').exists())
        self.assertEqual([c['stage'] for c in self.calls()],['implement','validate'])

    def add_excluded_lock(self):
        package={'name':'fixture','dependencies':{'vue':'^3.0.0'}}
        self.put('vue/package.json',json.dumps(package))
        self.put('vue/package-lock.json',json.dumps({'lockfileVersion':3,'packages':{'':package}}))
        self.m.inventory(argparse.Namespace(root=str(self.root),source=['vue'],target='react',exclude_dirs='node_modules'),self.state)
        inv=self.m.read(self.state/'inventory.json');plan=self.m.read(self.state/'plan.json')
        for index,name in enumerate(('package.json','package-lock.json'),3):
            path='vue/'+name
            plan['files'][path]={'sha256':inv['files'][path]['sha256'],'reviewed':True,'review_evidence':'full-file: replaced Vue dependency graph'}
            plan['items'].append(dict(id='I'+str(index),source=path,locator='whole file',basis='Vue dependency configuration',disposition='exclude',group=None,targets=[],reason='React dependency graph is regenerated'))
        plan['inventory_digest']=inv['digest'];self.m.write(self.state/'plan.json',plan)

    def change_lock(self):
        lock=self.m.read(self.root/'vue/package-lock.json')
        lock['packages']['node_modules/vue']={'version':'3.5.0'}
        self.put('vue/package-lock.json',json.dumps(lock))

    def test_excluded_lock_refresh_revalidates_previous_passes(self):
        self.add_excluded_lock();self.args.max_iterations=1;self.run_loop();count=len(self.calls())
        old_validation=self.m.read(self.state/'plan.json')['groups'][0]['validation']
        self.change_lock();controller=loop.MigrationLoop(self.args,self.root)
        summary=controller.prepare_state()
        self.assertEqual(summary['refreshed_excluded_locks'],['vue/package-lock.json'])
        self.assertTrue(summary['runtime_revalidation_required'])
        self.assertEqual(self.m.read(self.state/'plan.json')['groups'][0]['validation'],old_validation)
        self.assertEqual(self.m.check_state(self.state)['invalidated_groups'],['G1'])
        self.assertIn('vue/package-lock.json',self.m.read(self.state/'inventory.json')['files'])
        self.assertEqual(self.run_loop(),4)
        self.assertEqual([c['stage'] for c in self.calls()[count:]],['next','validate'])
        self.assertEqual(self.m.check_state(self.state)['groups_passed'],1)

    def test_legacy_root_and_excluded_lock_refresh_together(self):
        self.add_excluded_lock();self.fail_current();self.mark_as_moved();self.change_lock()
        self.args.max_iterations=1;self.assertEqual(self.run_loop(),4)
        self.assertEqual([c['stage'] for c in self.calls()],['implement','validate'])
        self.assertEqual(self.m.read(self.state/'inventory.json')['project_root'],'../..')
        self.assertTrue((self.state/'failure-report.md').exists())

    def test_lock_refresh_dry_run_is_read_only(self):
        self.add_excluded_lock();self.mark_as_moved();self.change_lock();self.args.dry_run=True
        before={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(self.run_loop(),0)
        after={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before,after);self.assertEqual(self.calls(),[])

    def test_migrated_lock_or_changed_manifest_is_not_auto_refreshed(self):
        self.add_excluded_lock();self.change_lock()
        plan=self.m.read(self.state/'plan.json');plan['items'][-1].update(disposition='migrate',group='G1')
        self.m.write(self.state/'plan.json',plan)
        with self.assertRaisesRegex(ValueError,'源快照变化'):self.run_loop()
        plan['items'][-1].update(disposition='exclude',group=None);self.m.write(self.state/'plan.json',plan)
        self.put('vue/package.json','{"dependencies":{"vue":"^4.0.0"}}')
        with self.assertRaisesRegex(ValueError,'源快照变化'):self.run_loop()
        self.assertEqual(self.calls(),[])

    def test_invalid_or_deleted_lock_is_not_auto_refreshed(self):
        self.add_excluded_lock();self.put('vue/package-lock.json','{invalid')
        with self.assertRaises(ValueError):self.run_loop()
        (self.root/'vue/package-lock.json').unlink()
        with self.assertRaisesRegex(ValueError,'源快照变化'):self.run_loop()
        self.assertEqual(self.calls(),[])

    def test_copied_project_runs_without_old_machine_and_keeps_passed_records(self):
        self.args.max_iterations=1;self.run_loop()
        copied=tempfile.TemporaryDirectory(prefix='second machine ');self.addCleanup(copied.cleanup)
        new_root=Path(copied.name).resolve()/'checkout';shutil.copytree(self.root,new_root)
        inv_before=(new_root/'migration/state/inventory.json').read_bytes()
        shutil.rmtree(self.root)
        os.environ['PATH']=str(new_root/'bin')+os.pathsep+os.environ['PATH']
        controller=loop.MigrationLoop(self.args,new_root)
        with redirect_stdout(io.StringIO()):self.assertEqual(controller.run(),4)
        new_state=new_root/'migration/state'
        self.assertEqual((new_state/'inventory.json').read_bytes(),inv_before)
        self.assertEqual(controller.m.check_state(new_state)['groups_passed'],2)
        self.assertEqual(controller.m.read(new_state/'inventory.json')['project_root'],'../..')
        prompts=list((new_state/'loop/runs').glob('*/*.prompt.txt'))
        for prompt in prompts:self.assertNotIn(str(new_root),prompt.read_text())
        for events in (new_state/'loop/runs').glob('*/events.jsonl'):
            self.assertNotIn(str(new_root),events.read_text())



if __name__=='__main__':unittest.main()
