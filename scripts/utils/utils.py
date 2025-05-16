import os
import json
import shutil
import sys
import urllib.request


def extract_variant(BASE_NAME):
    parts = BASE_NAME.split(".")
    return parts[1] if len(parts) > 1 else ""

def make_manifest(BASE_NAME, release_tag, esphome_firmware_repository, OTA_MD5, MANIFEST_FILE_DIR, beta, FIRMWARE_FILE_DIR):
    # Create the manifest file directory if it does not exist
    if not os.path.exists(MANIFEST_FILE_DIR):
        os.makedirs(MANIFEST_FILE_DIR)

    MANIFEST_FILE = os.path.join(MANIFEST_FILE_DIR, f"{BASE_NAME}.manifest.json")
    DIR_NAME = os.path.join(FIRMWARE_FILE_DIR, "beta") if beta else os.path.join(FIRMWARE_FILE_DIR, "production")
    variant = extract_variant(BASE_NAME)
    
    # Build the manifest data
    manifest_data = {
        "name": f"ESPHome Firmware for Satellite1-Core-Board",
        "version": release_tag + (f"+{variant}" if variant else ""),
        "new_install_prompt_erase": True,
        "builds": [
            {
                "chipFamily": "ESP32-S3",
                "ota": {
                    "path": f"{DIR_NAME}/{BASE_NAME}.ota.bin",
                    "md5": OTA_MD5,
                    "summary": f"ESPHome Firmware for {BASE_NAME}",
                    "release_url": f"https://github.com/{esphome_firmware_repository}/releases/tag/{release_tag}/"
                },
                "parts": [
                    {
                        "path": f"{DIR_NAME}/{BASE_NAME}.factory.bin",
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
    if variant != "":
        variant += "."
    if beta:
        shutil.copyfile(MANIFEST_FILE, os.path.join("..", f'manifest-beta.{variant}json'))
    else:
        shutil.copyfile(MANIFEST_FILE, os.path.join("..", f'manifest.{variant}json'))

def error_exit(message):
    print(message, file=sys.stderr)
    sys.exit(1)

def get_release_info(release_tag, release_repository, GITHUB_TOKEN):
    # Fetch the assets from the GitHub API
    api_url = f"https://api.github.com/repos/{release_repository}/releases/tags/{release_tag}"
    request = urllib.request.Request(api_url)
    request.add_header('Accept', 'application/vnd.github+json')
    if not GITHUB_TOKEN is None:
        request.add_header('Authorization', f'Bearer {GITHUB_TOKEN}')

    try:
        with urllib.request.urlopen(request) as response:
            return response.read()
    except urllib.error.HTTPError as e:
        error_exit(f"Failed to fetch release info: {e}")


def download_release(url, beta, FIRMWARE_FILE_DIR):
    # Download the release
    FILE_DIR = os.path.join(FIRMWARE_FILE_DIR, "beta") if beta else os.path.join(FIRMWARE_FILE_DIR, "production")
    os.makedirs(FILE_DIR, exist_ok=True)

    # Determine the filename and file path
    filename = os.path.basename(url)
    file_path = os.path.join(FILE_DIR, filename)

    # Download the release
    request = urllib.request.Request(url)
    request.add_header('Accept', 'application/octet-stream')
    try:
        with urllib.request.urlopen(request) as response:
            # Open the file in binary write mode
            with open(file_path, 'wb') as f:
                # Copy the response to the file in chunks
                shutil.copyfileobj(response, f)
        print(f"Downloaded file to {file_path}")
        return file_path
    except urllib.error.HTTPError as e:
        error_exit(f"Failed to download release: {e}")
    except IOError as e:
        error_exit(f"Failed to write file to {file_path}: {e}")
