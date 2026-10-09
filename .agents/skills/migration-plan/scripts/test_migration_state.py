"""Regression tests for inventory completeness, dependency ordering and stale evidence.

All fixtures live in temporary directories; this never migrates the actual project.
"""
import argparse
import importlib.util
from pathlib import Path
import tempfile
import unittest
import subprocess
import sys
import json

spec = importlib.util.spec_from_file_location("migration_state", Path(__file__).with_name("migration_state.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class MigrationStateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.state = self.root / "migration/state"
        for name in ("a.js", "b.vue", "c.vue"):
            self.put("vue/" + name, "old behavior: " + name)
        self.args = argparse.Namespace(root=str(self.root), source=["vue"], target="react",
                                       exclude_dirs=",".join(m.DEFAULT_EXCLUDES))
        m.inventory(self.args, self.state)
        inv = m.read(self.state / "inventory.json")
        plan = m.read(self.state / "plan.json")
        for path, review in plan["files"].items():
            review.update(reviewed=True, review_evidence="Read all content in " + path)
        names = ["vue/a.js", "vue/b.vue", "vue/c.vue"]
        plan["items"] = [{"id": "I" + str(n), "source": p, "locator": "export/template",
                          "basis": "old behavior", "disposition": "migrate", "group": "G" + str(n),
                          "target_locator": "translated function/component",
                          "targets": ["react/" + str(n) + ".tsx"]} for n, p in enumerate(names, 1)]
        plan["groups"] = []
        for n in range(1, 4):
            self.put("migration/state/groups/G" + str(n) + "/contract.md", "old inputs and expected results")
            plan["groups"].append({"id": "G" + str(n), "title": "Group " + str(n),
                                   "feature": ["shared", "login", "users"][n - 1],
                                   "entry_priority": 1 if n == 2 else 2,
                                   "depends_on": [] if n == 1 else ["G1"],
                                   "contract": "migration/state/groups/G" + str(n) + "/contract.md",
                                   "status": "pending", "targets": []})
        self.put("migration/state/integration/J1-contract.md", "main navigation and wiring")
        plan["integration_checks"] = [{"id": "J1", "groups": ["G1", "G2", "G3"],
                                        "contract": "migration/state/integration/J1-contract.md", "status": "pending"}]
        plan["inventory_digest"] = inv["digest"]
        m.write(self.state / "plan.json", plan)

    def put(self, relative, text):
        p = self.root / relative
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        return p

    def edit(self, fn):
        plan = m.read(self.state / "plan.json")
        fn(plan)
        m.write(self.state / "plan.json", plan)

    def record(self, key, result="passed", integration=False):
        self.put("migration/state/evidence/" + key + ".log", "command executed; assertions passed")
        self.put("migration/state/reports/" + key + ".md", "actual test results and limitations")
        args = argparse.Namespace(group=None if integration else key,
                                  integration=key if integration else None, result=result,
                                  report="migration/state/reports/" + key + ".md",
                                  evidence=["migration/state/evidence/" + key + ".log"],
                                  note="environment unavailable; retry when restored" if result != "passed" else "")
        return m.record(args, self.state)

    def pass_group(self, key):
        n = key[1:]
        self.put("react/" + n + ".tsx", "translated behavior: " + key)
        self.record(key)

    def test_inventory_root_is_relative_and_resolves_without_cwd(self):
        inv=m.read(self.state/'inventory.json')
        self.assertEqual(inv['project_root'],'../..')
        self.assertNotIn(str(self.root), (self.state/'inventory.json').read_text())
        self.assertEqual(m.inventory_root(inv,self.state),self.root.resolve())
        result=subprocess.run([sys.executable,str(Path(m.__file__).resolve()),'check','--state',str(self.state)],cwd=self.root.parent,capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stdout)

    def test_custom_nested_state_uses_its_own_relative_anchor(self):
        custom=self.root/'tracking/deep/state'
        m.inventory(self.args,custom)
        inv=m.read(custom/'inventory.json')
        self.assertEqual(inv['project_root'],'../../..')
        self.assertEqual(m.inventory_root(inv,custom),self.root.resolve())
        plan=m.read(self.state/'plan.json');plan['inventory_digest']=inv['digest'];m.write(custom/'plan.json',plan)
        self.assertEqual(m.check_state(custom)['files'],3)

    def test_hidden_and_gitignored_files_are_listed(self):
        self.put("vue/.gitignore", "secret.js\n")
        self.put("vue/secret.js", "still source")
        self.put("vue/.hidden/data.txt", "hidden source")
        self.put("vue/node_modules/pkg/index.js", "dependency")
        m.inventory(self.args, self.state)
        files = m.read(self.state / "inventory.json")["files"]
        self.assertIn("vue/secret.js", files)
        self.assertIn("vue/.hidden/data.txt", files)
        self.assertIn("vue/.gitignore", files)
        self.assertNotIn("vue/node_modules/pkg/index.js", files)

    def test_snapshot_preserves_plan_and_detects_new_source(self):
        before = (self.state / "plan.json").read_text()
        self.put("vue/new.js", "new behavior")
        with self.assertRaisesRegex(ValueError, "snapshot changed"):
            m.select(self.state, False)
        m.inventory(self.args, self.state)
        self.assertEqual(before, (self.state / "plan.json").read_text())
        with self.assertRaisesRegex(ValueError, "reconciled"):
            m.check_state(self.state)

    def test_modified_and_deleted_source_detected(self):
        self.put("vue/a.js", "changed behavior")
        with self.assertRaisesRegex(ValueError, "snapshot changed"):
            m.check_state(self.state)
        (self.root / "vue/b.vue").unlink()
        with self.assertRaisesRegex(ValueError, "snapshot changed"):
            m.check_state(self.state)

    def test_empty_source_and_overlapping_target_rejected(self):
        args = argparse.Namespace(**vars(self.args))
        args.target = "vue/react"
        with self.assertRaisesRegex(ValueError, "overlap"):
            m.inventory(args, self.root / "other-state")
        (self.root / "empty").mkdir()
        args.source, args.target = ["empty"], "react"
        with self.assertRaisesRegex(ValueError, "empty"):
            m.inventory(args, self.root / "other-state")

    def test_missing_file_review_and_item_fail(self):
        self.edit(lambda p: p["files"]["vue/a.js"].update(reviewed=False))
        with self.assertRaisesRegex(ValueError, "not been fully reviewed"):
            m.select(self.state, False)
        self.edit(lambda p: p["files"]["vue/a.js"].update(reviewed=True))
        self.edit(lambda p: p["items"].pop())
        with self.assertRaisesRegex(ValueError, "no content items"):
            m.select(self.state, False)

    def test_cycle_and_unknown_dependency_rejected(self):
        self.edit(lambda p: p["groups"][0].update(depends_on=["G2"]))
        with self.assertRaisesRegex(ValueError, "cycle"):
            m.select(self.state, False)
        self.edit(lambda p: p["groups"][0].update(depends_on=["unknown"]))
        with self.assertRaisesRegex(ValueError, "Invalid dependencies"):
            m.select(self.state, False)

    def test_source_target_mapping_cannot_escape(self):
        self.edit(lambda p: p["items"][0].update(targets=["../outside.js"]))
        with self.assertRaisesRegex(ValueError, "Unsafe relative path"):
            m.check_state(self.state)
        self.edit(lambda p: p["items"][0].update(targets=["vue/a.js"]))
        with self.assertRaisesRegex(ValueError, "outside React"):
            m.check_state(self.state)

    def test_dependency_then_main_entry_and_resume(self):
        self.assertEqual(m.select(self.state, True)["group"], "G1")
        self.assertEqual(m.select(self.state, True)["mode"], "resume")
        self.pass_group("G1")
        self.assertEqual(m.select(self.state, True)["group"], "G2")
        self.edit(lambda p: p["groups"][1].update(status="implemented"))
        self.assertEqual(m.select(self.state, True)["group_status"], "implemented")

    def test_current_feature_precedes_other_ready_groups(self):
        self.pass_group("G1")
        self.edit(lambda p: p.update(active_feature="users"))
        self.assertEqual(m.select(self.state, False)["group"], "G3")

    def test_downstream_count_then_size_then_id(self):
        def arrange(p):
            p["groups"][0]["depends_on"] = []
            p["groups"][1]["depends_on"] = []
            p["groups"][2]["depends_on"] = ["G2"]
            p["groups"][1]["entry_priority"] = 2
        self.edit(arrange)
        self.assertEqual(m.select(self.state, False)["group"], "G2")
        self.edit(lambda p: p["groups"][2].update(depends_on=[]))
        self.assertEqual(m.select(self.state, False)["group"], "G1")
        def extra_content(p):
            item = dict(p["items"][0])
            item.update(id="I4", locator="second source function")
            p["items"].append(item)
        self.edit(extra_content)
        self.assertEqual(m.select(self.state, False)["group"], "G2")

    def test_blocked_group_does_not_unlock_dependants(self):
        m.select(self.state, True)
        self.record("G1", "blocked")
        result = m.select(self.state, False)
        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["remaining"]["G2"]["waiting_for"], ["G1"])

    def test_pass_requires_targets_and_real_evidence(self):
        with self.assertRaisesRegex(ValueError, "Missing target"):
            self.record("G1")
        self.put("react/1.tsx", "translated")
        self.record("G1")
        self.assertEqual(m.check_state(self.state)["groups_passed"], 1)
        self.put("migration/state/evidence/G1.log", "changed log")
        self.assertEqual(m.check_state(self.state)["invalidated_groups"], ["G1"])

    def test_direct_pass_flag_does_not_count_as_validation(self):
        self.edit(lambda p: p["groups"][0].update(status="passed"))
        self.assertEqual(m.check_state(self.state)["groups_passed"], 0)
        selected = m.select(self.state, True)
        self.assertEqual((selected["group"], selected["mode"]), ("G1", "revalidate"))

    def test_shared_change_revalidates_and_resumes_original_group(self):
        m.select(self.state, True)
        self.pass_group("G1")
        m.select(self.state, True)
        self.put("react/1.tsx", "changed utility")
        selected = m.select(self.state, True)
        self.assertEqual((selected["group"], selected["mode"]), ("G1", "revalidate"))
        self.record("G1")
        resumed = m.select(self.state, True)
        self.assertEqual((resumed["group"], resumed["mode"]), ("G2", "resume"))

    def test_transitive_validation_invalidation(self):
        self.pass_group("G1")
        self.pass_group("G2")
        self.put("react/1.tsx", "changed shared file")
        self.assertEqual(m.check_state(self.state)["invalidated_groups"], ["G1", "G2"])

    def test_contract_change_mid_round_refuses_resume(self):
        m.select(self.state, True)
        self.put("migration/state/groups/G1/contract.md", "changed scope")
        with self.assertRaisesRegex(ValueError, "contract/snapshot changed"):
            m.select(self.state, True)

    def test_final_requires_integration_and_fresh_evidence(self):
        for gid in ("G1", "G2", "G3"):
            self.pass_group(gid)
        self.assertEqual(m.select(self.state, False)["status"], "groups_complete")
        with self.assertRaisesRegex(ValueError, "Final check incomplete"):
            m.check_state(self.state, True)
        self.record("J1", integration=True)
        self.assertEqual(m.check_state(self.state, True)["status"], "complete")
        self.put("migration/state/evidence/J1.log", "different run")
        with self.assertRaisesRegex(ValueError, "Final check incomplete"):
            m.check_state(self.state, True)

    def test_symlink_recorded_without_silent_directory_traversal(self):
        self.put("external/asset.txt", "asset")
        (self.root / "vue/linked").symlink_to(self.root / "external", target_is_directory=True)
        m.inventory(self.args, self.state)
        inv = m.read(self.state / "inventory.json")
        self.assertEqual(inv["files"]["vue/linked"]["kind"], "symlink")
        self.assertNotIn("vue/linked/asset.txt", inv["files"])

    def test_cli_final_returns_nonzero_before_completion(self):
        script = str(Path(__file__).with_name("migration_state.py"))
        args = [sys.executable, script, "check", "--state", str(self.state)]
        checked = subprocess.run(args, capture_output=True, text=True)
        self.assertEqual(checked.returncode, 0, checked.stderr)
        self.assertEqual(json.loads(checked.stdout)["status"], "plan_valid")
        final = subprocess.run(args + ["--final"], capture_output=True, text=True)
        self.assertEqual(final.returncode, 2)
        self.assertEqual(json.loads(final.stdout)["status"], "needs_attention")

    def test_multiple_revalidations_preserve_suspended_group(self):
        self.pass_group("G1")
        self.pass_group("G2")
        self.assertEqual(m.select(self.state, True)["group"], "G3")
        self.put("react/1.tsx", "changed shared behavior")
        self.assertEqual(m.select(self.state, True)["group"], "G1")
        self.record("G1")
        self.assertEqual(m.select(self.state, True)["group"], "G2")
        self.record("G2")
        resumed = m.select(self.state, True)
        self.assertEqual((resumed["group"], resumed["mode"]), ("G3", "resume"))

    def test_exclusion_requires_reason_and_cannot_claim_completion(self):
        def exclude(p):
            p["items"][0].update(disposition="exclude", group=None)
        self.edit(exclude)
        with self.assertRaisesRegex(ValueError, "Exclusion needs reason"):
            m.check_state(self.state)

    def test_empty_contract_and_target_locator_rejected(self):
        self.put("migration/state/groups/G1/contract.md", "")
        with self.assertRaisesRegex(ValueError, "empty group contract"):
            m.check_state(self.state)
        self.put("migration/state/groups/G1/contract.md", "old behavior")
        self.put("react/1.tsx", "translated behavior")
        self.edit(lambda p: p["items"][0].pop("target_locator"))
        with self.assertRaisesRegex(ValueError, "target function/component/resource locator"):
            self.record("G1")


if __name__ == "__main__":
    unittest.main()
