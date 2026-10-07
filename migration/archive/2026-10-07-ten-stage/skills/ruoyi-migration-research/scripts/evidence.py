#!/usr/bin/env python3
"""Create/check deterministic SHA-256 evidence manifests; never infer acceptance."""

import argparse
import hashlib
import json
import sys
from pathlib import Path

IGNORED_DIRS = {
    ".git", "node_modules", "dist", "build", "coverage", ".cache", ".vite",
    "playwright-report", "test-results", "__pycache__", ".venv",
}


def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def local_path(root, name):
    candidate = Path(name)
    if candidate.is_absolute() or ".." in candidate.parts or not candidate.parts:
        raise ValueError(f"Expected project-relative path: {name}")
    path = root / candidate
    path.resolve().relative_to(root)
    # Symlinks hide dependencies and may point outside the project; require an explicit real file.
    if any((root / Path(*candidate.parts[:i])).is_symlink()
           for i in range(1, len(candidate.parts) + 1)):
        raise ValueError(f"Evidence must not traverse symlinks: {name}")
    return path


def ignored(path):
    return (any(part in IGNORED_DIRS for part in path.parts)
            or path.name == ".DS_Store"
            or (path.name.startswith(".env") and not path.name.endswith((".example", ".sample"))))


def tree_files(root, name):
    tree = local_path(root, name)
    if not tree.is_dir():
        raise ValueError(f"Missing code tree: {name}")
    found = []
    # Prune ignored directories rather than reading dependency/build trees.
    def visit(folder):
        for path in sorted(folder.iterdir()):
            relative = path.relative_to(root)
            if ignored(relative):
                continue
            if path.is_symlink():
                raise ValueError(f"Symlink in evidence tree: {relative}")
            if path.is_dir():
                visit(path)
            elif path.is_file():
                found.append(relative.as_posix())
    visit(tree)
    return found


def fingerprint(files):
    encoded = json.dumps(files, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def snapshot(args):
    root = Path(args.root).resolve(strict=True)
    if args.tree:
        names = tree_files(root, args.tree)
    else:
        names = json.loads(Path(args.files).read_text(encoding="utf-8"))
        if not isinstance(names, list) or not all(isinstance(n, str) for n in names):
            raise ValueError("--files must contain a JSON array of relative file paths")
        names = sorted(set(names))
    if not names:
        raise ValueError("Empty evidence set; no runnable target or researched source files")
    files = {}
    for name in names:
        path = local_path(root, name)
        if ignored(Path(name)):
            raise ValueError(f"Secret/generated/dependency file is excluded: {name}")
        files[Path(name).as_posix()] = digest(path)
    result = {
        "schema_version": 1,
        "mode": "tree" if args.tree else "files",
        "files": files,
        "fingerprint": fingerprint(files),
    }
    if args.tree:
        result["tree"] = Path(args.tree).as_posix()
    output = Path(args.output)
    if any(output.resolve() == local_path(root, name).resolve() for name in names):
        raise ValueError("Manifest output cannot replace an evidence file")
    if args.tree and output.resolve().is_relative_to(local_path(root, args.tree).resolve()):
        raise ValueError("Store manifest outside its tracked tree")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"status": "recorded", "file_count": len(files), "fingerprint": result["fingerprint"]}


def check(args):
    root = Path(args.root).resolve(strict=True)
    saved = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    files = saved.get("files")
    if saved.get("schema_version") != 1 or saved.get("mode") not in ("files", "tree"):
        raise ValueError("Unsupported manifest format")
    if not isinstance(files, dict) or not files or not all(
            isinstance(name, str) and isinstance(value, str) and len(value) == 64
            and all(c in "0123456789abcdef" for c in value) for name, value in files.items()):
        raise ValueError("Malformed or empty evidence map")
    if saved.get("fingerprint") != fingerprint(files):
        raise ValueError("Manifest fingerprint does not match its evidence map")
    missing, changed = [], []
    for name, expected in files.items():
        path = local_path(root, name)
        if not path.is_file():
            missing.append(name)
        elif digest(path) != expected:
            changed.append(name)
    added = []
    if saved["mode"] == "tree":
        added = sorted(set(tree_files(root, saved["tree"])) - set(files))
    status = "stale" if missing or changed or added else "unchanged"
    return {"status": status, "missing": missing, "changed": changed, "added": added}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("snapshot")
    create.add_argument("--root", required=True)
    inputs = create.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--files")
    inputs.add_argument("--tree")
    create.add_argument("--output", required=True)
    verify = commands.add_parser("check")
    verify.add_argument("--root", required=True)
    verify.add_argument("--manifest", required=True)
    hashing = commands.add_parser("hash")
    hashing.add_argument("paths", nargs="+")
    args = parser.parse_args()
    try:
        if args.command == "snapshot":
            result = snapshot(args)
        elif args.command == "check":
            result = check(args)
        else:
            result = {name: digest(Path(name)) for name in args.paths}
        print(json.dumps(result, ensure_ascii=False))
        return 1 if result.get("status") == "stale" else 0
    except (OSError, ValueError, KeyError, TypeError, RecursionError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
