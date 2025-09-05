The firmware running on the Satellite1 is [open source](https://github.com/FutureProofHomes/Satellite1-ESPHome/blob/develop/LICENSE).  All we ask contribute back the FutureProofHomes community by submitting pull requests to the [Satellite1-ESPHome](https://github.com/FutureProofHomes/Satellite1-ESPHome) repository.  You may want to modify and flash your custom firmware on the Sat1 to do the following:

- Hardcode your Wifi SSID & Password
- Hardcode the Snapserver's IP address
- Add custom wake words
- Hide or show more logs for deep troubleshooting
- Change or extend the core functionality in any way you desire.

??? Warning "After taking control of your device's firmware you will no longer receive official firmware updates. If you'd like to get back in sync with the official Sat1 firmware you'll need to [restore factory firmware back to the Sat1](/satellite1-faqs#faq_anchor_factory_reset)."

??? Warning "Please also be aware that flashing custom firmware can potentially damage the Sat1 device. These instructions are provided with the understanding that you have the necessary expertise to proceed. We will assume a certain level of familiarity with the process. Proceed with caution, and enjoy the journey!"

## ESPHome Compatibility Matrix
Specific Sat1 firmware releases can only be compiled with specific ESPHome versions.

| Sat1 Release      | ESPHome Version                          |
| ----------- | ------------------------------------ |
| [v0.1.3](https://github.com/FutureProofHomes/Satellite1-ESPHome/releases/tag/v0.1.3-beta.2)    | [2025.5.2 - 2025.7.5](https://github.com/esphome/esphome/releases/tag/2025.7.5) |
| [v0.1.2](https://github.com/FutureProofHomes/Satellite1-ESPHome/releases/tag/v0.1.2)    | [2025.5.2](https://github.com/esphome/esphome/releases/tag/2025.5.2) |
| [v0.1.1](https://github.com/FutureProofHomes/Satellite1-ESPHome/releases/tag/v0.1.1)    | [2025.4.2](https://github.com/esphome/esphome/releases/tag/2025.4.2)  |


## Import the Sat1 to your ESPHome Dashboard and Take Control 

NOTE: Your Home Assistant instance must have the ability to run "Add-Ons". If you cannot run add-ons, see alternate ways to run this software by [reading ESPHome's official documentation](https://esphome.io/guides/getting_started_hassio#installing-esphome-device-compiler).

1. <b>Ensure you're running the correct ESPHome Device Builder version that follows the above ESPHome compatibility matrix:</b>
<br>[Install ESPHome Device Builder](https://github.com/khenderick/esphome-legacy-addons){ .md-button .md-button--primary }

2. <b>After the install is complete click "Open Web UI":</b>
<br>![Open WebUI](/assets/esphome_device_builder/1_open_ui.png){ width="100%" loading=lazy }</br>

3. <b>Click "SHOW" to see your Sat1 devices you have not taken control of:</b>
<br>![Show Devices](/assets/esphome_device_builder/2_show_devices.png){ width="100%" loading=lazy }</br>

4. <b>Click "Take Control" and give the device a name:</b>
<br>![Take Control](/assets/esphome_device_builder/3_take_control.png){ width="100%" loading=lazy }</br>
<br>![Give device a name](/assets/esphome_device_builder/4_name_device.png){ width="100%" loading=lazy }</br>

5. <b>Wait while the firmware compiles and your Sat1 is flashed over-the-air with your new firmware. This can take a significant amount of time depending on your server's hardware specs (Recommend 8gb RAM or more to avoid compilation errors). Please be patient:</b>
<br>![Compile Firmware](/assets/esphome_device_builder/6_firmware_compile.png){ width="100%" loading=lazy }</br>

6. <b>When the firmware is uploaded to the Sat1, you'll see the boot logs on your screen. You can close the window and return to the ESPHome Device Builder dashboard and click the "EDIT" button and have fun!</b>
<br>![Edit the Firmware](/assets/esphome_device_builder/8_build_cool_stuff.png){ width="100%" loading=lazy }</br>

Congrats.  You're done!