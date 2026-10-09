"""Build initial coverage/contract plan from the full-file structural audit.

Refuses to replace an existing populated plan. This is structural coverage,
not proof of semantic equivalence; each round rereads and tests its source.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
STATE = ROOT / 'migration/state'
SOURCE = 'ruoyi-fastapi-frontend/'
TARGET = 'react-front/'
inv = json.loads((STATE / 'inventory.json').read_text())
audit = json.loads((STATE / 'source-audit.json').read_text())
old = json.loads((STATE / 'plan.json').read_text())
if old['groups']:
    raise SystemExit('Existing plan: reconcile explicitly; do not overwrite progress')
groups = {}
items = []
owners = {}
file_groups = {}
edges = []
unresolved = []

def group(gid, title, feature='shared', priority=2):
    groups[gid] = dict(id=gid, title=title, feature=feature, entry_priority=priority,
                       depends_on=[] if gid == 'G000' else ['G000'],
                       contract=f'migration/state/groups/{gid}/contract.md',
                       targets=[], status='pending')
    return gid

group('G000', 'React 工程启动、HTML 加载入口与多环境构建', priority=0)

def add(file, gid, locator, basis, **extra):
    row = dict(id=f'I{len(items)+1:05}', source=file, locator=locator,
               basis=basis, disposition='migrate', group=gid, targets=[], **extra)
    items.append(row)
    return row

def feature(file):
    short = file.removeprefix(SOURCE)
    if short.startswith('src/views/'):
        return '/'.join(short.split('/')[2:4])
    if short.startswith('plugins/'):
        return '/'.join(short.split('/')[:2])
    return 'shared'

def standard_target(file):
    short = file.removeprefix(SOURCE)
    if short.endswith('.vue'):
        short = short[:-4] + '.tsx'
    if short.endswith('.js'):
        short = short[:-3] + '.ts'
    return TARGET + short

foundation_whole = {'.gitignore', 'index.html', 'public/favicon.ico', 'public/html/ie.html'}
for index, (file, r) in enumerate(audit.items(), 1):
    short = file.removeprefix(SOURCE)
    base = f'G{index:03}'
    js = r.get('scripts', []) + ([r['javascript']] if 'javascript' in r else [])
    statements = [s for j in js for s in j['statements']]
    fgroups = []
    if short in foundation_whole:
        add(file, 'G000', '完整文件（HTML 标题/meta/加载动画、IE 降级、favicon 或工程忽略规则）',
            '完整读取并保留原内容；挂载点 app→root，入口 main.js→main.tsx；忽略规则增加 React 测试产物。')
        file_groups[file] = ['G000']
        continue
    if short == 'package-lock.json':
        add(file, None, '完整锁文件', '原 Vue 依赖图；目标必须根据 React package.json 重新生成锁文件。',
            reason='不可沿用 Vue/Pinia 依赖图；npm install 生成目标完整性哈希，保留源锁文件作为原依赖证据。')['disposition'] = 'exclude'
        file_groups[file] = []
        continue
    if short == 'package.json':
        group(base, '业务依赖、插件和既有测试命令接入')
        for key, value in r['package'].items():
            if key in ('dependencies', 'devDependencies', 'overrides', 'scripts'):
                for name in value:
                    gid = 'G000' if key == 'scripts' and name in ('dev', 'preview', 'build:prod', 'build:stage', 'build:docker') else base
                    if key == 'devDependencies' and name in ('vite', '@vitejs/plugin-vue'):
                        gid = 'G000'
                    if key == 'dependencies' and name == 'vue':
                        gid = 'G000'
                    add(file, gid, f'JSON {key}.{name}',
                        f'保留 {name} 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。')
            else:
                add(file, 'G000', f'JSON {key}', '保留项目描述、版本、作者、许可证和上游来源；目标命名 vfadmin-react，ESM 模式。')
        file_groups[file] = ['G000', base]
        continue
    if short.startswith('.env.'):
        group(base, f'{short} 压缩构建参数接入')
        for key in r['environment_keys']:
            gid = base if key == 'VITE_BUILD_COMPRESS' else 'G000'
            add(file, gid, f'env key {key}', '环境名、标题与 API 前缀维持原值；不在报告输出变量值。压缩参数由压缩组接入。')
        file_groups[file] = ['G000', base] if any(i['group'] == base and i['source'] == file for i in items) else ['G000']
        if file_groups[file] == ['G000']:
            groups.pop(base)
        continue
    if short == 'vite.config.js':
        group(base, 'SVG/Monaco/压缩构建插件总装')
        add(file, 'G000', 'defineConfig: base/resolve/build/server/css（plugins 单独登记）',
            'base=/；~ 根别名、@ src 别名；dist/static 名称；12580 host/open；dev-api→19099 去前缀；移除 @charset。')
        add(file, base, 'imports createVitePlugins + defineConfig.plugins',
            '保留 symbol SVG、Monaco 五种 worker、按环境 gzip/brotli；Vue 编译/自动导入改为显式 React imports。')
        file_groups[file] = ['G000', base]
        continue
    large = r.get('lines', 0) > 500 and bool(js)
    group(base, f'{short}：' + ('状态、输入与依赖接口' if large else '完整能力'), feature(file),
          1 if short in ('src/router/index.js', 'src/permission.js', 'src/views/login.vue', 'src/views/lock.vue') else 2)
    fgroups.append(base)
    for number, s in enumerate(statements):
        top_function = s['names'] and (s['kind'] == 'FunctionDeclaration' or
                        s['functions'] and s['functions'][0]['line'] == s['line'])
        gid = base
        if large and top_function:
            gid = group(f'{base}F{number:03}', f'{short}：{", ".join(s["names"])}', feature(file))
            groups[gid]['depends_on'].append(base)
            fgroups.append(gid)
        names = s['names'] or [f['name'] for f in s['functions'] if f['name'] != 'callback'][:4]
        if large and gid != base:
            stem = Path(standard_target(file)).with_suffix('')
            groups[gid]['targets'] = [str(stem) + '.parts/' + (s['names'][0] if s['names'] else f'block{number}') + '.ts']
        add(file, gid, f'lines {s["line"]}-{s["end"]} {s["kind"]}: {", ".join(names)}',
            f'源语句 sha256={s["sha256"]}；保留返回、异常及 {len(s["branches"])} 个分支，调用={", ".join(s["calls"])}。',
            statement_sha256=s['sha256'], branch_lines=s['branches'], function_ranges=s['functions'])
        for name in s['names']:
            owners[(file, name)] = gid
    if large and not r.get('template'):
        assembly = group(f'{base}V', f'{short}：导出接口与调用装配', feature(file))
        groups[assembly]['depends_on'].extend(fgroups)
        fgroups.append(assembly)
        add(file, assembly, '完整文件导出接口/初始化与跨函数调用', '保持原 export 名、调用先后、共享状态；函数逐个迁移后集成，不用空函数补接口。')
    view_gid = base
    if r.get('template'):
        if large:
            view_gid = group(f'{base}V', f'{short}：页面渲染、事件接线和生命周期', feature(file))
            groups[view_gid]['depends_on'].extend(fgroups)
            fgroups.append(view_gid)
        t = r['template']
        add(file, view_gid, f'template lines {t["line"]}-{t["end"]}（完整静态文本/DOM/插槽）',
            '保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。')
        for b in t['bindings']:
            add(file, view_gid, f'template line {b["line"]}: v-{b["name"]}:{b["arg"]}',
                f'原表达式：{b["expression"]}；分别验证受控值/事件参数/分支/列表键。')
        for b in t['interpolations']:
            add(file, view_gid, f'template interpolation line {b["line"]}', f'原显示表达式：{b["expression"]}')
    for n, s in enumerate(r.get('styles', [])):
        add(file, view_gid, f'style[{n}] lines {s["line"]}-{s["end"]}',
            f'保留全部选择器、声明和 url；lang={s["lang"]}, scoped={s["scoped"]}；原样式选择器在 source-audit.json。')
    if not statements and not r.get('template'):
        add(file, base, '完整文件（包括注释、数据、配置、样式或资源）',
            f'完整内容哈希 {r["sha256"]}；二进制核实格式与引用，静态文件保留内容，配置保留实际选项/部署语义。')
    file_groups[file] = fgroups
    for gid in fgroups:
        if not groups[gid]['targets']:
            groups[gid]['targets'] = [str(Path(standard_target(file)).with_suffix(''))+'.context.ts' if large and gid == base else standard_target(file)]

# A default component import must wait for its view, not just its state context.
for file, gids in file_groups.items():
    if gids:
        owners[(file, 'default')] = next((g for g in gids if g.endswith('V')), gids[0])

def resolve(file, spec):
    if spec.startswith('@/'):
        path = ROOT / SOURCE / 'src' / spec[2:]
    elif spec.startswith('~/'):
        path = ROOT / SOURCE / spec[2:]
    elif spec.startswith('.'):
        path = ROOT / file
        path = path.parent / spec
    else:
        return None
    candidates = [path] + [Path(str(path)+s) for s in ('.js', '.vue', '.json', '.scss')] + [path / ('index'+s) for s in ('.js', '.vue')]
    for p in candidates:
        rel = str(p.resolve().relative_to(ROOT)) if p.resolve().is_relative_to(ROOT) else ''
        if rel in audit:
            return rel
    unresolved.append(dict(source=file, specifier=spec, reason='本地路径不在源快照或不存在；实施前补契约证据，不能忽略'))
    return None

# Explicit dependency inversion: these are deferred callback/registry contracts,
# never ignored edges. Original calls remain in content items and integration.
inverted = {
 ('src/utils/request.js', 'src/store/modules/user.js'): '401 重新登录回调注入；request 不静态导入用户 store',
 ('src/store/modules/user.js', 'src/router/index.js'): '退出/路由 reset 回调注入',
 ('src/store/modules/permission.js', 'src/router/index.js'): '路由注册/匹配接口注入',
 ('src/store/modules/permission.js', 'src/layout/index.vue'): '组件名→页面/布局注册表注入；权限 store 只处理路由元数据，不导入布局组件',
 ('src/router/index.js', 'src/layout/index.vue'): '路由 catalog 引用布局注册表；实际挂载在集成验证',
 ('src/store/modules/settings.js', 'src/utils/dynamicTitle.js'): 'setTitle 后的纯标题同步函数接收状态参数，避免反读 store',
}
for file, r in audit.items():
    js = r.get('scripts', []) + ([r['javascript']] if 'javascript' in r else [])
    for j in js:
        for edge in j.get('import_edges', []):
            dependency = resolve(file, edge['source'])
            if not dependency:
                continue
            srcshort, depshort = file.removeprefix(SOURCE), dependency.removeprefix(SOURCE)
            why = inverted.get((srcshort, depshort))
            runtime = edge['kind'] == 'runtime' or bool(why)
            edges.append(dict(source=file, dependency=dependency, kind='integration' if runtime else 'prerequisite',
                              basis=why or edge['kind'] + ' import', names=edge['names']))
            if not runtime:
                depgroups = set()
                for name in edge['names']:
                    depgroups.add(owners.get((dependency, name), file_groups[dependency][0] if file_groups[dependency] else 'G000'))
                for gid in file_groups[file]:
                    if gid != 'G000':
                        groups[gid]['depends_on'].extend(depgroups - {gid})
        # Function calls within a large source share an injected state context;
        # activation in context initializers is deferred to the render/wiring group.
        for s in j['statements']:
            own = next((owners[(file, n)] for n in s['names'] if (file, n) in owners), None)
            if own and 'F' in own:
                for call in s['calls']:
                    dep = owners.get((file, call))
                    if dep and dep != own:
                        groups[own]['depends_on'].append(dep)

# Track implicit global components/functions, used by Vue auto imports and main.js.
global_components = {'dict-tag':'DictTag', 'pagination':'Pagination', 'file-upload':'FileUpload',
 'business-file-upload':'BusinessFileUpload', 'image-upload':'ImageUpload', 'image-preview':'ImagePreview',
 'right-toolbar':'RightToolbar', 'editor':'Editor', 'svg-icon':'SvgIcon'}
for file, r in audit.items():
    for tag, component in global_components.items():
        if tag in r.get('template', {}).get('tags', {}) if r.get('template') else False:
            dep = SOURCE+f'src/components/{component}/index.vue'
            if dep in file_groups:
                for gid in file_groups[file]:
                    if gid.endswith('V') or len(file_groups[file]) == 1:
                        groups[gid]['depends_on'].extend(file_groups[dep])
                edges.append(dict(source=file, dependency=dep, kind='prerequisite', basis='main.js 全局组件注册'))
    identifiers = set(n for j in r.get('scripts', []) for n in j['identifiers'])
    implicit = {'useDict': 'src/utils/dict.js', 'parseTime': 'src/utils/ruoyi.js', 'resetForm': 'src/utils/ruoyi.js',
                'addDateRange': 'src/utils/ruoyi.js', 'selectDictLabel': 'src/utils/ruoyi.js', 'handleTree': 'src/utils/ruoyi.js'}
    for name, rel in implicit.items():
        dep = SOURCE+rel
        if name in identifiers and dep != file and dep in file_groups:
            for gid in file_groups[file]:
                if gid != 'G000':
                    groups[gid]['depends_on'].append(file_groups[dep][0])
            edges.append(dict(source=file, dependency=dep, kind='prerequisite', basis=f'main.js 全局函数 {name}'))

# Tarjan: retain minimal residual strongly connected components together.
counter = 0
indices, low, stack, onstack, cycles = {}, {}, [], set(), []
def visit(v):
    global counter
    indices[v] = low[v] = counter
    counter += 1
    stack.append(v); onstack.add(v)
    for w in set(groups[v]['depends_on']) - {v}:
        if w not in indices:
            visit(w); low[v] = min(low[v], low[w])
        elif w in onstack:
            low[v] = min(low[v], indices[w])
    if low[v] == indices[v]:
        comp = []
        while True:
            w = stack.pop(); onstack.remove(w); comp.append(w)
            if w == v: break
        if len(comp) > 1: cycles.append(sorted(comp))
for gid in list(groups):
    if gid not in indices: visit(gid)
aliases = {g: comp[0] for comp in cycles for g in comp}
for comp in cycles:
    root = comp[0]
    groups[root]['title'] += '（最小互依能力闭环）'
    groups[root]['cycle_members'] = comp
    groups[root]['depends_on'] = sorted({aliases.get(d, d) for g in comp for d in groups[g]['depends_on']} - {root})
    groups[root]['targets'] = sorted({p for g in comp for p in groups[g]['targets']})
    for gid in comp[1:]: groups.pop(gid)
for g in groups.values():
    g['depends_on'] = sorted({aliases.get(d, d) for d in g['depends_on']} - {g['id']})
for i in items:
    if i['group']: i['group'] = aliases.get(i['group'], i['group'])
    if i['group'] != 'G000' and i['disposition'] != 'exclude':
        i['targets'] = groups[i['group']]['targets'] or [standard_target(i['source'])]

integration = []
for feat in sorted({g['feature'] for g in groups.values()}):
    cid = f'J{len(integration):03}'
    members = [g['id'] for g in groups.values() if g['feature'] == feat]
    contract = f'migration/state/integration/{cid}-contract.md'
    integration.append(dict(id=cid, groups=members, contract=contract, status='pending'))
    path = ROOT / contract; path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f'# {cid} {feat} 集成\n\n覆盖组：{", ".join(members)}\n\n'
                    '原版依据：各组逐项源定位与 source-audit.json。按原入口固定数据、权限、时区/语言，重放成功、失败、取消、刷新与深链接。\n\n'
                    '工具验证真实调用参数/返回；共享组件验证实际页面 props/事件；资源查真实加载和原界面对照；动态路由、glob 与注册关系按 dependency-edges.json 核对。\n\n'
                    '未迁页面、缺失外部测试夹具或后端环境不能记通过。每组本地检查通过不等于本项集成通过。\n')

for gid, g in groups.items():
    owned = [i for i in items if i['group'] == gid]
    path = ROOT / g['contract']; path.parent.mkdir(parents=True, exist_ok=True)
    content = [f'# {gid} {g["title"]}', '', f'依赖：{", ".join(g["depends_on"]) or "无"}', '',
      '本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。', '',
      '逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：', '']
    for i in owned:
        content.extend([f'- {i["id"]} `{i["source"]}` {i["locator"]}', f'  - 基线：{i["basis"]}', f'  - 去向：{", ".join(i["targets"]) or "由本组实施登记"}'])
    content.extend(['', '验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。', '',
      '大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。', '',
      '全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。', '',
      '待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。'])
    path.write_text('\n'.join(content)+'\n')

plan = dict(schema_version=1, inventory_digest=inv['digest'], files={p:dict(sha256=r['sha256'], reviewed=True,
       review_level='full-file-structural', review_evidence=f'migration/state/source-audit.json [{p}]：读取全部字节；JS/Vue 严格 AST，无解析错误；结构内容全部登记，语义待逐组验证。') for p,r in audit.items()},
       items=items, groups=list(groups.values()), integration_checks=integration, active_group=None, active_feature=None)
(STATE/'plan.json').write_text(json.dumps(plan, ensure_ascii=False, indent=2)+'\n')
(STATE/'dependency-edges.json').write_text(json.dumps(dict(edges=edges, unresolved=unresolved, minimal_cycles=cycles,
    dynamic_registry={'source':'src/utils/pluginViewResolver.js', 'coverage':'plugins/**/views/**/*.vue 与 src/views/**/*.vue 的完整清单；实际映射由视图解析组及 J 集成检查'},
    inversion_contracts=[dict(source=a, dependency=b, method=why) for (a,b),why in inverted.items()]), ensure_ascii=False, indent=2)+'\n')
with (STATE/'coverage.md').open('w') as f:
    f.write('# 文件覆盖表\n\n结构盘点，不能作为语义迁移完成证明。目标为计划去向，实际实施后登记定位和验证。\n\n| 源文件 | 哈希前缀 | 内容项数 | 小组 | 状态 |\n|---|---|---:|---|---|\n')
    for p,r in audit.items():
        own=[i for i in items if i['source']==p]
        f.write(f'| `{p}` | {r["sha256"][:12]} | {len(own)} | {", ".join(sorted({i["group"] for i in own if i["group"]})) or "exclude：重建锁文件"} | pending |\n')
print(json.dumps(dict(files=len(audit),items=len(items),groups=len(groups),integration=len(integration),cycles=cycles,unresolved=unresolved),ensure_ascii=False))
