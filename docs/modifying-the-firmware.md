## Import the Sat1 to your ESPHome Dashboard
The firmware running on the Satellite1 is [open source](https://github.com/FutureProofHomes/Satellite1-ESPHome/blob/develop/LICENSE).  This means you can modify the firmware to build all kinds of amazing things with it!  All we ask contribute back the FutureProofHomes community by submitting pull requests to the [Satellite1-ESPHome](https://github.com/FutureProofHomes/Satellite1-ESPHome) repository.

??? Warning "After taking control of your device's firmware you will no longer receive firmware updates from the community. If you'd like to get back in sync with the community you'll need to [restore factory firmware back the Sat1](/troubleshooting/#start-the-device-in-boot-mode)."

??? Warning "Please also be aware that flashing custom firmware can potentially damage the Sat1 device. These instructions are provided with the understanding that you have the necessary expertise to proceed. We will assume a certain level of familiarity with the process. Proceed with caution, and enjoy the journey!"

There are two ways you can modify the firmware running on your Satellite1:

??? abstract "I want to make simple changes from my Home Assistant server via the ESPHome Device Builder dashboard software. (Recommended)"

    NOTE: Your Home Assistnat instance must have the ability to run "Add-Ons".  If you cannot run add-ons see alternate ways to run this software by [reading ESPHome's official documentation](https://esphome.io/guides/getting_started_hassio#installing-esphome-device-compiler).
    
    1. <b>Install the ESPHome Device Builder Add-on by clicking below:</b>
    <br>[Install ESPHome Device Builder](https://my.home-assistant.io/redirect/supervisor_addon/?addon=5c53de3b_esphome&repository_url=https%3A%2F%2Fgithub.com%2Fesphome%2Fhome-assistant-addon){ .md-button .md-button--primary }

    2. <b>After the install is complete click "Open Web UI":</b>
    <br><img width="50%" alt="image" src="/assets/esphome_device_builder/1_open_ui.png">

    3. <b>Click "SHOW" to see your Sat1 devices you have not taken control of:</b>
    <br><img width="50%" alt="image" src="/assets/esphome_device_builder/2_show_devices.png">

    4. <b>Click "Take Control" and give the device a name:</b>
    <br><img width="50%" alt="image" src="/assets/esphome_device_builder/3_take_control.png">
    <br><img width="50%" alt="image" src="/assets/esphome_device_builder/4_name_device.png">

    5. <b>Click "Install" to proivsion the encryption key between the Sat1 and Home Assistant server:</b>
    <br><img width="50%" alt="image" src="/assets/esphome_device_builder/5_accept_encryption.png">
    
    6. <b>Wait, while the firmware compiles and your Sat1 is flashed over-the-air with your new firmware.  This can a signifanct amount of time depending on your server's hardware specs.  Please be patient:</b>
    <br><img width="50%" alt="image" src="/assets/esphome_device_builder/6_firmware_compile.png">

    7. <b>When the firmware uploaded to the Sat1 you'll see the boot logs on your screen.  You can close the window and return to the ESPHome Device Builder dashboard and click the "EDIT" button and have fun!</b>
    <br><img width="50%" alt="image" src="/assets/esphome_device_builder/8_build_cool_stuff.png">

    Congrats.  You're done!

??? abstract "I'm a developer and want to make heavy changes in my IDE or from the command line. (Advanced)"

    I'll keep this simple.  Just read here: [Getting Started with the ESPHome Commmand Line](https://esphome.io/guides/getting_started_command_line)

    If you master this stuff then please join the Discord and our contributor team!  We'd love to have you!

[Back to top](./modifying-the-firmware.md/#modifying-the-firmware)