#!/bin/bash

# Exit immediately if any command exits with a non-zero status
set -e

# Function to print an error message and exit
error_exit() {
  echo "$1" 1>&2
  exit 1
}

# Check if the correct number of arguments were provided
if [ "$#" -ne 2 ]; then
  error_exit "Usage: $0 <version> <release_repo>"
fi

# Assign the arguments to named variables
version=$1
release_repo=$2

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change the current working directory to the script directory
cd "$SCRIPT_DIR"

./create_manifest.py $version $release_repo