import os
import json
import shutil
import sys
import urllib.request

def make_manifest(BASE_NAME, release_tag, esphome_firmware_repository, BROWSER_URL_OTA, OTA_MD5, BROWSER_URL_FACTORY, MANIFEST_FILE_DIR, beta):
    # Create the manifest file directory if it does not exist
    if not os.path.exists(MANIFEST_FILE_DIR):
        os.makedirs(MANIFEST_FILE_DIR)

    MANIFEST_FILE = os.path.join(MANIFEST_FILE_DIR, f"{BASE_NAME}.manifest.json")

    # Build the manifest data
    manifest_data = {
        "name": f"ESPHome Firmware for {BASE_NAME}",
        "version": release_tag,
        "new_install_prompt_erase": True,
        "builds": [
            {
                "chipFamily": "ESP32-S3",
                "ota": {
                    "path": BROWSER_URL_OTA,
                    "md5": OTA_MD5,
                    "summary": f"ESPHome Firmware for {BASE_NAME}",
                    "release_url": f"https://github.com/{esphome_firmware_repository}/releases/tag/{release_tag}/"
                },
                "parts": [
                    {
                        "path": BROWSER_URL_FACTORY,
                        "offset": 0
                    }
                ]
            }
        ]
    }

    # Adjust the name if it's a beta release
    if beta:
        manifest_data["name"] = f"ESPHome Beta Firmware for {BASE_NAME}"

    # Write the manifest data to a JSON file
    with open(MANIFEST_FILE, 'w') as f:
        json.dump(manifest_data, f, indent=2)

    # Copy the manifest file to the appropriate filename
    if beta:
        shutil.copyfile(MANIFEST_FILE, os.path.join("..", 'manifest-beta.json'))
    else:
        shutil.copyfile(MANIFEST_FILE, os.path.join("..", 'manifest.json'))

def error_exit(message):
    print(message, file=sys.stderr)
    sys.exit(1)

def get_release_info(release_tag, release_repository, GITHUB_TOKEN):
    # Fetch the assets from the GitHub API
    api_url = f"https://api.github.com/repos/{release_repository}/releases/tags/{release_tag}"
    request = urllib.request.Request(api_url)
    request.add_header('Accept', 'application/vnd.github+json')
    request.add_header('Authorization', f'Bearer {GITHUB_TOKEN}')

    try:
        with urllib.request.urlopen(request) as response:
            return response.read()
    except urllib.error.HTTPError as e:
        error_exit(f"Failed to fetch release info: {e}")