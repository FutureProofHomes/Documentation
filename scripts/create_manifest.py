#!/usr/bin/env python3

import sys
import os
import json
import hashlib
import urllib.request
import urllib.error
from . import utils
    
def process_build(BASE_NAME, factory_urls, ota_urls, release_tag, beta, release_repository):
        BROWSER_URL_FACTORY = factory_urls.get(BASE_NAME)
        BROWSER_URL_OTA = ota_urls.get(BASE_NAME)
        # Compute OTA_MD5 if BROWSER_URL_OTA is available
        OTA_MD5 = ''
        # Compute OTA_MD5 if BROWSER_URL_OTA is available
        if BROWSER_URL_OTA:
            try:
                with urllib.request.urlopen(BROWSER_URL_OTA) as response:
                    ota_data = response.read()
                OTA_MD5 = hashlib.md5(ota_data).hexdigest()
            except urllib.error.HTTPError as e:
                utils.error_exit(f"Failed to download OTA binary for {BASE_NAME}: {e}")

        # Check if the firmware directory exists
        MANIFEST_FILE_DIR = os.path.join('.', 'assets', 'manifests', BASE_NAME, release_tag)

        # Call the make_manifest function
        utils.make_manifest(
            BASE_NAME,
            release_tag,
            release_repository,
            BROWSER_URL_OTA,
            OTA_MD5,
            BROWSER_URL_FACTORY,
            MANIFEST_FILE_DIR,
            beta
        )
def main():
    # Check if at least two parameters are passed
    if len(sys.argv) < 3:
        utils.error_exit(f"Usage: {sys.argv[0]} <release_tag> <release_repository>")

    # Assign input parameters to variables
    release_tag = sys.argv[1]
    release_repository = sys.argv[2]

    # Ensure GITHUB_TOKEN is set
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
    if not GITHUB_TOKEN:
        utils.error_exit("GITHUB_TOKEN is not set.")

    # Determine if the release is a beta release.
    beta = any(keyword in release_tag.lower() for keyword in ['beta', 'alpha', 'rc'])

    data = utils.get_release_info(release_tag, release_repository, GITHUB_TOKEN)
    
    if not data:
        utils.error_exit(f"Failed to fetch release info for {release_tag}")

    # Parse the JSON data
    release_info = json.loads(data.decode('utf-8'))
    assets = release_info.get('assets', [])

    # Declare dictionaries to hold the URLs
    factory_urls = {}
    ota_urls = {}

    # Process the assets to build the dictionaries
    for asset in assets:
        name = asset.get('name')
        url = asset.get('browser_download_url')

        if name.endswith('.factory.bin'):
            build_name = name[:-len('.factory.bin')]
            factory_urls[build_name] = url
        elif name.endswith('.ota.bin'):
            build_name = name[:-len('.ota.bin')]
            ota_urls[build_name] = url

    # Get the list of unique build names
    build_names = set(factory_urls.keys()).union(set(ota_urls.keys()))

    # Process each build
    for BASE_NAME in build_names:
        process_build(BASE_NAME, factory_urls, ota_urls, release_tag, beta, release_repository)

if __name__ == "__main__":
    main()
