"""Build a reviewable plan from the frozen audit and manually selected capabilities.
This writes planning artifacts only. It neither selects nor implements a group.
"""
from pathlib import Path
import collections
import fnmatch
import glob
import json
import re
import sys
sys.dont_writebytecode = True
from capabilities import GROUPS, API_OVERRIDES, INTEGRATIONS

ROOT = Path(__file__).resolve().parents[3]
STATE = ROOT / 'migration/state'
PREFIX = 'ruoyi-fastapi-frontend/'
def read(p): return json.loads((STATE / p).read_text())
def save(p, data):
    dst = STATE / p
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
def md(p, text):
    dst = STATE / p
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text.rstrip()+'\n')
inv = read('inventory.json')
audit = read('source-audit.json')
previous = read('plan.json')
assert not previous.get('active_group') and not previous.get('active_feature'), 'Do not overwrite an active round'
assert all(g.get('status')=='pending' and not g.get('validation') for g in previous.get('groups', [])), 'This generator only creates a fresh pending plan; preserve executed groups manually'
assert all(j.get('status')=='pending' and not j.get('validation') for j in previous.get('integration_checks', [])), 'Do not erase integration results'
assert not audit['errors'] and set(audit['files']) == set(inv['files'])
group_count = len(GROUPS)
keys = {g['key']:g for g in GROUPS}
ids = {g['key']:f'G{i:03}' for i,g in enumerate(GROUPS,1)}
owners = {}
for file in inv['files']:
    local = file.removeprefix(PREFIX)
    matches = [g['key'] for g in GROUPS if any(fnmatch.fnmatchcase(local,p) for p in g['patterns'])]
    assert len(matches)==1, (file,matches)
    owners[file]=matches[0]

def target(file, key=None):
    p=file.removeprefix(PREFIX)
    if p.endswith('.vue'): p=p[:-4]+'.tsx'
    elif p.endswith('.js'):
        p=p[:-3]+('.tsx' if p in ['src/utils/generator/render.js','src/main.js'] else '.ts')
    if key and file.removeprefix(PREFIX) in API_OVERRIDES and key!=owners[file]:
        # A separately owned adapter never appends to another passed group's file.
        p=str(Path(p).with_name(Path(p).stem+'-'+key+Path(p).suffix))
    if p.startswith('vite/plugins/'):
        p='vite.config.ts'  # Vue-only build hooks become explicit React configuration.
    return 'react-front/'+p

items=[]
export_owner={}
file_items=collections.defaultdict(list)
def add(file, locator, basis, key=None, disposition='migrate', reason=None, t=None):
    item={'id':f'I{len(items)+1:04}', 'source':file,'locator':locator,
          'basis':basis,'disposition':disposition,'targets':[] if disposition=='exclude' else [t or target(file,key)],
          'target_locator':locator+'；React 框架适配保持同一可观察语义' if disposition=='migrate' else '完整文件内容与引用'}
    if disposition=='exclude':item['reason']=reason
    else:item['group']=ids[key or owners[file]]
    items.append(item);file_items[file].append(item)

for file, f in audit['files'].items():
    local=file.removeprefix(PREFIX); owner=owners[file]
    if local=='package-lock.json':
        add(file,'完整 npm lock v'+str(f['lock']['version']),
            '完整解析锁文件；根依赖与源 package.json 对应，packageCount='+str(f['lock']['packageCount']),
            disposition='exclude',reason='Vue 工程依赖锁不适用于 React 依赖图；目标工程重新生成 package-lock.json，保留源文件快照而非忽略该文件。')
        continue
    if local in API_OVERRIDES:
        funcs=[x for s in f['sections'] for x in s.get('semantics',{}).get('functions',[]) if x['name'] not in ['<callback>','default']]
        assert len({x['name'] for x in funcs})==len(funcs)
        for x in funcs:
            key=API_OVERRIDES[local].get(x['name'],owner)
            export_owner[(file,x['name'])]=key
            api=[a for s in f['sections'] for a in s.get('semantics',{}).get('api',[]) if x['start']<=a['line']<=x['end']]
            add(file,f"L{x['start']}-L{x['end']} 完整导出 {x['name']}",
                '完整函数、请求配置、辅助变量与错误传播；'+json.dumps(api,ensure_ascii=False),key)
        add(file,'模块导入、注释及函数之间全部剩余内容',
            '整文件已解析；公共 import 需要分别组织到各能力适配器，不直接复制 Vue import 或重复实现 API 导出。默认分区维护其所需导入。',owner)
        continue
    for s in f['sections']:
        name=s['name']; sem=s.get('semantics',{})
        locator=f"L{s['start']}-L{s['end']} {name} 完整内容"
        if name.startswith('script') or name=='module':
            basis='完整解析全部导入/导出、声明、函数/状态、条件/返回、请求与副作用；能力行为见本组合同；函数：'+', '.join(dict.fromkeys(x['name'] for x in sem.get('functions',[])))
            if sem.get('effects'):basis+='；副作用/props/emits/lifecycle 见 source-audit.json 对应 sections'
        elif name=='template':
            basis='完整解析全部模板元素、文本、插值、条件、循环、事件、插槽、绑定和权限；组件：'+', '.join(sem['tags'])+'；全部表达式定位见 source-audit.json'
        elif name.startswith('style'):
            basis='完整读取所有选择器、声明、嵌套、scoped/deep 与资源引用；React/Ant Design 样式需实测适配，不能直接以源 Element class 作为完成证据。'
        elif f['type']=='environment':
            basis='完整读取环境文件并只登记键名：'+', '.join(f['keys'])+'；值不复制到报告，实施在目标工程按原环境安全配置。'
        elif f['type']=='binary-asset' or local.endswith('.svg'):
            basis='完整读取资源并登记格式/签名、哈希和原引用用途；不转译像素/SVG路径，目标完整复制后验证引用与实际显示。'
        else:
            basis='完整读取配置/文档/HTML/脚本；键、入口、依赖、启动/部署和框架相关部分逐项适配，原业务用途见本组合同。'
        reuse = f['type']=='binary-asset' or local.endswith('.svg') or local=='LICENSE'
        add(file,locator,basis,owner,'reuse' if reuse else 'migrate')
    if f['type']=='vue-sfc':
        add(file,'SFC 外壳、块属性与全部块间注释',
            'script/template/style 已独立覆盖；name/setup/scoped/lang、组件导出与文件级注释/空白的剩余区域随完整组件处理。',owner)

edges=read('dependency-edges.json')['edges']
expanded=[]
for e in edges:
    if e['kind']=='glob':
        p=Path(e['from']).parent/e['spec']
        paths=glob.glob(str(ROOT/p),recursive=True)
        for path in sorted(paths):
            rel=Path(path).resolve().relative_to(ROOT).as_posix()
            if rel in owners: expanded.append(dict(e,kind='local',target=rel,via='glob-match'))
        assert any(x['from']==e['from'] and x['via']=='glob-match' for x in expanded), e
    else:expanded.append(e)

# Also cover template assets, stylesheet links and the HTML/runtime entry. Values
# are never recorded here for env files or cryptographic key declarations.
for file,f in audit['files'].items():
    if f['type']=='binary-asset' or f['type']=='environment':continue
    text=(ROOT/file).read_text(encoding='gb18030' if f.get('encoding')=='gb18030' else 'utf-8-sig')
    refs=[]
    if file.endswith(('.vue','.scss','.html')):
        refs=re.findall(r'(?:src\s*=\s*[\"\']|url\(\s*[\"\']?|@import\s+[\"\'])([^\"\'\s);]+)',text)
    for spec in refs:
        if spec.startswith('@/'):base=PREFIX+'src/'+spec[2:]
        elif spec.startswith('/src/'):base=PREFIX+spec[1:]
        elif spec.startswith('.'):base=str((ROOT/Path(file).parent/spec).resolve().relative_to(ROOT))
        elif spec.startswith(('http:','https:','data:','#')):continue
        else:base=str(Path(file).parent/spec)
        for p in [base,base+'.scss']:
            if p in owners:
                expanded.append({'from':file,'target':p,'kind':'local','via':'asset/style/entry','spec':spec});break

template_groups={'dict-tag':'dict','pagination':'table','right-toolbar':'table','file-upload':'fileupload',
                 'business-file-upload':'businessupload','image-upload':'images','image-preview':'images',
                 'editor':'editor','svg-icon':'icons','business-date-time-picker':'time'}
global_groups={'useDict':'dict','download':'http','resetForm':'data','parseTime':'data','handleTree':'data',
               'addDateRange':'data','selectDictLabel':'data','selectDictLabels':'data',
               'getConfigKey':'http','$modal':'http','$download':'download','$tab':'tabs','$auth':'session','$cache':'data'}
for file,f in audit['files'].items():
    if f['type']!='vue-sfc':continue
    for s in f['sections']:
        sem=s.get('semantics',{})
        if s['name']=='template':
            for tag in sem['tags']:
                # PascalCase and kebab-case registrations share the same provider.
                kebab=re.sub(r'(?<!^)(?=[A-Z])','-',tag).lower()
                if kebab in template_groups:expanded.append({'from':file,'kind':'capability','provider':template_groups[kebab],'via':'global-template','spec':tag})
            if any(d['name'] in ['hasPermi','hasRole','has-permi','has-role'] for d in sem['directives']):
                expanded.append({'from':file,'kind':'capability','provider':'session','via':'permission-directive','spec':'hasPermi/hasRole'})
            if any(d['name'] in ['copyText','copy-text'] for d in sem['directives']):
                expanded.append({'from':file,'kind':'capability','provider':'data','via':'copy-directive','spec':'copyText'})
    text=(ROOT/file).read_text()
    for name,key in global_groups.items():
        if (name.startswith('$') and 'proxy.'+name in text) or (not name.startswith('$') and re.search(r'\b'+re.escape(name)+r'\s*\(',text)):
            expanded.append({'from':file,'kind':'capability','provider':key,'via':'global-helper','spec':name})

deps={g['key']:set(g['deps']) for g in GROUPS}
classified=[]
def inverted(a,b,e):
    if a=='http' and b=='session':return 'HTTP 接收 session-expired handler；会话组注册真实注销/跳转，J001/J002验收。'
    if a=='theme' and b in ['shell','session','tabs']:
        return '设置抽屉接收导航状态/重置侧边路由/标签清理回调；主题状态独立，shell接真实实现，J002/J009验收。'
    if a=='session' and (e.get('via') in ['dynamic-import','glob-match'] or e['from'].endswith(('/router/index.js','/store/modules/permission.js'))) and b not in ['http','data','time','theme','password']:
        return '路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。'
    if a=='embed' and b=='tabs':return '内嵌组件接收 iframeViews 查询/关闭接口；tabs提供真实状态，shell装配，J002/J007验收。'
    if a=='build' and e.get('via')=='asset/style/entry':return 'index.html 的运行入口随 shell 装配；工程组先验证实际空React启动入口，J001/J010检查最终入口。'
    return None

for e in expanded:
    a=owners[e['from']]
    # API modules partitioned by actual exports: consumer named imports depend
    # on the owner of that export, not on an unrelated administration page.
    if e['kind']=='local':
        t=e['target']; bindings=e.get('bindings',[])
        if t.removeprefix(PREFIX) in API_OVERRIDES:
            named=[b['imported'] for b in bindings if b['imported'] not in ['default','*']]
            bs={export_owner[(t,n)] for n in named} if named else {owners[t]}
        else:bs={owners[t]}
        # Within partitioned source API files each capability needs these same
        # imported helpers; do not lose a profile/ACL adapter prerequisite.
        aa={a} | {export_owner[(e['from'],n)] for n in API_OVERRIDES.get(e['from'].removeprefix(PREFIX),{})}
    elif e['kind']=='capability':bs={e['provider']};aa={a}
    else:
        classified.append(dict(e,classification='missing-input' if e['kind']=='unresolved-local' else 'external-package',from_group=ids[a]));continue
    for src in sorted(aa):
        for b in sorted(bs):
            reason=inverted(src,b,e) if src!=b else None
            if src==b:classification='internal-capability'
            elif reason:classification='injected-interface/final-assembly'
            else:classification='prerequisite';deps[src].add(b)
            classified.append(dict(e,from_group=ids[src],to_group=ids[b],classification=classification,**({'reason':reason} if reason else {})))

# Verify the semantic graph before writing. Removing a cycle is never automatic.
ordered=[];remaining=set(deps)
while remaining:
    available=[k for k in remaining if not (deps[k] & remaining)]
    if not available:
        raise RuntimeError('Review/merge actual capability cycle: '+repr({k:sorted(deps[k]&remaining) for k in remaining}))
    available.sort(key=lambda k:ids[k]);ordered.extend(available);remaining.difference_update(available)

plan={'schema_version':1,'inventory_digest':inv['digest'],'files':{},'items':items,'groups':[],
      'integration_checks':[],'active_group':None,'active_feature':None,
      'architecture':{'source':'Vue 3 + Element Plus + Pinia + Vue Router','target':'React + TypeScript + Vite + React Router + Ant Design + Context',
                      'rule':'仅迁移前端运行实现，保留后端API、插件组件标识与生成器现有Vue产品格式。'},
      'planning_basis':'源代码静态行为与全文结构审阅；未运行浏览器/后端等价验证。合同是待验收条件，不是通过证据。',
      'dependency_evidence':'migration/state/dependency-review.json',
      'verification_gaps':[{'source':PREFIX+'tests/time/time.test.js','missing':'ruoyi-fastapi-test/time-contract/contract.mjs',
                            'group':ids['time'],'status':'unresolved','impact':'不能声称原 test:time 已通过；需恢复可信契约或登记基于旧源码的明确替代测试依据。'}]}
for file,f in audit['files'].items():
    owner_groups=sorted({i['group'] for i in file_items[file] if i.get('group')})
    plan['files'][file]={'sha256':f['sha256'],'reviewed':True,
        'review_evidence':'全文读取与解析：migration/state/source-audit.json#files/'+file+
        '；全部区段/资源/配置用途映射：'+', '.join(i['id'] for i in file_items[file])+
        '；业务边界与可观察行为条件：'+(', '.join('migration/state/groups/'+i+'/contract.md' for i in owner_groups) or 'migration/planning-summary.md 的锁文件排除复核')}

for spec in GROUPS:
    key=spec['key'];gid=ids[key];owned=[i for i in items if i.get('group')==gid]
    scope='本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；'+spec['notes']
    group={'id':gid,'title':spec['title'],'feature':key if spec['phase'] in ['入口','业务'] else 'shared',
           'outcome':spec['outcome'],'scope':scope,'split_reason':spec['notes'],
           'entry_priority':0 if spec['phase']=='基础' else 1 if spec['phase']=='入口' else 2,
           'depends_on':sorted(ids[d] for d in deps[key]),'contract':f'migration/state/groups/{gid}/contract.md',
           'targets':[],'status':'pending','phase':spec['phase'],'source_files':sorted({i['source'] for i in owned})}
    if key=='build': group['targets']=['react-front/tsconfig.json','react-front/tsconfig.app.json','react-front/tsconfig.node.json','react-front/package-lock.json','react-front/src/main.tsx']
    if key=='session':group['targets']=['react-front/src/router/viewRegistry.ts','react-front/src/context/SessionContext.tsx']
    if key=='shell':group['targets']=['react-front/src/context/AppContext.tsx','react-front/src/router/registerViews.ts']
    if key=='tabs':group['targets']=['react-front/src/components/PageCache/index.tsx']
    plan['groups'].append(group)
    depnames=', '.join(ids[d]+' '+keys[d]['title'] for d in sorted(deps[key],key=lambda x:ids[x])) or '无'
    parts=[f'# {gid} {spec["title"]}', '',f'状态：pending。源清单：`{inv["digest"]}`。仅规划，未实施/未验收。',
           '', '## 可观察交付与边界','',spec['outcome'], '',scope,'', '依赖：'+depnames,
           '', '## 正常、异常与边界检查条件','']
    parts += [f'{n}. {c}' for n,c in enumerate(spec['cases'],1)]
    parts += ['', '这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。',
              '', '## 验证与证据','',
              '- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。',
              '- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。',
              '- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。',
              '- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。',
              '', '## 全部源内容与目标映射','', '| 项 | 原文件/定位 | 目标 |','| --- | --- | --- |']
    for i in owned:
        parts.append('| '+i['id']+' | '+i['source']+' / '+i['locator'].replace('|','\\|')+' | '+', '.join(i['targets'])+' |')
    parts+=['','完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。',
            '', '## 原版行为定位与请求清单','']
    for file in group['source_files']:
        f=audit['files'][file]
        parts += ['### '+file,'']
        for s in f['sections']:
            sem=s.get('semantics',{})
            funcs=sem.get('functions',[])
            if file.removeprefix(PREFIX) in API_OVERRIDES:
                funcs=[x for x in funcs if export_owner.get((file,x['name']))==key]
            if funcs:parts.append('逻辑定位：'+', '.join(f"{x['name']}@L{x['start']}–{x['end']}" for x in funcs)+'.')
            if sem.get('api'):
                for a in sem['api']:
                    if file.removeprefix(PREFIX) in API_OVERRIDES and not any(x['start']<=a['line']<=x['end'] for x in funcs):continue
                    # These object URL records may also be UI data objects; label
                    # them accurately rather than calling every URL an endpoint.
                    parts.append(f"- URL/请求对象 L{a['line']}: `{a['method'] or '(非请求URL对象)'} {a['url']}`; params=`{a['params']}`, data=`{a['data']}`")
            if s['name']=='template':
                ev=[d for d in sem['directives'] if d['name'] in ['on','hasPermi','hasRole']]
                parts.append('全部模板事件/权限：'+'; '.join(f"{d.get('arg','')}={d['expression']}@L{d['line']}" for d in ev)+'.')
        parts.append('')
    interfaces=[e for e in classified if e.get('from_group')==gid and e['classification']=='injected-interface/final-assembly']
    if interfaces:
        parts+=['## 源循环/延后装配的明确接口','']
        for e in interfaces:
            parts.append(f"- `{e['from']}` → `{e.get('target','')}` ({e.get('to_group','')}): {e['reason']}")
        parts+=['','这些源关系保留在 dependency-review.json；只是将运行依赖改为显式接口注入，未删除功能。最终必须以真实页面/服务接线验收。']
    md(f'groups/{gid}/contract.md','\n'.join(parts))

for iid,title,selection,checks in INTEGRATIONS:
    chosen=list(ids.values()) if selection=='ALL' else [ids[g['key']] for g in GROUPS if g['phase'] in selection or g['key'] in selection]
    assert chosen
    contract=f'migration/state/integration/{iid}-contract.md'
    plan['integration_checks'].append({'id':iid,'title':title,'groups':chosen,'contract':contract,'status':'pending'})
    md(f'integration/{iid}-contract.md',f'# {iid} {title}\n\n状态：pending。尚无原版/目标浏览器或真实后端验证证据。\n\n覆盖组：'+', '.join(chosen)+'\n\n'+
       '\n'.join(f'{i}. {s}' for i,s in enumerate(checks,1))+
       '\n\n验证时保存同环境原版/目标截图、真实网络请求、测试与构建日志。涉及写操作使用明确的测试数据/环境，遵循用户的实施授权；本计划不执行任何后端写入。\n\n仅此合同存在不表示通过。结果单独写入 '+iid+'-result.md，以真实独立证据调用 record；最后运行 check --final。')
save('plan.json',plan)
save('dependency-review.json',{'original_static_edges':len(edges),'expanded_and_implicit_edges':len(classified),
     'rule':'所有源导入保留；分区API按实际导出归属建边，原循环改显式接口并要求最终装配验证；未解决本地引用登记missing-input。',
     'edges':classified,'topological_order':[ids[k] for k in ordered]})

counts=collections.Counter(g['phase'] for g in GROUPS)
disp=collections.Counter(i['disposition'] for i in items)
single=[g for g in plan['groups'] if sum(i.get('group')==g['id'] for i in items)==1]
multi={f:sorted({i['group'] for i in its if i.get('group')}) for f,its in file_items.items() if len({i.get('group') for i in its if i.get('group')})>1}
pages=[]
for file,f in audit['files'].items():
    if f['type']=='vue-sfc':pages.append({'source':file,'main_groups':[ids[owners[file]]], 'count':1})
summary={'files':len(inv['files']),'items':len(items),'groups':len(GROUPS),'phase_counts':dict(counts),
         'dispositions':dict(disp),'integration_checks':len(INTEGRATIONS),'minimum_logical_rounds':group_count+1,
         'single_item_groups':[g['id'] for g in single],'multi_group_files':multi,'page_component_groups':pages,
         'maximum_main_groups_per_sfc':1,'all_pending':True}
save('grouping-review.json',summary)
lines=['# 全项目 Vue → React 迁移计划（重新开始）','',
       f'源码快照：`{inv["digest"]}`。范围：`ruoyi-fastapi-frontend/` → `react-front/`；339 个文件，'+str(len(items))+' 个内容映射，55 个执行组。',
       '', '## 轮次与范围','',
       '**按“一组完整迁移并验收＝一轮”计算，55 轮能力迁移，再加 1 个整体验收/收尾阶段，基线约 56 个逻辑轮。**',
       '这不是56次CLI调用或56次对话的保证。每组包含选组、实施、验证；大组跨会话续做、验证失败修复和共享依赖复验会增加实际调用/会话次数。当前没有实际耗时或失败率数据，不虚构完成日期或轮次上限。',
       '',f'基础 {counts["基础"]} 组；公共 {counts["公共"]} 组；入口 {counts["入口"]} 组；业务 {counts["业务"]} 组。10 项集成合同在各组完成后作为一个收尾阶段逐项执行。',
       '', '旧计划773组是此前会话审阅的比较数据；本轮从源码重新生成，未继承旧进度。此次55组比旧记录减少约93%，覆盖范围没有按组数缩减。',
       '', '## 分组复核','',
       '- 125 个 Vue SFC 各有一个主要交付组，没有一个页面/组件超过5组。所有细粒度函数/模板节点/样式都归所属完整能力，不各自生成执行轮。',
       '- 文件管理、插件管理、表单设计器、AI聊天、任务管理各保留完整业务状态与子组件，组内分步骤续做，不用“状态壳→函数→装配”制造组。',
       '- Cron 的九个内部文件同组；96个SVG图标同组；time.js全部时区/格式化/提交与日期输入同组。',
       '- 字典类型/数据/详情形成同一维护闭环；两个Redis入口形成同一缓存管理能力。用户/角色授权与个人中心是独立真实页面，保留单独能力组。',
       '- 同一源文件跨组只发生在8个共享API模块。按完整导出分区是覆盖映射，不额外创建API函数执行组；目标独立适配文件避免后续组反复改动已通过目标。',
       '- 单内容项组复核：'+(', '.join(g['id']+' '+g['title'] for g in single) or '无')+'。G011包含一个完整下载模块的四类入口、Range校验、重试/回退与Blob组装，能够独立复用与验证，故保留一组。普通单文件SFC还包括脚本/模板/样式项；不因内容项数自动合并无关能力。',
       '', '依赖从静态/动态import、glob、模板全局组件、helper、权限指令和资源引用建立；完整边及循环处理理由见 `state/dependency-review.json`。HTTP与会话、主题与导航、路由与视图、iframe与标签的反向关系通过显式接口注入解决，全部真实接线仍需集成验收。',
       '', '## 保留的原行为与验证缺口','',
       '- 时间测试引用的 `ruoyi-fastapi-test/time-contract/contract.mjs` 在工作区缺失。测试本身计入清单；需恢复可信契约或从旧源码建立明确替代用例并记录依据，未标通过。',
       '- AI使用逐行JSON流（NDJSON），不是SSE；React渲染库替换与后端plugin.yaml仍声明Vue npm依赖的兼容性需要真实环境验证，不改后端清单冒充迁移完成。',
       '- 表单设计器及后端代码生成器当前产出Vue文件/模板。这是产品功能，React运行界面迁移仍保留该输出；若要同时生成React业务代码，是另一个范围变更。',
       '- Druid当前页面只显示“我是数据监控”，iframe已注释，按此原行为迁移；Swagger则连接 `/proxy-docs`。不把当前未实现的控制台新增为迁移要求。',
       '- 路由获取Promise失败、redirect查询字符串、字典旧过滤器写法、AI配置字符串布尔判断/无换行尾块、部分请求失败loading等存在原版边界差异观察点。合同明确对照；未运行原版与React浏览器验证，不宣称这些已修复或等价。',
       '- 默认仅排除依赖/产物目录，实际清单排除只有node_modules；未引用的源码/样式/测试/资源仍在339文件内。内容排除只有Vue package-lock.json，新React锁文件由工程组生成。',
       '', '## 完整执行组','', '| 组 | 交付能力 | 类别 | 前置组 |','| --- | --- | --- | --- |']
for g in plan['groups']:
    lines.append(f"| [{g['id']}](state/groups/{g['id']}/contract.md) | {g['title']} | {g['phase']} | {', '.join(g['depends_on']) or '无'} |")
lines += ['', '## 逐页面/组件范围','', '| 原组件/页面 | 主要执行组 | 数量 |','| --- | --- | --- |']
for p in pages:lines.append(f"| {p['source'].removeprefix(PREFIX)} | {p['main_groups'][0]} | 1 |")
lines += ['', '## 跨组API源码复核','']
for f,gs in multi.items():lines.append('- '+f+': '+', '.join(gs)+'；具体完整导出归属见 plan.json，目标按能力独立适配。')
lines += ['', '## 审阅、验证与交接','',
          '`state/inventory.json` 由固定盘点脚本生成；`source-audit.json` 全文解析所有源内容；`plan.json` 保存逐项映射；55份组合同含具体正常/异常/边界条件，10份集成合同含最终真实接线场景。',
          '结构检查 `migration_state.py check` 只能证明清单/登记/快照/依赖合法，不证明业务等价；所有组和集成均为pending，active_group/active_feature为空。React目录仍为空。本阶段只生成计划，未选下一组或实施业务。',
          '下一阶段用 `migration-next-group` 按依赖自动选唯一组，读合同后完整实施与验证；第一组应是G001工程基础。']
md('../planning-summary.md','\n'.join(lines))
print(json.dumps({k:v for k,v in summary.items() if k not in ['page_component_groups','multi_group_files']},ensure_ascii=False))
