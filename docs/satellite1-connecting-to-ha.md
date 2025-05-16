## Connecting to Home Assistant
Your Satellite1 arrives pre-flashed from the factory and will boot into BLE improv mode with white sparkling LEDs.  Follow the steps below to connect to Home Assistnat via Bluetooth.

<div class="grid cards" markdown>
-   :material-numeric-1-circle:{ .lg .middle } __Open Home Assistant App__

    ---

    ![Tap "Add" next to your Sat1 device (contains last 6 of device MAC address):](/assets/ble_improv/3_improv_discovered_device.png){ loading=lazy }
    Open Home Assistant on your **iPhone** or **Android** device with Bluetooth enabled. Navigate to "Settings -> Devices & Services" and tap "Add" next to your discovered Sat1 device.

-   :material-numeric-2-circle:{ .lg .middle } __Configure WiFi credentials__

    ---

    ![Type in your 2.4ghz network credentials:](/assets/ble_improv/4_improv_add_wifi_credentials.png){ loading=lazy }
    Type in your **2.4 Ghz WiFI** credentials and click **"Connect"**.

-   :material-numeric-3-circle:{ .lg .middle } __Authorize the WiFi connection__

    ---

    ![Click action buttons](/assets/ble_improv/6_click_action_button.png){ loading=lazy }
    On the **Sat1 HAT**, press the right **"Action button"** to give authorization.

-   :material-numeric-4-circle:{ .lg .middle } __Continue to next steps__

    ---

    ![Tap "Continue" after successfull Wifi connection:](/assets/ble_improv/8_improv_successful_wifi_connection.png){ loading=lazy }
    Tap **"Continue"** after successful Wifi connection.

-   :material-numeric-5-circle:{ .lg .middle } __Add the Sat1 to ESPHome__

    ---

    ![Tap "Ok" to begin setting up ESPHome:](/assets/ble_improv/9_esphome_setup_request.png){ loading=lazy }
    Tap **"Ok"** to begin setting up **ESPHome**.

-   :material-numeric-6-circle:{ .lg .middle } __Select Sat1 device to add__

    ---

    ![Tap the name if your Sat1 device and then tap the "Submit" button:](/assets/ble_improv/10_esphome_select_device.png){ loading=lazy }
    Tap the name of your **Sat1** device and then tap the **"Submit"** button.

-   :material-numeric-7-circle:{ .lg .middle } __Checking updates__

    ---

    ![The Wizard will pull down the most recent Sat1 Firmware:](/assets/ble_improv/12_wizard_checking_for_updates.png){ loading=lazy }
    The **Wizard** will pull down the most recent **Sat1** Firmware.

-   :material-numeric-8-circle:{ .lg .middle } __Test Wake Word detection__

    ---

    ![The Wizard will ask you to say the Wake Word twice:](/assets/ble_improv/13_wizard_first_wake_word_test.png){ loading=lazy }
    The **Wizard** will ask you to say the **Wake Word** twice.

-   :material-numeric-9-circle:{ .lg .middle } __Select Area__

    ---

    ![Type the Area this Sat1 falls in:](/assets/ble_improv/15_wizard_assign_area.png){ loading=lazy }
    Select the **Area** that you **Sat1** belongs in.

-   :material-numeric-10-circle:{ .lg .middle } __Configure Sat1__

    ---

    ![Stick with the default or change the wake word, conversation agent, and voice:](/assets/ble_improv/16_wizard_quick_pipeline_config.png){ loading=lazy }
    Stick with the default or change the **Wake word**, **Assistant**, and **Voice**.
</div>

!!! success
    You have connected your **Satellite1** to **Home Assistant**!

!!! warning
    ![After completing the Wizard, do NOT click to add the Sat1 to ESPHome again.  Simply refresh and this will go away.](/assets/ble_improv/17_ignore_device_discovered_cut.png){ width="40%" align=left loading=lazy }
    After completing the **Wizard**, **do NOT click** to add the Sat1 to ESPHome again.  Simply refresh and this will go away.

## Re-Flashing your Satellite1 via a USB-C Cable

Find the USB-C port on your Sat1 labeled "CORE/ESP32".  Plug directly into your computer with a USB-C cable that supports a data connection. Use the form below to select your preferred Sat1 firmware and then click the blue "Connect" button to begin flashing your chosen firmware:

!!! example ""
    <div class="form-container" id="firmware-selector" role="form" aria-live="polite"></div>

<div class="next-steps grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Select the JTAG device__

    ---

    ![Select JTAG](/assets/ESPHome-SerialConn.png){ loading=lazy }
    After clicking the blue **"Connect"** button, a pop-up window will open.  Select the **JTAG device** in the pop-up window.

-   :material-numeric-2-circle:{ .lg .middle } __Start Firmware installation__

    ---

    ![Image title](/assets/ESPHome-Install.png){ loading=lazy }
    Click **"Install"**.

-   :material-numeric-3-circle:{ .lg .middle } __Erase the device__

    ---

    ![Image title](/assets/ESPHome-Erase.png){ loading=lazy }
    ![Image title](/assets/ESPHome-ConfirmInstall.png){ loading=lazy }
    Select **Erase the device** checkbox, then click **"Next"** and then **"Install"**.

-   :material-numeric-4-circle:{ .lg .middle } __Installation completed__

    ---

    ![Image title](/assets/ESPHome-InstallationComplete.png){ loading=lazy }
    Installation will complete. Click **"Next"**.

-   :material-numeric-5-circle:{ .lg .middle } __Configure WiFi__

    ---

    ![Image title](/assets/ConfigureWifi.png){ loading=lazy }
    Select your **2.4ghz WiFi** network and click **"Connect"**.  Your **Sat1** device will begin sparkling blue while attempting to connect. If you don't see your WiFi network then click the **refresh icon** on the top right to scan for networks again.

-   :material-numeric-6-circle:{ .lg .middle } __Connected to WiFi__

    ---

    ![Image title](/assets/ESPHome-WiFiConnected.png){ loading=lazy }
    Congrats you're now connected to your Wifi! Your device will now begin sparkling red. This means it needs to be connected to **ESPHome** in your **Home Assistant** instance.

-   :material-numeric-7-circle:{ .lg .middle } __Start ESP Onboarding__

    ---

    ![Image title](/assets/discovered_sat1.png){ loading=lazy }
    Inside **Home Assistant**, go to **"Settings -> Devices & Services"** and notice you have a Discovered **`Satellite1 xxxxxx`** device. Click **ADD** and follow the **ESPHome** onboarding steps.
</div>

<div class="next-steps" markdown>
!!! success
    You have re-flashed your **Sat1** and connected it to **Home Assistant**.
</div>

## Understanding the ESPHome User Interface
Once your **Sat1** is connected to **Home Assistant** you should familiarize yourself with all the server-side settings you may want to change:

<div class="grid cards" markdown>
-   :material-numeric-1-circle:{ .lg .middle } __Select Sat1 device from list__

    ---

    ![esphome device list](/assets/esphome/1_esphome_device_list.png){ loading=lazy }
    Inside your **Home Assistant**, head over to **"Settings -> Devices & Services -> ESPHome"** and click on your **Sat1** device.
</div>
<div class="grid cards" markdown>
-   :material-numeric-2-circle:{ .lg .middle } __Explore Sat1 settings__

    ---

    ![top esphome device](/assets/esphome/2_esphome_top_page.png){ loading=lazy }
    ![top esphome device](/assets/esphome/3_esphome_bottom_page.png){ loading=lazy }
    Understand all the features of your **Sat1** device.
</div>
