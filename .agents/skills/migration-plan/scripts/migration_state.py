#!/usr/bin/env python3
"""Deterministic migration inventory, coverage checks, scheduling and evidence hashes.

Python standard library only. This validates bookkeeping, not semantic equivalence.
All source access is read-only; writes are limited to the explicit state directory.
"""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import uuid
from datetime import datetime, timezone

DEFAULT_EXCLUDES = [".git", "node_modules", "dist", "coverage", ".vite"]
STATES = {"pending", "implementing", "implemented", "failed", "blocked", "passed"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(",", ":")).encode()).hexdigest()


def file_hash(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def inside(path, base):
    return path == base or base in path.parents


def relative_file(root, value):
    require(isinstance(value, str) and bool(value), "Expected a nonempty project-relative path")
    p = Path(value)
    require(not p.is_absolute() and ".." not in p.parts, "Unsafe relative path: " + value)
    resolved = (root / p).resolve()
    require(inside(resolved, root), "Path escapes project: " + value)
    return resolved


def inventory_root(config, state):
    # New inventories anchor the root to the state directory, never the CWD.
    # Absolute values are only supported while upgrading legacy metadata.
    return (state / config["project_root"]).resolve()


def inventory_digest(config):
    fields = {k: config[k] for k in ("project_root", "source_roots", "target_root", "exclude_dirs")}
    return digest({"config": fields, "files": config["files"]})


def scan(config, root):
    root = root.resolve()
    files, excluded = {}, []
    excluded_names = set(config["exclude_dirs"])

    def register(path):
        name = path.relative_to(root).as_posix()
        if path.is_symlink():
            link = os.readlink(path)
            resolved = path.resolve()
            payload = {"link": link}
            if resolved.is_file() and inside(resolved, root):
                payload["target_sha256"] = file_hash(resolved)
            files[name] = {"kind": "symlink", "link_target": link,
                           "sha256": digest(payload), "bytes": len(link.encode())}
        else:
            require(path.is_file(), "Unsupported source entry: " + name)
            files[name] = {"kind": "file", "sha256": file_hash(path),
                           "bytes": path.stat().st_size}

    def walk_error(error):
        raise error

    for source in config["source_roots"]:
        base = relative_file(root, source)
        require(base.is_dir(), "Missing source directory: " + source)
        for current, dirs, names in os.walk(base, followlinks=False, onerror=walk_error):
            directory = Path(current)
            for name in sorted(list(dirs)):
                p = directory / name
                if name in excluded_names:
                    excluded.append({"path": p.relative_to(root).as_posix(),
                                     "reason": "explicit excluded directory name: " + name})
                    dirs.remove(name)
                elif p.is_symlink():
                    register(p)
                    dirs.remove(name)
            dirs.sort()
            for name in sorted(names):
                register(directory / name)
    require(files, "Source inventory is empty; refuse an empty migration")
    # A nested source root may visit an excluded folder: explicit roots take precedence.
    return dict(sorted(files.items())), sorted(excluded, key=lambda x: x["path"])


def inventory(args, state):
    root = Path(args.root).resolve()
    state = state.resolve()
    require(root.is_dir(), "Project root does not exist")
    sources = sorted(set(str(relative_file(root, s).relative_to(root)) for s in args.source))
    target = relative_file(root, args.target)
    for s in sources:
        source = relative_file(root, s)
        require(not inside(target, source) and not inside(source, target),
                "Source and target directories must not overlap")
        require(not inside(state, source), "State directory must be outside source directories")
    excludes = args.exclude_dirs.split(",") if args.exclude_dirs else []
    require(all(x and "/" not in x and x not in {".", ".."} for x in excludes),
            "--exclude-dirs expects comma-separated directory basenames")
    config = {"project_root": Path(os.path.relpath(root, state)).as_posix(), "source_roots": sources,
              "target_root": target.relative_to(root).as_posix(), "exclude_dirs": sorted(set(excludes))}
    files, excluded = scan(config, root)
    result = {"schema_version": 1, **config, "created_at": now(), "files": files,
              "excluded": excluded, "digest": digest({"config": config, "files": files})}
    old_path = state / "inventory.json"
    if old_path.exists():
        old = read(old_path)
        comparable = dict(old, project_root=Path(os.path.relpath(root, state)).as_posix())
        require(all(comparable.get(k) == config[k] for k in config),
                "Inventory configuration changed; use a new state directory for a new scope")
        write(state / "history" / ("inventory-" + old["digest"] + ".json"), old)
    write(old_path, result)
    if not (state / "plan.json").exists():
        write(state / "plan.json", {"schema_version": 1, "inventory_digest": result["digest"],
              "files": {p: {"sha256": f["sha256"], "reviewed": False, "review_evidence": ""}
                        for p, f in files.items()}, "items": [], "groups": [],
              "integration_checks": [], "active_group": None, "active_feature": None})
    return {"status": "inventory_created", "files": len(files), "digest": result["digest"],
            "excluded": excluded, "state": Path(os.path.relpath(state, root)).as_posix(), "plan_preserved": True}


def refreshable_lock(root, path, old, live, plan):
    """Only refresh already excluded, whole-file npm locks with unchanged manifests.

    A lock refresh never certifies runtime equivalence: portable() changes the
    environment revision so every earlier passed group must be revalidated.
    """
    if (Path(path).name != "package-lock.json" or path not in old or path not in live
            or old[path]["kind"] != "file" or live[path]["kind"] != "file"):
        return False
    manifest = str(Path(path).with_name("package.json"))
    if manifest not in old or old[manifest] != live.get(manifest):
        return False
    owned = [i for i in plan.get("items", []) if i.get("source") == path]
    review = plan.get("files", {}).get(path, {})
    if (not owned or any(i.get("disposition") != "exclude" or i.get("group") or not i.get("reason") for i in owned)
            or review.get("reviewed") is not True or review.get("sha256") != old[path]["sha256"]
            or not isinstance(review.get("review_evidence"), str) or not review["review_evidence"].strip()):
        return False
    lock = read(relative_file(root, path))
    package = read(relative_file(root, manifest))
    if not isinstance(lock, dict) or not isinstance(package, dict):
        return False
    version = lock.get("lockfileVersion")
    if type(version) is not int or version not in {1, 2, 3}:
        return False
    if version == 1:
        return isinstance(lock.get("dependencies"), dict)
    packages = lock.get("packages")
    if not isinstance(packages, dict) or not isinstance(packages.get(""), dict):
        return False
    return all(packages[""].get(k, {}) == package.get(k, {})
               for k in ("dependencies", "devDependencies", "optionalDependencies", "peerDependencies"))


def portable(state, root, dry_run=False):
    """Upgrade legacy roots and reconcile excluded npm locks with an atomic journal.

    Does not write source/target files, remove inventory entries, reset progress
    or fabricate a successful validation. Existing evidence is retained.
    """
    root, state = root.resolve(), state.resolve()
    root_ref = Path(os.path.relpath(root, state)).as_posix()
    journal_path = state / "root-relocation.pending.json"
    legacy, legacy_actual = None, {}
    if journal_path.exists():
        journal = read(journal_path)
        if Path(journal["new_root"]).is_absolute():
            # An interrupted run of the previous absolute-root implementation.
            # Use its intended snapshots, but verify actual old/new values first.
            legacy = journal
            for name, update in legacy["updates"].items():
                actual = read(state / name)
                require(name in {"inventory.json", "plan.json", "round.json", "suspended-round.json"}
                        and actual in (update["old"], update["new"]),
                        "State changed during legacy portability update: " + name)
                legacy_actual[name] = actual
        else:
            require(journal["new_root"] == root_ref, "Unfinished portability update has a different state layout")
    if not journal_path.exists() or legacy:
        inv = legacy["updates"]["inventory.json"]["new"] if legacy else read(state / "inventory.json")
        plan = legacy["updates"]["plan.json"]["new"] if legacy else read(state / "plan.json")
        require(plan.get("inventory_digest") == inv["digest"], "Plan must be reconciled with the inventory digest")
        require(inventory_digest(inv) == inv["digest"], "Inventory digest does not match its contents")
        new_inv, new_plan = copy.deepcopy(inv), copy.deepcopy(plan)
        new_inv["project_root"] = root_ref
        live, _ = scan(new_inv, root)
        changed = sorted(p for p in set(live) | set(inv["files"]) if live.get(p) != inv["files"].get(p))
        rejected = [p for p in changed if not refreshable_lock(root, p, inv["files"], live, plan)]
        require(not rejected, "Source snapshot changed; 源快照变化，需重新盘点：" + ", ".join(rejected[:20]))
        if changed:
            new_inv["files"] = live
            new_inv["runtime_revision"] = digest({p: f for p, f in live.items() if Path(p).name == "package-lock.json"})
            for p in changed:
                new_plan["files"][p]["sha256"] = live[p]["sha256"]
                new_plan["files"][p]["review_evidence"] += (
                    "; 自动复核：有效 npm 锁文件、package.json 快照未变、保留既有整文件排除处置；旧运行验证须复验。")
        new_inv["digest"] = inventory_digest(new_inv)
        if new_inv == inv:
            return None
        new_plan["inventory_digest"] = new_inv["digest"]
        updates = {"inventory.json": {"old": legacy_actual.get("inventory.json", inv), "new": new_inv},
                   "plan.json": {"old": legacy_actual.get("plan.json", plan), "new": new_plan}}
        for name in ("round.json", "suspended-round.json"):
            if (state / name).exists():
                actual = legacy_actual[name] if name in legacy_actual else read(state / name)
                task = legacy["updates"][name]["new"] if legacy and name in legacy["updates"] else actual
                if task.get("inventory_digest") == inv["digest"]:
                    updates[name] = {"old": actual, "new": dict(task, inventory_digest=new_inv["digest"])}
        journal = {"new_root": root_ref, "at": now(), "changed_locks": changed,
                   "history": "portability-" + uuid.uuid4().hex + ".json", "updates": updates}
    new_inv = journal["updates"]["inventory.json"]["new"]
    require(inventory_root(new_inv, state) == root, "Portable inventory points outside the current project")
    live, _ = scan(new_inv, root)
    require(live == new_inv["files"], "Source changed during portability update; retry after reviewing the source")
    allowed = {"inventory.json", "plan.json", "round.json", "suspended-round.json"}
    for name, update in journal["updates"].items():
        require(name in allowed and read(state / name) in (update["old"], update["new"]),
                "State changed during portability update: " + name)
    summary = {"project_root": root_ref, "source_files": len(live), "refreshed_excluded_locks": journal["changed_locks"],
               "progress_preserved": True, "runtime_revalidation_required": bool(journal["changed_locks"])}
    if dry_run:
        return summary
    if not journal_path.exists() or legacy:
        write(journal_path, journal)
    write(state / "history" / journal["history"], journal)
    for name, update in journal["updates"].items():
        write(state / name, update["new"])
    journal_path.unlink()
    return summary


def keyed(rows, kind):
    require(isinstance(rows, list), kind + " must be a list")
    result = {}
    for row in rows:
        require(isinstance(row, dict), kind + " entries must be objects")
        key = row.get("id")
        require(isinstance(key, str) and re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", key),
                "Invalid stable ID in " + kind)
        require(key not in result, "Duplicate " + kind + " ID: " + key)
        result[key] = row
    return result


def topology(groups):
    remaining = set(groups)
    order = []
    while remaining:
        ready = sorted(g for g in remaining if not (set(groups[g]["depends_on"]) & remaining))
        require(ready, "Dependency cycle among: " + ", ".join(sorted(remaining)))
        order.extend(ready)
        remaining.difference_update(ready)
    return order


def load_checked(state):
    inv, plan = read(state / "inventory.json"), read(state / "plan.json")
    require(inv.get("schema_version") == plan.get("schema_version") == 1, "Unsupported schema version")
    root = inventory_root(inv, state)
    live, _ = scan(inv, root)
    old = inv["files"]
    changed = sorted(p for p in set(live) | set(old) if live.get(p) != old.get(p))
    require(not changed, "Source snapshot changed; rerun inventory and review: " + ", ".join(changed[:20]))
    require(plan.get("inventory_digest") == inv["digest"], "Plan must be reconciled with the new inventory digest")
    require(isinstance(plan.get("files"), dict) and set(plan["files"]) == set(old),
            "Plan files must exactly cover inventory (including hidden and unreferenced files)")
    groups = keyed(plan.get("groups"), "groups")
    items = keyed(plan.get("items"), "items")
    checks = keyed(plan.get("integration_checks"), "integration_checks")
    require(groups, "No migration groups planned")
    require(checks, "Plan at least one integration/final runtime check")
    covered = set()
    for item in items.values():
        source = item.get("source")
        require(source in old, "Item has unknown source: " + str(source))
        covered.add(source)
        for field in ("locator", "basis"):
            require(isinstance(item.get(field), str) and item[field].strip(), item["id"] + " missing " + field)
        disposition = item.get("disposition")
        require(disposition in {"migrate", "reuse", "exclude"}, "Invalid disposition: " + item["id"])
        if disposition == "exclude":
            require(isinstance(item.get("reason"), str) and item["reason"].strip(), "Exclusion needs reason: " + item["id"])
            require(not item.get("group"), "Excluded item must not own a group")
        else:
            require(item.get("group") in groups, "Missing group for " + item["id"])
            if old[source]["kind"] == "symlink":
                resolved = (root / source).resolve()
                require(resolved.exists(), "Unresolved source symlink: " + source)
                require(inside(resolved, root), "External symlink needs an explicit audited disposition: " + source)
                if resolved.is_dir():
                    require(any(inside(resolved, relative_file(root, s)) for s in inv["source_roots"])
                            and any(inside(root / p, resolved) for p in old if p != source),
                            "Directory symlink target is not inventoried; add an explicit --source: " + source)
        require(isinstance(item.get("targets", []), list), "Item targets must be a list")
        for p in item.get("targets", []):
            require(inside(relative_file(root, p), relative_file(root, inv["target_root"])), "Target outside React directory: " + p)
    require(covered == set(old), "Files have no content items: " + ", ".join(sorted(set(old) - covered)[:20]))
    for p, review in plan["files"].items():
        require(isinstance(review, dict) and review.get("reviewed") is True,
                "Source file has not been fully reviewed: " + p)
        require(review.get("sha256") == old[p]["sha256"], "Stale source review: " + p)
        require(isinstance(review.get("review_evidence"), str) and review["review_evidence"].strip(),
                "Missing source review evidence: " + p)
    for gid, group in groups.items():
        for field in ("title", "feature", "contract"):
            require(isinstance(group.get(field), str) and group[field].strip(), gid + " missing " + field)
        require(type(group.get("entry_priority")) is int and group["entry_priority"] in (0, 1, 2), "Invalid entry_priority: " + gid)
        deps = group.get("depends_on")
        require(isinstance(deps, list) and len(deps) == len(set(deps)) and
                all(d in groups and d != gid for d in deps), "Invalid dependencies: " + gid)
        require(group.get("status") in STATES, "Invalid group status: " + gid)
        contract = relative_file(root, group["contract"])
        require(contract.is_file() and contract.stat().st_size, "Missing/empty group contract: " + gid)
        owned = [i for i in items.values() if i.get("group") == gid]
        require(owned or group["entry_priority"] == 0, "Non-foundation group has no source items: " + gid)
        for p in group.get("targets", []):
            require(inside(relative_file(root, p), relative_file(root, inv["target_root"])), "Group target outside React directory: " + p)
    order = topology(groups)
    for cid, check in checks.items():
        require(check.get("status") in STATES, "Invalid integration status: " + cid)
        require(isinstance(check.get("groups"), list) and check["groups"] and
                len(check["groups"]) == len(set(check["groups"])) and all(g in groups for g in check["groups"]),
                "Invalid integration group scope: " + cid)
        require(isinstance(check.get("contract"), str) and relative_file(root, check["contract"]).is_file()
                and relative_file(root, check["contract"]).stat().st_size,
                "Missing integration contract: " + cid)
    require(set(groups) <= {g for c in checks.values() for g in c["groups"]},
            "Integration checks must account for every group; pure utilities can be covered by a minimal wiring check")
    require(plan.get("active_group") is None or plan["active_group"] in groups, "Invalid active_group")
    return inv, plan, root, groups, items, checks, order


def group_snapshot(root, inv, groups, items, gid):
    group = groups[gid]
    own = sorted((i for i in items.values() if i.get("group") == gid), key=lambda x: x["id"])
    targets = sorted(set(group.get("targets", []) + [p for i in own for p in i.get("targets", [])]))
    require(targets, "No target paths for " + gid)
    require(all(i.get("targets") for i in own), "Content item has no target in " + gid)
    require(all(isinstance(i.get("target_locator"), str) and i["target_locator"].strip() for i in own),
            "Content item has no target function/component/resource locator in " + gid)
    hashes = {}
    for p in targets:
        target = relative_file(root, p)
        require(target.is_file(), "Missing target file: " + p)
        hashes[p] = file_hash(target)
    snapshot = {"source": {i["source"]: inv["files"][i["source"]]["sha256"] for i in own},
                   "items": own, "targets": hashes, "contract": file_hash(relative_file(root, group["contract"])),
                   "depends_on": {d: groups[d].get("validation") for d in group["depends_on"]}}
    if inv.get("runtime_revision"):
        snapshot["source_environment"] = inv["runtime_revision"]
    return digest(snapshot)


def evidence_valid(root, validation):
    if not isinstance(validation, dict) or not validation.get("artifacts"):
        return False
    try:
        return all(relative_file(root, a["path"]).is_file() and
                   file_hash(relative_file(root, a["path"])) == a["sha256"]
                   for a in validation["artifacts"])
    except (ValueError, KeyError, OSError):
        return False


def scope_digest(group, items):
    return digest({"items": sorted(
        [{k: v for k, v in i.items() if k not in {"targets", "target_locator"}}
         for i in items.values() if i.get("group") == group["id"]], key=lambda x: x["id"]),
        "depends_on": group["depends_on"]})


def effective_groups(root, inv, groups, items, order):
    passed, invalid = set(), []
    for gid in order:
        g = groups[gid]
        if g["status"] != "passed":
            continue
        try:
            good = (set(g["depends_on"]) <= passed and evidence_valid(root, g.get("validation")) and
                    group_snapshot(root, inv, groups, items, gid) == g.get("validation", {}).get("snapshot"))
        except (ValueError, OSError):
            good = False
        if good:
            passed.add(gid)
        else:
            invalid.append(gid)
    return passed, invalid


def integration_snapshot(root, groups, check):
    return digest({"groups": {g: groups[g].get("validation") for g in check["groups"]},
                   "contract": file_hash(relative_file(root, check["contract"]))})


def effective_checks(root, groups, checks, passed):
    good = set()
    for cid, c in checks.items():
        if (c["status"] == "passed" and set(c["groups"]) <= passed and
                evidence_valid(root, c.get("validation")) and
                integration_snapshot(root, groups, c) == c.get("validation", {}).get("snapshot")):
            good.add(cid)
    return good


def check_state(state, final=False):
    inv, plan, root, groups, items, checks, order = load_checked(state)
    passed, invalid = effective_groups(root, inv, groups, items, order)
    integrated = effective_checks(root, groups, checks, passed)
    complete = len(passed) == len(groups) and len(integrated) == len(checks)
    result = {"status": "complete" if complete else "plan_valid", "files": len(inv["files"]),
              "items": len(items), "groups": len(groups), "groups_passed": len(passed),
              "invalidated_groups": invalid, "integration_passed": len(integrated),
              "integration_total": len(checks), "semantic_equivalence_proven_by_script": False}
    if final:
        require(complete, "Final check incomplete: " + json.dumps(result, ensure_ascii=False))
    return result


def select(state, claim):
    inv, plan, root, groups, items, checks, order = load_checked(state)
    passed, invalid = effective_groups(root, inv, groups, items, order)
    active = plan.get("active_group")
    repair = [g for g in invalid if set(groups[g]["depends_on"]) <= passed]
    if repair:
        chosen, mode = repair[0], "revalidate"
        if claim and active and active != chosen and active not in passed and not plan.get("resume_after_validation"):
            plan["resume_after_validation"] = active
            if (state / "round.json").exists():
                write(state / "suspended-round.json", read(state / "round.json"))
    elif active and active not in passed and groups[active]["status"] != "blocked":
        chosen, mode = active, "resume"
        require(set(groups[active]["depends_on"]) <= passed, "Active group dependency no longer valid")
    else:
        suspended = plan.get("resume_after_validation")
        if suspended in groups and suspended not in passed and groups[suspended]["status"] != "blocked" and set(groups[suspended]["depends_on"]) <= passed:
            if claim:
                plan["active_group"] = suspended
                plan.pop("resume_after_validation", None)
                # Save then use the ordinary resume path, including the restored round.
                write(state / "plan.json", plan)
                suspended_round = state / "suspended-round.json"
                if suspended_round.exists():
                    old_round = read(suspended_round)
                    require(old_round.get("group") == suspended, "Suspended round does not match saved group")
                    write(state / "round.json", old_round)
                    suspended_round.unlink()
                return select(state, claim)
            return {"status": "selected", "mode": "resume", "group": suspended,
                    "contract": groups[suspended]["contract"], "reason": "resume after dependency revalidation"}
        candidates = [g for g in groups if g not in passed and groups[g]["status"] != "blocked"
                      and set(groups[g]["depends_on"]) <= passed]
        if not candidates:
            if len(passed) == len(groups):
                integrated = effective_checks(root, groups, checks, passed)
                return {"status": "complete" if len(integrated) == len(checks) else "groups_complete",
                        "remaining_integration": sorted(set(checks) - integrated)}
            return {"status": "blocked", "remaining": {g: {"status": groups[g]["status"],
                    "note": groups[g].get("note"), "waiting_for": sorted(set(groups[g]["depends_on"]) - passed)}
                    for g in groups if g not in passed}}
        downstream = {g: set() for g in groups}
        for g in reversed(order):
            for dep in groups[g]["depends_on"]:
                downstream[dep].add(g)
                downstream[dep].update(downstream[g])
        current = plan.get("active_feature")

        def rank(g):
            affected = {g} | downstream[g]
            continuation = bool(current and current != "shared" and
                                any(groups[x]["feature"] == current for x in affected - passed))
            priority = min(groups[x]["entry_priority"] for x in affected - passed)
            size = sum(i.get("group") == g for i in items.values())
            return (0 if continuation else 1, priority, -len(downstream[g] - passed), size, g)

        chosen, mode = min(candidates, key=rank), "new"
    group = groups[chosen]
    contract = relative_file(root, group["contract"])
    result = {"status": "selected", "mode": mode, "group": chosen, "title": group["title"],
              "feature": group["feature"], "group_status": group["status"], "contract": group["contract"],
              "contract_sha256": file_hash(contract), "inventory_digest": inv["digest"],
              "items": [i["id"] for i in items.values() if i.get("group") == chosen],
              "depends_on": group["depends_on"], "selected_at": now(),
              "reason": "resume active group" if mode == "resume" else "validation hashes changed; revalidate in dependency order" if mode == "revalidate" else
              "ready dependencies; current feature; entry priority; downstream count; item count; stable ID"}
    result["scope_digest"] = scope_digest(group, items)
    if claim:
        round_path = state / "round.json"
        if mode == "resume" and round_path.exists():
            previous = read(round_path)
            require(previous.get("group") == chosen and previous.get("contract_sha256") == result["contract_sha256"]
                    and previous.get("inventory_digest") == inv["digest"]
                    and previous.get("scope_digest") == result["scope_digest"],
                    "Active round contract/snapshot changed; reconcile plan and explicitly close the old round first")
        else:
            if round_path.exists():
                previous = read(round_path)
                write(state / "history" / ("round-" + digest(previous) + ".json"), previous)
            write(round_path, result)
        plan["active_group"] = chosen
        if mode != "revalidate" and group["feature"] != "shared":
            plan["active_feature"] = group["feature"]
        if group["status"] == "pending":
            group["status"] = "implementing"
        write(state / "plan.json", plan)
    return result


def record(args, state):
    inv, plan, root, groups, items, checks, order = load_checked(state)
    passed, _ = effective_groups(root, inv, groups, items, order)
    key = args.group or args.integration
    rows = groups if args.group else checks
    require(key in rows, "Unknown validation ID: " + key)
    row = rows[key]
    required = row["depends_on"] if args.group else row["groups"]
    if args.result == "passed":
        require(set(required) <= passed, "Required group validation is not effective")
        require(any(p != args.report for p in args.evidence), "Passed record requires distinct evidence in addition to a report")
        require(not args.group or plan.get("active_group") in (None, key), "Another group is active")
        if args.group and plan.get("active_group") == key:
            selected = read(state / "round.json")
            require(selected.get("group") == key and selected.get("inventory_digest") == inv["digest"]
                    and selected.get("contract_sha256") == file_hash(relative_file(root, row["contract"]))
                    and selected.get("scope_digest") == scope_digest(row, items),
                    "Selected round scope changed; reconcile and select it again before passing")
    else:
        require(args.note, "Failure/block requires --note with diagnosis and recovery condition")
    artifacts = []
    for name in sorted(set([args.report] + args.evidence)):
        p = relative_file(root, name)
        require(p.is_file() and p.stat().st_size, "Missing/empty evidence or report: " + name)
        artifacts.append({"path": name, "sha256": file_hash(p)})
    validation = {"result": args.result, "recorded_at": now(), "report": args.report,
                  "artifacts": artifacts, "note": args.note}
    if args.result == "passed":
        validation["snapshot"] = (group_snapshot(root, inv, groups, items, key) if args.group
                                  else integration_snapshot(root, groups, row))
    previous = row.get("validation")
    if previous:
        write(state / "history" / (key + "-" + digest(previous) + ".json"), previous)
    row["validation"] = validation
    row["status"] = args.result
    row["note"] = args.note
    if args.group and plan.get("active_group") == key and args.result in {"passed", "blocked"}:
        plan["active_group"] = None
    if args.group and plan.get("resume_after_validation") == key and args.result == "passed":
        plan.pop("resume_after_validation", None)
    write(state / "plan.json", plan)
    return {"status": "recorded", "id": key, "result": args.result,
            "scope": "group" if args.group else "integration"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("inventory")
    p.add_argument("--root", default=".")
    p.add_argument("--source", action="append", required=True)
    p.add_argument("--target", required=True)
    p.add_argument("--exclude-dirs", default=",".join(DEFAULT_EXCLUDES))
    p = commands.add_parser("portable")
    p.add_argument("--root", default=".")
    p.add_argument("--dry-run", action="store_true")
    for name in ("check", "next", "record"):
        commands.add_parser(name)
    for p in commands.choices.values():
        p.add_argument("--state", default="migration/state")
    commands.choices["check"].add_argument("--final", action="store_true")
    commands.choices["next"].add_argument("--claim", action="store_true")
    p = commands.choices["record"]
    which = p.add_mutually_exclusive_group(required=True)
    which.add_argument("--group")
    which.add_argument("--integration")
    p.add_argument("--result", choices=["passed", "failed", "blocked"], required=True)
    p.add_argument("--report", required=True)
    p.add_argument("--evidence", action="append", default=[])
    p.add_argument("--note", default="")
    args = parser.parse_args()
    state = Path(args.state).resolve()
    try:
        if args.command == "inventory":
            result = inventory(args, state)
        elif args.command == "portable":
            result = portable(state, Path(args.root), args.dry_run) or {"status": "already_portable"}
        elif args.command == "check":
            result = check_state(state, args.final)
        elif args.command == "next":
            result = select(state, args.claim)
        else:
            result = record(args, state)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(json.dumps({"status": "needs_attention", "error": str(error)}, ensure_ascii=False, indent=2))
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
