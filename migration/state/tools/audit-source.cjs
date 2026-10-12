// Read the frozen inventory in full. Structural evidence supplements, not replaces,
// the capability/behavior review documented in the contracts.
const fs = require('node:fs');
const path = require('node:path');
const { createRequire } = require('node:module');
const root = path.resolve(__dirname, '../../..');
const req = createRequire(path.join(root, 'ruoyi-fastapi-frontend/package.json'));
const babel = req('@babel/parser');
const sfc = req('@vue/compiler-sfc');
const dom = req('@vue/compiler-dom');
const inv = JSON.parse(fs.readFileSync(path.join(root, 'migration/state/inventory.json')));
const known = new Set(Object.keys(inv.files));
const audit = {}, edges = [], errors = [];
const clean = (s, n = 240) => String(s).replace(/\s+/g, ' ').slice(0, n);
function resolve(from, spec) {
  let base;
  if (spec.startsWith('@/')) base = 'ruoyi-fastapi-frontend/src/' + spec.slice(2);
  else if (spec.startsWith('~/')) base = 'ruoyi-fastapi-frontend/' + spec.slice(2);
  else if (spec.startsWith('.')) base = path.posix.normalize(path.posix.join(path.posix.dirname(from), spec));
  else return { kind: 'external', target: spec };
  for (const p of [base, ...['.js','.vue','.json','.ts','.mjs','/index.js','/index.vue'].map(x=>base+x)]) {
    if (known.has(p)) return { kind: 'local', target: p };
  }
  return { kind: 'unresolved-local', target: base };
}
function walk(node, fn, parent) {
  if (!node || typeof node !== 'object') return;
  if (node.type) fn(node, parent);
  for (const [k,v] of Object.entries(node)) {
    if (['loc','start','end','extra','comments','tokens'].includes(k)) continue;
    if (Array.isArray(v)) v.forEach(x=>walk(x,fn,node));
    else if (v && typeof v==='object') walk(v,fn,node);
  }
}
function script(file, content, offset) {
  const ast = babel.parse(content, { sourceType:'unambiguous', plugins:['jsx','importMeta','topLevelAwait'], errorRecovery:false });
  const result = { functions:[], declarations:[], imports:[], exports:[], effects:[], api:[], constraints:[] };
  const slice = n => clean(content.slice(n.start,n.end));
  walk(ast,(n,parent)=>{
    if (n.type==='ImportDeclaration' || (n.type.startsWith('Export') && n.source)) {
      const spec=n.source.value, r=resolve(file,spec);
      result.imports.push(spec); edges.push({from:file,spec,...r,via:n.type,line:n.loc.start.line+offset,
        bindings:(n.specifiers||[]).map(s=>({local:s.local?.name,imported:s.imported?.name||s.imported?.value|| (s.type==='ImportDefaultSpecifier'?'default':'*')}))});
    }
    if (n.type==='CallExpression' && (n.callee.type==='Import' || slice(n.callee)==='require') && n.arguments[0]?.type==='StringLiteral') {
      const spec=n.arguments[0].value; edges.push({from:file,spec,...resolve(file,spec),via:'dynamic-import',line:n.loc.start.line+offset});
    }
    if (n.type==='CallExpression' && /^import\.meta\.glob/.test(slice(n.callee))) {
      result.effects.push(slice(n)); edges.push({from:file,spec:n.arguments[0]?.value,kind:'glob',via:'glob',line:n.loc.start.line+offset});
    }
    if (n.type==='ExportNamedDeclaration' || n.type==='ExportDefaultDeclaration') result.exports.push(clean(slice(n),150));
    if (n.type==='VariableDeclarator') result.declarations.push({name:slice(n.id),line:n.loc.start.line+offset});
    if (/FunctionDeclaration|FunctionExpression|ArrowFunctionExpression|ObjectMethod/.test(n.type)) {
      let name=n.id?.name || (n.key ? slice(n.key) : parent?.type==='VariableDeclarator' ? slice(parent.id) : parent?.key ? slice(parent.key) : '<callback>');
      if (name !== '<callback>') {
        const calls=[], conditions=[], returns=[];
        walk(n.body,(c)=>{
          if (c.type==='CallExpression' || c.type==='NewExpression') calls.push(slice(c.callee));
          if (c.type==='IfStatement' || c.type==='ConditionalExpression') conditions.push(slice(c.test));
          if (c.type==='ReturnStatement') returns.push(c.argument ? slice(c.argument) : 'void');
        });
        result.functions.push({name,start:n.loc.start.line+offset,end:n.loc.end.line+offset,params:n.params?.map(slice),calls:[...new Set(calls)],conditions:[...new Set(conditions)],returns:[...new Set(returns)]});
      }
    }
    if (n.type==='ObjectExpression') {
      const p = Object.fromEntries(n.properties.filter(x=>x.type==='ObjectProperty' && !x.computed).map(x=>[x.key.name||x.key.value,x.value]));
      if(p.url) result.api.push({url:slice(p.url),method:p.method ? slice(p.method) : null,params:p.params ? slice(p.params) : null,data:p.data ? slice(p.data) : null,line:n.loc.start.line+offset});
    }
    if (n.type==='CallExpression' && /^(watch|watchEffect|onMounted|onBeforeMount|onUnmounted|onBeforeUnmount|defineProps|defineEmits|defineExpose|app\.|window\.|document\.)/.test(slice(n.callee))) result.effects.push(slice(n));
    if (n.type==='ObjectProperty' && /^(required|min|max|pattern|validator|trigger|limit|fileSize|fileType)$/.test(n.key.name||n.key.value)) result.constraints.push({line:n.loc.start.line+offset,value:slice(n)});
  });
  return result;
}
for(const [file,meta] of Object.entries(inv.files)) {
  const bytes=fs.readFileSync(path.join(root,file));
  const ext=path.extname(file);
  const r={sha256:meta.sha256,bytes:bytes.length,sections:[]};
  try {
    if (['.png','.jpg','.jpeg','.gif','.ico'].includes(ext)) {
      r.type='binary-asset';r.signature=bytes.subarray(0,12).toString('hex');r.sections.push({name:'asset',start:1,end:1});
    } else {
      let text;
      try { text=new TextDecoder('utf-8',{fatal:true}).decode(bytes);r.encoding='utf-8'; }
      catch { text=new TextDecoder('gb18030',{fatal:true}).decode(bytes);r.encoding='gb18030'; }
      r.lines=text.split('\n').length;r.type='text';
      if(ext==='.vue') {
        r.type='vue-sfc';const parsed=sfc.parse(text,{filename:file});
        if(parsed.errors.length) throw new Error(parsed.errors.join(';'));
        const d=parsed.descriptor;
        for(const [name,b] of [['script',d.script],['script-setup',d.scriptSetup]]) if(b) {
          const start=b.loc.start.line; r.sections.push({name,start,end:b.loc.end.line,semantics:script(file,b.content,start-1)});
        }
        if(d.template) {
          const t=dom.parse(d.template.content), tags=new Set(), texts=new Set(), directives=[], attributes=[];
          function scan(n){
            if(n.type===1) {tags.add(n.tag);for(const p of n.props){if(p.type===7)directives.push({name:p.name,arg:p.arg?.content,expression:clean(p.exp?.content||''),line:p.loc.start.line+d.template.loc.start.line-1});else if(['label','title','placeholder','prop','type','permission'].includes(p.name))attributes.push({name:p.name,value:p.value?.content});}n.children.forEach(scan);}
            else if(n.type===0) n.children.forEach(scan);
            else if(n.type===2 && n.content.trim()) texts.add(clean(n.content,100));
            else if(n.type===5) directives.push({name:'interpolation',expression:clean(n.content.content),line:n.loc.start.line+d.template.loc.start.line-1});
          } scan(t);
          r.sections.push({name:'template',start:d.template.loc.start.line,end:d.template.loc.end.line,semantics:{tags:[...tags],texts:[...texts],directives,attributes}});
        }
        d.styles.forEach((b,i)=>r.sections.push({name:'style-'+(i+1),start:b.loc.start.line,end:b.loc.end.line,lang:b.lang||'css',scoped:b.scoped,selectors:[...b.content.matchAll(/([^{}]+)\{/g)].map(x=>clean(x[1])),references:[...b.content.matchAll(/(?:@import\s+|url\()([^)\n;]+)/g)].map(x=>clean(x[1]))}));
        // Remaining comments and block metadata remain covered by whole-SFC review.
      } else if (['.js','.mjs'].includes(ext)) r.sections.push({name:'module',start:1,end:r.lines,semantics:script(file,text,0)});
      else if(ext==='.json') {
        const j=JSON.parse(text);r.type='json';r.jsonKeys=Object.keys(j);if(file.endsWith('/package.json')) r.manifest=j;
        if(file.endsWith('/package-lock.json')) r.lock={version:j.lockfileVersion,packageCount:Object.keys(j.packages||{}).length,root:j.packages?.['']};
        r.sections.push({name:'configuration',start:1,end:r.lines});
      } else if(path.basename(file).startsWith('.env')) {r.type='environment';r.keys=text.split('\n').map(x=>x.match(/^\s*([A-Za-z_][\w]*)\s*=/)?.[1]).filter(Boolean);r.sections.push({name:'environment',start:1,end:r.lines});}
      else {r.sections.push({name:ext==='.svg'?'asset':ext==='.scss'?'style':'document-or-config',start:1,end:r.lines});r.summary=ext==='.svg'?{svg:/<svg\b/.test(text),viewBox:text.match(/viewBox="([^"]+)"/)?.[1]}:{outline:text.split('\n').filter(x=>/^\s*(?:#|@import|@mixin|\$|server|location|FROM|RUN|COPY|EXPOSE|CMD|npm|set |call )/.test(x)).map(x=>clean(x))};}
    }
    audit[file]=r;
  }catch(e){errors.push({file,error:String(e)});}
}
fs.writeFileSync(path.join(root,'migration/state/source-audit.json'),JSON.stringify({method:'full-file parsing; semantic review is documented separately in contracts',files:audit,errors},null,2)+'\n');
fs.writeFileSync(path.join(root,'migration/state/dependency-edges.json'),JSON.stringify({edges},null,2)+'\n');
console.log(JSON.stringify({files:Object.keys(audit).length,edges:edges.length,errors,unresolved:edges.filter(e=>e.kind==='unresolved-local'),globs:edges.filter(e=>e.kind==='glob')}));
if(errors.length)process.exitCode=1;
