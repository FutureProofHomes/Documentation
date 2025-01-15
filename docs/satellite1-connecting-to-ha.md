Your Satellite1 arrives pre-flashed with all the necessary firmware to get you up and running quickly. You have 2 choices: 

??? abstract "I want to set up via my iPhone or Android device with Bluetooth. (Recommended)"

    <!-- <iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> -->

    Open the Home Assistant Companion App on your Android or iPhone.  Make sure Bluetooth on your phone is on and that you're nearby the Sat1!  
    
    1. <b>Tap "Settings":</b>
    <br>![Tap "Settings":](/assets/ble_improv/1_go_to_settings.png){ width="100%" loading=lazy }</br>

    2. <b>Tap "Devices & Services":</b>
    <br>![Tap "Devices & Services":](/assets/ble_improv/2_go_to_devices.png){ width="100%" loading=lazy }</br>

    3. <b>Tap "Add" next to your Sat1 device (contains last 6 of device MAC address):</b>
    <br>![Tap "Add" next to your Sat1 device (contains last 6 of device MAC address):](/assets/ble_improv/3_improv_discovered_device.png){ width="100%" loading=lazy }</br>

    4. <b>Type in your 2.4ghz network credentials:</b>
    <br>![Type in your 2.4ghz network credentials:](/assets/ble_improv/4_improv_add_wifi_credentials.png){ width="100%" loading=lazy }</br>

    5. <b>On the Sat1 HAT, press the right "Action button" to give authorization:</b>
    <br>![On the Sat1 HAT, press the right "Action button" to give authorization:](/assets/ble_improv/5_improv_press_authorization_button.png){ width="100%" loading=lazy }</br>
    <br>![Click action buttons](/assets/ble_improv/6_click_action_button.png){ width="100%" loading=lazy }</br>

    6. <b>Tap "Continue" after successful Wifi connection:</b>
    <br>![Tap "Continue" after successfull Wifi connection:](/assets/ble_improv/8_improv_successful_wifi_connection.png){ width="100%" loading=lazy }</br>

    7. <b>Tap "Ok" to begin setting up ESPHome:</b>
    <br>![Tap "Ok" to begin setting up ESPHome:](/assets/ble_improv/9_esphome_setup_request.png){ width="100%" loading=lazy }</br>

    8. <b>Tap the name of your Sat1 device and then tap the "Submit" button:</b>
    <br>![Tap the name if your Sat1 device and then tap the "Submit" button:](/assets/ble_improv/10_esphome_select_device.png){ width="100%" loading=lazy }</br>

    9. <b>The Wizard will pull down the most recent Sat1 Firmware:</b>
    <br>![The Wizard will pull down the most recent Sat1 Firmware:](/assets/ble_improv/12_wizard_checking_for_updates.png){ width="100%" loading=lazy }</br>

    10. <b>The Wizard will ask you to say the Wake Word twice:</b>
    <br>![The Wizard will ask you to say the Wake Word twice:](/assets/ble_improv/13_wizard_first_wake_word_test.png){ width="100%" loading=lazy }</br>

    11. <b>Type the Area this Sat1 falls in:</b>
    <br>![Type the Area this Sat1 falls in:](/assets/ble_improv/15_wizard_assign_area.png){ width="100%" loading=lazy }</br>

    12. <b>Stick with the default or change the wake word, conversation agent, and voice:</b>
    <br>![Stick with the default or change the wake word, conversation agent, and voice:](/assets/ble_improv/16_wizard_quick_pipeline_config.png){ width="100%" loading=lazy }</br>

    13. <b>After completing the Wizard, do NOT click to add the Sat1 to ESPHome again.  Simply refresh and this will go away.</b>
    <br>![After completing the Wizard, do NOT click to add the Sat1 to ESPHome again.  Simply refresh and this will go away.](/assets/ble_improv/17_ignore_device_discovered.png){ width="100%" loading=lazy }</br>

    Congrats.  You're done!

??? abstract "I want to set up via my computer & USB-C cable. (Advanced)"

    Plug your Sat1 directly into your computer with a USB-C cable that supports a data connection.

    1. <b>Click <esp-web-install-button id="install-button" manifest="https://raw.githubusercontent.com/FutureProofHomes/Documentation/refs/heads/main/manifest.json" install-supported></esp-web-install-button> and select the JTAG device in the browser's notification:</b>
    <br>![Select JTAG](/assets/ESPHome-SerialConn.png){ width="100%" loading=lazy }</br>

    2. <b>Click "Install":</b>
    <br>![Image title](/assets/ESPHome-Install.png){ width="100%" loading=lazy }</br>
    
    3. <b>Optionally erase the device, then click "Next" and then "Install":</b>
    <br>![Image title](/assets/ESPHome-Erase.png){ width="100%" loading=lazy }</br>
    <br>![Image title](/assets/ESPHome-ConfirmInstall.png){ width="100%" loading=lazy }</br>

    4. <b>Installation will complete. Click "Next":</b>
    <br>![Image title](/assets/ESPHome-InstallationComplete.png){ width="100%" loading=lazy }</br>

    5. <b>Type in your 2.4ghz WiFi network and click "Connect".  Your device will begin sparkling blue while attempting to connect.</b>
    <br>![Image title](/assets/ConfigureWifi.png){ width="100%" loading=lazy }</br>

    6. <b>Congrats you're now connected to your Wifi.  Your device will now begin sparkling red.  This means it needs to be connected to ESPHome in your Home Assistant instance.</b>
    <br>![Image title](/assets/ESPHome-WiFiConnected.png){ width="100%" loading=lazy }</br>

    7. <b>Inside Home Assistant, go to "Settings -> Devices & Services" and notice you have a Discovered `Satellite1 xxxxxx' device.  Click add and follow the onboarding steps.</b>
    <br>![Image title](/assets/discovered_sat1.png){ width="100%" loading=lazy }</br>

    Congrats.  You're done!


## ESPHome User Interface
Once your Sat1 is connected to Home Assistant you should familiarize yourself with all the server-side settings you may want to change:

1. <b>Inside your Home Assistant, head over to "Settings -> Devices & Services -> ESPHome" and click on your Sat1 device:</b>
  <br>![esphome device list](/assets/esphome/1_esphome_device_list.png){ width="100%" loading=lazy }</br>

  2. <b>Understand all the features of your Sat1 device:</b>
  <br>![top esphome device](/assets/esphome/2_esphome_top_page.png){ width="100%" loading=lazy }</br>
  <br>![top esphome device](/assets/esphome/3_esphome_bottom_page.png){ width="100%" loading=lazy }</br>