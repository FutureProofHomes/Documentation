## Connect to Home Assistant Wirelessly via BLE Improv
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
