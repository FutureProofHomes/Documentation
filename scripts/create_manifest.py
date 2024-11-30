#!/usr/bin/env python3

import sys
import os
import json
import hashlib
import urllib.request
import urllib.error

# Set the path to the directory containing this script and add it to the system path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_DIR)

from utils import utils


def process_build(
    BASE_NAME,
    factory_urls,
    ota_urls,
    release_tag,
    beta,
    release_repository,
    GITHUB_TOKEN,
):
    # Get the Asset ID for the factory and OTA binaries
    # Sample URL: https://api.github.com/repos/FutureProofHomes/Satellite1-ESPHome/releases/assets/210089213
    BASE_URL=f"https://api.github.com/repos/{release_repository}/releases/assets/"
    BROWSER_URL_FACTORY = f"{BASE_URL}{factory_urls.get(BASE_NAME)}"
    BROWSER_URL_OTA = f"{BASE_URL}{ota_urls.get(BASE_NAME)}"
    print(f"Factory URL: {BROWSER_URL_FACTORY}")
    print(f"OTA URL: {BROWSER_URL_OTA}")
    # Compute OTA_MD5 if BROWSER_URL_OTA is available
    OTA_MD5 = ""
    # Compute OTA_MD5 if BROWSER_URL_OTA is available
    if BROWSER_URL_OTA:
        headers = {
            "Accept": "application/octet-stream",
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        request = urllib.request.Request(BROWSER_URL_OTA, headers=headers)
        try:
            with urllib.request.urlopen(request) as response:
                ota_data = response.read()
            OTA_MD5 = hashlib.md5(ota_data).hexdigest()
        except urllib.error.HTTPError as e:
            utils.error_exit(f"Failed to download OTA binary for {BASE_NAME}: {e}")

    # Check if the firmware directory exists
    MANIFEST_FILE_DIR = os.path.join("..", "assets", "manifests", BASE_NAME, release_tag)

    # Call the make_manifest function
    utils.make_manifest(
        BASE_NAME,
        release_tag,
        release_repository,
        BROWSER_URL_OTA,
        OTA_MD5,
        BROWSER_URL_FACTORY,
        MANIFEST_FILE_DIR,
        beta,
    )


def main():
    # Check if at least two parameters are passed
    if len(sys.argv) < 3:
        utils.error_exit(f"Usage: {sys.argv[0]} <release_tag> <release_repository>")

    # Assign input parameters to variables
    release_tag = sys.argv[1]
    release_repository = sys.argv[2]

    # Ensure GITHUB_TOKEN is set
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
    if not GITHUB_TOKEN:
        utils.error_exit("GITHUB_TOKEN is not set.")
    print(f"Fetching release info for {release_tag} from {release_repository}")
    # Determine if the release is a beta release.
    beta = any(keyword in release_tag.lower() for keyword in ["beta", "alpha", "rc"])

    data = utils.get_release_info(release_tag, release_repository, GITHUB_TOKEN)

    if not data:
        utils.error_exit(f"Failed to fetch release info for {release_tag}")

    # Parse the JSON data
    release_info = json.loads(data.decode("utf-8"))

    assets = release_info.get("assets", [])

    # Declare dictionaries to hold the URLs
    factory_urls = {}
    ota_urls = {}

    # Process the assets to build the dictionaries
    for asset in assets:
        print(f"Processing asset: {asset.get('name')}")
        name = asset.get("name")
        asset_id = asset.get("id") # Get the Asset ID
        # url = asset.get("browser_download_url")

        if name.endswith(".factory.bin"):
            build_name = name[: -len(".factory.bin")]
            factory_urls[build_name] = asset_id
        elif name.endswith(".ota.bin"):
            build_name = name[: -len(".ota.bin")]
            ota_urls[build_name] = asset_id

    # Get the list of unique build names
    build_names = set(factory_urls.keys()).union(set(ota_urls.keys()))

    # Process each build
    for BASE_NAME in build_names:
        process_build(
            BASE_NAME,
            factory_urls,
            ota_urls,
            release_tag,
            beta,
            release_repository,
            GITHUB_TOKEN,
        )


if __name__ == "__main__":
    main()
