#!/bin/bash

# Exit immediately if any command exits with a non-zero status
set -e

# Function to print an error message and exit
error_exit() {
  echo "$1" 1>&2
  exit 1
}

# Check if at least two parameters are passed
if [ $# -lt 2 ]; then
  error_exit "Usage: $0 <release_tag> <esphome_firmware_repository>"
fi

# Assign input parameters to variables
release_tag="$1"
esphome_firmware_repository="$2"

# Check if the firmware directory exists
FIRMWARE_DIR="./assets/firmware/esphome/$release_tag"
if [ ! -d "$FIRMWARE_DIR" ]; then
  error_exit "Firmware directory '$FIRMWARE_DIR' does not exist."
fi

# Create the manifest directory if it doesn't exist
mkdir -p ./manifests/$release_tag

# Find all .bin and .ota.bin files and process them in pairs
for OTA_FILE in $(ls $FIRMWARE_DIR/*.ota.bin 2>/dev/null); do
  # Derive the base name by stripping the .ota.bin extension
  BASE_NAME=$(basename "$OTA_FILE" .ota.bin)

  # Find the corresponding full .bin file
  BIN_FILE="$FIRMWARE_DIR/${BASE_NAME}.bin"

  # Check if both files exist
  if [ -f "$OTA_FILE" ] && [ -f "$BIN_FILE" ]; then
    # Create a manifest file for this hardware revision
    MANIFEST_FILE="./manifests/${release_tag}/${BASE_NAME}.manifest.json"

    cat <<EOF > "$MANIFEST_FILE"
{
  "name": "ESPHome Firmware for $BASE_NAME",
  "version": "$release_tag",
  "new_install_prompt_erase": true,
  "builds": [
      {
        "chipFamily": "esp32",
        "ota": {
          "path": "$(basename $OTA_FILE)",
          "md5": "$(md5sum $OTA_FILE | cut -d' ' -f1)",
          "summary": "ESPHome Firmware for $BASE_NAME",
          "release_url": "https://github.com/$esphome_firmware_repository/releases/tag/$release_tag/"
        },
        "parts": [
          {
            "path": "$(basename $BIN_FILE)",
            "offset": 0
          }
        ]
      }
    ]
}
EOF

    echo "Created manifest for hardware revision: $BASE_NAME"
  else
    echo "Warning: Matching .bin file not found for OTA file $OTA_FILE."
  fi
done

# Check if no OTA files were found
if [ -z "$(ls $FIRMWARE_DIR/*.ota.bin 2>/dev/null)" ]; then
  echo "No .ota.bin files found in the directory '$FIRMWARE_DIR'."
fi
