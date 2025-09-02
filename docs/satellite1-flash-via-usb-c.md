!!! warning "Flashing your Satellite1 will erase all data on the device, and optionally your WiFi credentials setting it back to factory settings.  I will not remove the Satellite1 from your Home Assistant server instance."

## Flash your Satellite1 via USB-C Cable

1. Use a data-capable USB-C cable and connect it directly to your computer.
2. If the CORE is mounted to the HAT, plug into the HAT’s “CORE/ESP32” USB-C port. Otherwise, use the CORE’s USB-C port.
3. Use the form below to flash Production or Beta firmware, with or without mmWave.

!!! example ""
    <div class="form-container" id="firmware-selector" role="form" aria-live="polite"></div>

<div class="grid cards" markdown>

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
    Check **Erase the device** if you want to remove saved WiFi credentials, then click **"Next"** and **"Install"**.

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