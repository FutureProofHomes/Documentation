The built-in **Radar Tuner WebUI** lets you visually calibrate your mmWave sensor from a web browser. You do not need Home Assistant dashboard cards or manual entity tuning.

!!! note "Install first"

    Your sensor needs to be [connected and detected](satellite1-mmwave-installation.md) before it will appear in the tuner. LD2450 owners should also confirm the [radar firmware is up to date](satellite1-mmwave-installation.md#updating-the-radar-firmware).

## Opening the Radar Tuner

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Open Sat1 ESPHome Device UI__

    ---

    ![Radar Tuner WebUI toggle](/assets/presence-sensors/mmwave_radar_tuner_toggle.png){ loading=lazy }
    With a mmWave attached to your Satellite1, go to **"Settings -> Devices & Services -> ESPHome"** and find your Sat1 device.

    Toggle on **"Radar Tuner WebUI"** within the "Diagnostics" section.

-   :material-numeric-2-circle:{ .lg .middle } __Open the Radar Tuner WebUI__

    ---

    ![Visit Radar Tuner WebUI](/assets/presence-sensors/visit_radar_tuner_webUI.png){ loading=lazy }
    Open a web browser and navigate to your **Sat1's IP address** (for example, `http://192.168.1.xxx`), or click the **Visit** button in the Device Info section.

</div>

## Tuning LD2450 Zones

The LD2450 tuner lets you draw **up to 3 detection zones** plus an **exclusion zone** on a visual radar map. Click the canvas to add points and define each zone boundary. This gives you precise control over where presence is detected.

![Satellite1 Radar Tuner — LD2450](/assets/presence-sensors/radar_tuner_ld2450.png){ width="100%" loading=lazy }

- **Zone 1 / Zone 2 / Zone 3**: Define areas where you want presence detection active. Left click to add points, right click to remove them. Click to move the shape around the screen.
- **Exclusion Zone**: Mark areas to ignore, such as a fan or a window with moving curtains.
- Adjust **Max Detection Range**, **Timeout**, **Stability**, and **Multi-Target Tracking** from the right-hand panel. Read the info popups.
- Click **"Save Zone"** after defining each zone, or **"Save All Zones"** to write the configuration to the sensor. This requires rebooting your Sat1.

After tuning, the relevant presence sensors and states will appear in your Sat1's ESPHome Device UI, ready for use in Home Assistant automations.

![Satellite1 Radar Tuner — sensors](/assets/presence-sensors/mmwave_esphome_sensors.png){ width="100%" loading=lazy }

## Tuning LD2410 Gates

The LD2410 tuner provides a visual **gate energy chart** where you can see real-time moving and still energy levels for all 9 gates and adjust thresholds by dragging the dashed lines.

![Satellite1 Radar Tuner — LD2410](/assets/presence-sensors/radar_tuner_ld2410.png){ width="100%" loading=lazy }

- **Blue bars** = Moving energy per gate. **Green bars** = Still energy per gate.
- **Dashed lines** = Thresholds (drag up or down to adjust).
- Set **Max Moving Gate** and **Max Still Gate** to restrict detection range.
- Adjust the **Timeout** and **Distance Resolution** as needed.
- Click **"Save All"** to write changes to the sensor.

After tuning, the relevant presence sensors and states will appear in your Sat1's ESPHome Device UI, ready for use in Home Assistant automations.

Not sure what gates, zones, or energy mean? See [Understanding the LD2410 and LD2450](satellite1-mmwave-overview.md#understanding-the-ld2410).
