// Read-only full-file structural audit. Uses the source project's installed parsers.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const root = process.cwd();
const parser = require(require.resolve('@babel/parser', { paths: [path.join(root, 'ruoyi-fastapi-frontend')] }));
const vue = require(require.resolve('@vue/compiler-sfc', { paths: [path.join(root, 'ruoyi-fastapi-frontend')] }));
const inventory = JSON.parse(fs.readFileSync('migration/state/inventory.json', 'utf8'));
function visit(node, fn) {
  if (!node || typeof node !== 'object') return;
  if (Array.isArray(node)) { node.forEach(x => visit(x, fn)); return; }
  if (node.type) fn(node);
  for (const [k, v] of Object.entries(node)) if (!['loc', 'comments', 'tokens', 'errors', 'extra'].includes(k)) visit(v, fn);
}
function name(n) {
  if (!n) return '';
  if (n.type === 'Identifier') return n.name;
  if (n.type === 'StringLiteral') return n.value;
  if (n.type === 'MemberExpression' || n.type === 'OptionalMemberExpression') return name(n.object) + '.' + name(n.property);
  return n.type;
}
function parseJS(text, offset = 0) {
  const ast = parser.parse(text, { sourceType: 'unambiguous', plugins: ['jsx', 'typescript'], errorRecovery: false });
  const imports = new Set(), globals = new Set(), importEdges = [];
  function declarationNames(n) {
    if (!n) return [];
    if (n.type === 'ExportNamedDeclaration' || n.type === 'ExportDefaultDeclaration') return declarationNames(n.declaration);
    if (n.type === 'VariableDeclaration') return n.declarations.flatMap(d => d.id.type === 'Identifier' ? [d.id.name] : []);
    return n.id?.name ? [n.id.name] : [];
  }
  const statements = ast.program.body.map((statement, index) => {
    const funcs = [], calls = new Set(), bindings = new Set(), branches = [];
    visit(statement, n => {
      if (/Function|Method/.test(n.type)) funcs.push({ name: name(n.id || n.key) || 'callback', line: n.loc.start.line + offset, end: n.loc.end.line + offset });
      if (n.type === 'VariableDeclarator') bindings.add(name(n.id));
      if (n.type === 'Identifier') globals.add(n.name);
      if (n.type === 'ImportDeclaration' || /Export(All|Named)Declaration/.test(n.type) && n.source) {
        imports.add(n.source.value);
        importEdges.push({ source: n.source.value, kind: 'static', names: (n.specifiers || []).map(s => s.imported?.name || (s.type === 'ImportDefaultSpecifier' ? 'default' : '*')) });
      }
      if (n.type === 'CallExpression' || n.type === 'OptionalCallExpression') {
        calls.add(name(n.callee));
        if ((n.callee.type === 'Import' || name(n.callee) === 'require') && n.arguments[0]?.type === 'StringLiteral') { imports.add(n.arguments[0].value); importEdges.push({ source: n.arguments[0].value, kind: 'runtime', names: ['*'] }); }
      }
      if (/^(IfStatement|ConditionalExpression|SwitchCase|CatchClause|ThrowStatement|ReturnStatement|LogicalExpression)$/.test(n.type)) branches.push({ kind: n.type, line: n.loc.start.line + offset });
    });
    return { names: declarationNames(statement), kind: statement.type, line: statement.loc.start.line + offset, end: statement.loc.end.line + offset,
      bindings: [...bindings], functions: funcs, calls: [...calls], branches,
      sha256: crypto.createHash('sha256').update(text.slice(statement.start, statement.end)).digest('hex') };
  });
  return { imports: [...imports], import_edges: importEdges, identifiers: [...globals], statements };
}
const output = {};
for (const [file, metadata] of Object.entries(inventory.files)) {
  const buffer = fs.readFileSync(file), ext = path.extname(file);
  const result = { path: file, sha256: metadata.sha256, bytes: buffer.length, kind: ext || 'text' };
  if (['.png', '.jpg', '.gif', '.ico'].includes(ext)) {
    result.asset_signature = buffer.subarray(0, 12).toString('hex');
  } else {
    const text = buffer.toString('utf8');
    result.lines = text.split('\n').length;
    if (ext === '.vue') {
      const parsed = vue.parse(text, { filename: file });
      if (parsed.errors.length) throw new Error(file + ': ' + parsed.errors.map(String).join(';'));
      const d = parsed.descriptor;
      result.scripts = [d.script, d.scriptSetup].filter(Boolean).map(s => parseJS(s.content, s.loc.start.line - 1));
      result.template = null;
      if (d.template) {
        const tags = {}, bindings = [], literals = [];
        // The SFC parser produces the full template AST, including nested expressions.
        visit(d.template.ast, n => {
          if (typeof n.tag === 'string') tags[n.tag] = (tags[n.tag] || 0) + 1;
          if (n.type === 7) bindings.push({ name: n.name, arg: n.arg?.content || '', expression: n.exp?.content || '', line: n.loc.start.line });
          if (n.type === 5) literals.push({ expression: n.content?.content, line: n.loc.start.line });
        });
        result.template = { line: d.template.loc.start.line, end: d.template.loc.end.line, tags, bindings, interpolations: literals };
      }
      result.styles = d.styles.map(s => ({ line: s.loc.start.line, end: s.loc.end.line, scoped: s.scoped || false,
        lang: s.lang || 'css', selectors: [...s.content.matchAll(/([^{}]+)\{/g)].map(x => x[1].trim()),
        urls: [...s.content.matchAll(/url\(['"]?([^)'"\s]+)['"]?\)/g)].map(x => x[1]) }));
    } else if (ext === '.js') result.javascript = parseJS(text);
    else if (ext === '.json') {
      const json = JSON.parse(text);
      result.json_keys = Object.keys(json);
      if (file.endsWith('/package.json')) result.package = json;
      else result.entries = Array.isArray(json) ? json.length : Object.keys(json).length;
    } else if (path.basename(file).startsWith('.env.')) {
      result.environment_keys = text.split('\n').filter(x => x.includes('=') && !x.trimStart().startsWith('#')).map(x => x.split('=')[0].trim());
    } else if (ext === '.svg') {
      result.svg = { root: /<svg\b/.test(text), elements: [...new Set([...text.matchAll(/<([\w:-]+)/g)].map(x => x[1]))], viewBox: text.match(/viewBox="([^"]+)"/)?.[1] || null };
    } else {
      result.headings = [...text.matchAll(/^#+\s+(.+)$/gm)].map(x => x[1]);
      result.selectors = ext === '.scss' ? [...text.matchAll(/([^{}]+)\{/g)].map(x => x[1].trim()) : [];
      result.urls = [...text.matchAll(/(?:url\(['"]?|(?:src|href)=["'])([^)'"\s>]+)/g)].map(x => x[1]);
      result.sha256_full_read = crypto.createHash('sha256').update(buffer).digest('hex');
    }
  }
  output[file] = result;
}
fs.writeFileSync('migration/state/source-audit.json', JSON.stringify(output, null, 2) + '\n');
let statements = 0, functions = 0, branches = 0, bindings = 0;
for (const r of Object.values(output)) {
  for (const js of [...(r.scripts || []), ...(r.javascript ? [r.javascript] : [])]) {
    statements += js.statements.length;
    for (const s of js.statements) { functions += s.functions.length; branches += s.branches.length; }
  }
  bindings += (r.template?.bindings.length || 0) + (r.template?.interpolations.length || 0);
}
console.log(JSON.stringify({ files: Object.keys(output).length, statements, functions, branches, template_bindings: bindings }));
