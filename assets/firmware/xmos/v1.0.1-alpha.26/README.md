# Satellite1 XMOS firmware

## Variants
**satellite1_firmware_adec**

Uses the 'Automatic Delay Estimation and Correction' pipeline of the sln_voice example repository.

**satellite1_firmware_bypass**

Initial variant which bypasses the mic-pipeline, so the raw mic signal is streamed to the ESP32.

**dev_satellite1_usb_pipeline_analysis**

Enables recording of microphone channels at various stages of the processing pipeline through USB.


## Github Artifacts
On each pull request and push to `develop` the **satellite1_firmware_*** variants above are built and can be downloaded from the respective workflow under the github action menu.

Additionally, the build workflow can be triggered manually for any branch by selecting `Build and Upload Artifacts` workflow and clicking the `Run workflow` button on the top right of the workflow table.
Don't check `Run as release` for now...

The artifact zip archive also includes a `build_metadata.json` which contains the sha of the commit the firmware was built of. 

## Firmware Files

**variant_name.xe**

The XMOS executable (XE) binary format stores programs for XMOS devices and includes information about the system it is intended to run on, allowing support for multiple program loads, configurations and debugging.

**variant_name.factory.bin**

A complete image of the flash memory, including both the boot partition (containing the flash loader and factory image) and the data partition.

**variant_name.upgrade.bin**

A firmware upgrade image that can be uploaded through the Device Firmware Update (DFU) service on XMOS, requiring a factory image to already be flashed onto the device.

## Flashing via dfu-util
If the XMOS device is running a factory firmware with DFU over USB support, an upgrade image can be uploaded as follows:
```bash
dfu-util -e -a 1 -D variant_name.upgrade.bin
```


## Running / Flashing via xTAG
When the XMOS board is connected as a USB xTag device, the firmware can be run or flashed as follows:

Running without flashing:

```bash
xrun --xscope variant_name.xe
```

Flashing:
```bash
xflash --quad-spi-clock 50MHz --factory variant_name.xe --boot-partition-size 0x100000 --data variant_name_data_partition.bin
```


## Building the firmware Locally

### Clone repository

```bash
git clone https://github.com/FutureProofHomes/Satellite1-XMOS.git
cd Satellite1-XMOS
git submodule update --init --recursive
```

### Building the firmware (.xe files)
Run the following commands in the root folder to build the firmware.

On Linux and Mac run:

```bash
cmake -B build --toolchain xmos_cmake_toolchain/xs3a.cmake
cd build

make variant_name
```

On Windows run:
```bash
cmake -G Ninja -B build --toolchain xmos_cmake_toolchain/xs3a.cmake
cd build

ninja variant_name
```

### Creating factory and upgrade images

On Linux and Mac run:

```bash
cmake -B build --toolchain xmos_cmake_toolchain/xs3a.cmake
cd build

make create_flash_img_variant_name
make create_upgrade_img_variant_name
```

On Windows run:
```bash
cmake -G Ninja -B build --toolchain xmos_cmake_toolchain/xs3a.cmake
cd build

ninja create_flash_img_variant_name
ninja create_upgrade_img_variant_name
```




