## Import the Sat1 to your ESPHome Dashboard
The firmware running on the Satellite1 is [open source](https://github.com/FutureProofHomes/Satellite1-ESPHome/blob/develop/LICENSE).  This means you can modify the firmware to build all kinds of amazing things with it!  All we ask contribute back the FutureProofHomes community by submitting pull requests to the [Satellite1-ESPHome](https://github.com/FutureProofHomes/Satellite1-ESPHome) repository.

??? Warning "After taking control of your device's firmware you will no longer receive firmware updates from the community. If you'd like to get back in sync with the community you'll need to [restore factory firmware back to the Sat1](/satellite1-faqs#faq_anchor_factory_reset)."

??? Warning "Please also be aware that flashing custom firmware can potentially damage the Sat1 device. These instructions are provided with the understanding that you have the necessary expertise to proceed. We will assume a certain level of familiarity with the process. Proceed with caution, and enjoy the journey!"

NOTE: Your Home Assistant instance must have the ability to run "Add-Ons". If you cannot run add-ons, see alternate ways to run this software by [reading ESPHome's official documentation](https://esphome.io/guides/getting_started_hassio#installing-esphome-device-compiler).

1. <b>Install the ESPHome Device Builder Add-on by clicking below:</b>
<br>[Install ESPHome Device Builder](https://my.home-assistant.io/redirect/supervisor_addon/?addon=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon){ .md-button .md-button--primary }

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