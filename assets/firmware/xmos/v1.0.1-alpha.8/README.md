# Satellite XMOS firmware

## Variants
*satellite_firmware_bypass.xe*

Initial variant which bypasses the mic-pipeline, so the raw mic signal is passed to the ESP32.

## Pre-Requirements


## Running / Flashing

Running without flashing:

```bash
xrun --xscope satellite_firmware_bypass.xe
```

Flashing:
```bash
xflash --quad-spi-clock 50MHz --factory satellite_firmware_bypass.xe --boot-partition-size 0x100000 --data satellite_firmware_bypass_data_partition.bin
```


## Github Artifacts
On each pull request and push to `develop` and `main` the firmware is built and can be downloaded from the respective workflow under the github action menu.

Additionally, the build workflow can be triggered manually for any branch by selecting `Build and Upload Artifacts` workflow and clicking the `Run workflow` button on the top right of the workflow table.
Don't check `Run as release` for now...

The artifact zip archive also includes a `build_metadata.json` which contains the sha of the commit the firmware was built of. 


## Building Locally

Run the following commands in the root folder to build the firmware.

On Linux and Mac run:

```bash
cmake -B build --toolchain xmos_cmake_toolchain/xs3a.cmake
cd build

make satellite_firmware_bypass
```

On Windows run:
```bash
cmake -G Ninja -B build --toolchain xmos_cmake_toolchain/xs3a.cmake
cd build

ninja satellite_firmware_bypass
```

From the build folder, create the data partition containing the filesystem and
flash the device with the appropriate command to the desired configuration:

On Linux and Mac run:


```bash
make flash_app_satellite_firmware_bypass
```

On Windows run:


```bash
ninja flash_app_satellite_firmware_bypass
```

Once flashed, the application will run.

If changes are made to the data partition components, the application must be
re-flashed.



