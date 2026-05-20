import json
import os


def on_config(config):
    manifests = {
        "fw_stable": "manifest.json",
        "fw_beta": "manifest-beta.json",
    }
    for key, filename in manifests.items():
        path = os.path.join(config["docs_dir"], "..", filename)
        if os.path.exists(path):
            with open(path) as f:
                manifest = json.load(f)
                config["extra"][f"{key}_version"] = manifest["version"]
                config["extra"][f"{key}_release_url"] = manifest["builds"][0]["ota"]["release_url"]
    return config
