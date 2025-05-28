# ADD CODE HERE
# change script to whatever language you are comfortable withimport json
import json
import sys

def is_valid_change(change):
    action = change.get("change", {}).get("actions", [])
    if action == ["create"]:
        return True
    elif action == ["update"]:
        before = change["change"].get("before", {})
        after = change["change"].get("after", {})

        # Only `tags` should change
        if before.keys() != after.keys():
            return False

        for key in before:
            if key != "tags" and before[key] != after[key]:
                return False

        before_tags = before.get("tags", {})
        after_tags = after.get("tags", {})

        # Only GitCommitHash can change
        diff_keys = {k for k in before_tags if before_tags[k] != after_tags.get(k)} | {k for k in after_tags if k not in before_tags}
        return diff_keys == {"GitCommitHash"}

    return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <tfplan.json>")
        sys.exit(1)

    tfplan_file = sys.argv[1]
    with open(tfplan_file, 'r') as f:
        tfplan = json.load(f)

    changes = tfplan.get("resource_changes", [])
    errors = []

    for change in changes:
        actions = change.get("change", {}).get("actions", [])
        if "delete" in actions:
            errors.append(f"❌ Delete action detected in resource: {change.get('address')}")
        elif not is_valid_change(change):
            errors.append(f"❌ Invalid update in resource: {change.get('address')}")

    if errors:
        print("\nPlan validation failed. Apply should NOT proceed.\n")
        for error in errors:
            print(error)
        sys.exit(1)
    else:
        print("✅ Plan is valid. Safe to apply.")

if __name__ == "__main__":
    main()
