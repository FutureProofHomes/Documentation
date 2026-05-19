import json
import os


def on_config(config):
    manifests = {
        "fw_stable_version": "manifest.json",
        "fw_beta_version": "manifest-beta.json",
    }
    for key, filename in manifests.items():
        path = os.path.join(config["docs_dir"], "..", filename)
        if os.path.exists(path):
            with open(path) as f:
                config["extra"][key] = json.load(f)["version"]
    return config
