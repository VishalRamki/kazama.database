import os, hashlib, json

entries_dir = "database/entries"
manifest_file = "database/manifest.json"

# Load previous manifest if it exists
if os.path.exists(manifest_file):
    with open(manifest_file, "r") as f:
        old_manifest = json.load(f)
    old_version = old_manifest.get("version", "0.0.0")
else:
    old_version = "0.0.0"

# Increment the PATCH version
major, minor, patch = map(int, old_version.split("."))
patch += 1
new_version = f"{major}.{minor}.{patch}"

manifest = {
    "version": new_version,
    "files": []
}

for filename in sorted(os.listdir(entries_dir)):
    if not filename.endswith(".json"):
        continue
    path = os.path.join(entries_dir, filename)
    with open(path, "rb") as f:
        hash_hex = hashlib.sha256(f.read()).hexdigest().upper()
    entry_id = int(filename.split(".")[0])
    manifest["files"].append({"id": entry_id, "file": filename, "hash": hash_hex})

with open(manifest_file, "w") as f:
    json.dump(manifest, f, indent=2)
print(f"Manifest generated with {len(manifest['files'])} entries.")