## Connecting to Home Assistant
Your Satellite1 arrives pre-flashed from the factory and will boot into BLE improv mode with white sparkling LEDs.  Follow the steps below to connect to Home Assistnat via Bluetooth.

1. <b>Open Home Assistnat on your iPhone or Android device with Bluetooth enabled. Navigate to "Settings -> Devices & Services" and tap "Add" next to your discovered Sat1 device:</b>
<br>![Tap "Add" next to your Sat1 device (contains last 6 of device MAC address):](/assets/ble_improv/3_improv_discovered_device.png){ width="60%" loading=lazy }</br>

2. <b>Type in your 2.4 Ghz WiFI credentials and click "Connect":</b>
<br>![Type in your 2.4ghz network credentials:](/assets/ble_improv/4_improv_add_wifi_credentials.png){ width="60%" loading=lazy }</br>

3. <b>On the Sat1 HAT, press the right "Action button" to give authorization:</b>
<br>![Click action buttons](/assets/ble_improv/6_click_action_button.png){ width="60%" loading=lazy }</br>

4. <b>Tap "Continue" after successful Wifi connection:</b>
<br>![Tap "Continue" after successfull Wifi connection:](/assets/ble_improv/8_improv_successful_wifi_connection.png){ width="60%" loading=lazy }</br>

5. <b>Tap "Ok" to begin setting up ESPHome:</b>
<br>![Tap "Ok" to begin setting up ESPHome:](/assets/ble_improv/9_esphome_setup_request.png){ width="60%" loading=lazy }</br>

6. <b>Tap the name of your Sat1 device and then tap the "Submit" button:</b>
<br>![Tap the name if your Sat1 device and then tap the "Submit" button:](/assets/ble_improv/10_esphome_select_device.png){ width="60%" loading=lazy }</br>

7. <b>The Wizard will pull down the most recent Sat1 Firmware:</b>
<br>![The Wizard will pull down the most recent Sat1 Firmware:](/assets/ble_improv/12_wizard_checking_for_updates.png){ width="60%" loading=lazy }</br>

8. <b>The Wizard will ask you to say the Wake Word twice:</b>
<br>![The Wizard will ask you to say the Wake Word twice:](/assets/ble_improv/13_wizard_first_wake_word_test.png){ width="60%" loading=lazy }</br>

9. <b>Select the Area that you Sat1 belongs in:</b>
<br>![Type the Area this Sat1 falls in:](/assets/ble_improv/15_wizard_assign_area.png){ width="60%" loading=lazy }</br>

10. <b>Stick with the default or change the wake word, conversation agent, and voice:</b>
<br>![Stick with the default or change the wake word, conversation agent, and voice:](/assets/ble_improv/16_wizard_quick_pipeline_config.png){ width="60%" loading=lazy }</br>

11. <b>After completing the Wizard, do NOT click to add the Sat1 to ESPHome again.  Simply refresh and this will go away.</b>
<br>![After completing the Wizard, do NOT click to add the Sat1 to ESPHome again.  Simply refresh and this will go away.](/assets/ble_improv/17_ignore_device_discovered.png){ width="60%" loading=lazy }</br>

Congrats.  You have connected your Satellite1 to Home Assistant!

## Re-Flashing your Satellite1 via a USB-C Cable

Find the USB-C port on your Sat1 labeled "CORE/ESP32".  Plug directly into your computer with a USB-C cable that supports a data connection. Use the form below to select your preferred Sat1 firmware and then click the blue "Connect" button to begin flashing your chosen firmware:
<div class="form-container" id="firmware-selector" role="form" aria-live="polite"></div>

??? tip "NOTE: If you do not see a blue "Connect" button, be sure you are using a Google Chrome browser and have disabled any pop-up blockers and security extensions.  You can also try opening this page in an incognito window."

2. <b>After clicking the blue "Connect" button, a pop-up window will open.  Select the JTAG device in the pop-up window.</b>
<br>![Select JTAG](/assets/ESPHome-SerialConn.png){ width="60%" loading=lazy }</br>

2. <b>Click "Install":</b>
<br>![Image title](/assets/ESPHome-Install.png){ width="60%" loading=lazy }</br>

3. <b>Erase the device, then click "Next" and then "Install":</b>
<br>![Image title](/assets/ESPHome-Erase.png){ width="60%" loading=lazy }</br>
<br>![Image title](/assets/ESPHome-ConfirmInstall.png){ width="60%" loading=lazy }</br>

4. <b>Installation will complete. Click "Next":</b>
<br>![Image title](/assets/ESPHome-InstallationComplete.png){ width="60%" loading=lazy }</br>

5. <b>Select your 2.4ghz WiFi network and click "Connect".  Your device will begin sparkling blue while attempting to connect.  If you don't see your WiFi network then click the refresh icon on the top right to scan for networks again.</b>
<br>![Image title](/assets/ConfigureWifi.png){ width="60%" loading=lazy }</br>

6. <b>Congrats you're now connected to your Wifi.  Your device will now begin sparkling red.  This means it needs to be connected to ESPHome in your Home Assistant instance.</b>
<br>![Image title](/assets/ESPHome-WiFiConnected.png){ width="60%" loading=lazy }</br>

7. <b>Inside Home Assistant, go to "Settings -> Devices & Services" and notice you have a Discovered `Satellite1 xxxxxx' device.  Click add and follow the onboarding steps.</b>
<br>![Image title](/assets/discovered_sat1.png){ width="60%" loading=lazy }</br>

Congrats.  You have re-flashed your Sat1 and connected it to Home Assistant.


## Understanding the ESPHome User Interface
Once your Sat1 is connected to Home Assistant you should familiarize yourself with all the server-side settings you may want to change:

1. <b>Inside your Home Assistant, head over to "Settings -> Devices & Services -> ESPHome" and click on your Sat1 device:</b>
  <br>![esphome device list](/assets/esphome/1_esphome_device_list.png){ width="60%" loading=lazy }</br>

  2. <b>Understand all the features of your Sat1 device:</b>
  <br>![top esphome device](/assets/esphome/2_esphome_top_page.png){ width="60%" loading=lazy }</br>
  <br>![top esphome device](/assets/esphome/3_esphome_bottom_page.png){ width="60%" loading=lazy }</br>