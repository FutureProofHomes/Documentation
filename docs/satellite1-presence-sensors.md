## Connecting mmWave Sensors

Satellite1 supports mmWave radar sensors for detecting human presence in a room. This is useful when you want Sat1 to automate actions like turning on a light or starting a conversation when someone enters.

The Sat1 HAT has headers for directly mounting either the LD2410 or LD2450 mmWave human presence sensor. Direct mounting is typically best for in-ceiling installations because the sensor points in the same direction as the LEDs and microphones.

The latest Satellite1.1 HAT also includes an LD2450 connector on the underside of the board. This lets you mount the sensor in any orientation with a 4-pin JST-ZH cable.

<div class="grid cards" markdown>

-  :material-numeric-1-circle:{ .lg .middle } __LD2410 mmWave module__

    ---
    
    The LD2410 is a small but capable presence sensor. It detects both motion and still human presence up to 6 meters away, with a detection angle of +/-60 degrees. For best results, tune it after installation. It can also detect through materials like glass walls and thin plywood.

    <figure markdown="span">
      ![LD2410 mmWave](../assets/presence-sensors/sat1_ld2410.jpg){ loading=lazy}
      <figcaption>Original Sat1 with direct-mounted LD2410</figcaption>
    </figure>
    

    ???+ warning "The LD2410B includes Bluetooth for updating the radar firmware. The standard LD2410 does not include Bluetooth. Sat1 is compatible with both versions."
    [Get LD2410 on Amazon](https://amzn.to/3C6utsf){ .md-button .md-button--primary }
    
-   :material-numeric-2-circle:{ .lg .middle } __LD2450 mmWave module__

    ---

    The LD2450 is a more advanced presence sensor. It can track up to 3 moving occupants while also detecting still human presence up to 8 meters away. It has a detection angle of +/-60 degrees and can detect through materials like glass walls and thin plywood.

    <figure markdown="span">
      ![LD2450 mmWave](../assets/presence-sensors/sat1_ld2450.jpg){ loading=lazy}
      <figcaption>Original Sat1 with direct-mounted LD2450</figcaption>
    </figure>
    <figure markdown="span">
      ![LD2450 4-pin mmWave](../assets/presence-sensors/sat1.1_ld2450_square.png){ loading=lazy}
      <figcaption>Latest Sat1.1 supports LD2450 connected with the included cable</figcaption>
    </figure>

    ???+ warning "The LD2450 must be running firmware version V2.02.23090617 to work with ESPHome. Learn how to [update the firmware](#updating-mmwave-radar-sensor)."
    [Get LD2450 and Cable](https://futureproofhomes.net/products/ld2450-mmwave-human-presence-sensor){ .md-button .md-button--primary }
</div>

???+ "Not all enclosures support mmWave"

    Only some Satellite1 enclosures support mmWave sensors.

    1. Our new [Sat1.1 Smart Speaker](https://futureproofhomes.net/products/satellite1-smart-speaker) fits the LD2450 using a 4-pin cable.
    2. Our older DIY [Cylindrical Enclosure](satellite1-cylindrical-enclosure.md) fits both mmWave sensors when mounted directly to the HAT.
    3. In-ceiling enclosures are coming soon.

---

## Understanding the LD2410

  1. **Gate**: the LD2410 divides its detection range into distance bands called gates. Each gate can be tuned separately. Think of the gates like layers extending outward from the sensor. The LD2410 has 8 useful gates, plus gate 0, which is usually not helpful for tuning.

  2. **Distance Resolution**: distance resolution controls the size of each gate. The LD2410 can use 75 cm or 20 cm per gate. At 75 cm per gate, the maximum range is `0.75 * 8 =` 6 meters. At 20 cm per gate, the maximum range is 1.6 meters, but tuning can be more precise.

  3. **Energy**: energy is the amount of detected activity in a gate. More movement usually creates a higher energy value.

## Understanding the LD2450

  1. **Target Tracking**: unlike the gate-based LD2410, the LD2450 tracks up to 3 individual targets at the same time using X/Y coordinates. Each target reports its position, distance, speed, and direction, giving you a real-time map of where occupants are in the room.

  2. **Zones**: you can define up to 3 zones on the coordinate grid. When a target enters a zone, that zone's occupancy sensor turns on. You can also define an exclusion zone to ignore motion from areas like a ceiling fan or a window with moving curtains.

## mmWave Setup

=== "Stable"

    ### Flash the mmWave Firmware
    First, flash the appropriate mmWave firmware to Satellite1 using a USB-C cable.

    [Flash the appropriate mmWave firmware](satellite1-flash-via-usb-c.md#re-flashing-your-satellite1-via-a-usb-c-cablef){ .md-button .md-button--primary }

    ### LD2450 Zone Mapper

    #### ESPHome LD2450 Entities

    After installation, several new LD2450 entities appear in Home Assistant. These are the key ones to know:

    1. Binary sensors:
        1. **Presence** — the main presence sensor. It turns on when any still or moving target is detected, then follows the **Timeout** cooldown before switching off.
        2. **Moving Target** — true when at least one target is actively moving.
        3. **Still Target** — true when a stationary target is detected.
    2. Sensors (global):
        1. **Target Count** — total number of targets currently detected (0–3).
        2. **Still Target Count** / **Moving Target Count** — target-count breakdowns by motion state.
    3. Sensors (per target, targets 1–3):
        1. **X** / **Y** — the target's position in mm on the coordinate grid.
        2. **Distance** — straight-line distance from the sensor to the target in mm.
        3. **Angle** — angle in degrees relative to the sensor's center line.
        4. **Speed** — target velocity in mm/s (positive = moving away, negative = approaching).
        5. **Resolution** — the sensor's detection range resolution in mm.
    4. Sensors (per zone, zones 1–3):
        1. **Target Count** / **Still Target Count** / **Moving Target Count** — same as the global counters, but scoped to a specific zone.
    5. Text sensors:
        1. **Firmware Version** — the LD2450 firmware currently running.
        2. **BT MAC** — the sensor's Bluetooth MAC address.
        3. **Direction** (per target) — a human-readable label: `Stationary`, `Approaching`, `Moving away`, or `NA`.
    6. Switches:
        1. **Bluetooth** — enables the sensor's built-in Bluetooth so you can connect with the HLKRadarTool app (useful for firmware updates).
        2. **Multi Target Tracking** — toggles between tracking a single target and tracking up to 3 targets.
    7. Numbers:
        1. **Timeout** — cooldown period in seconds. After the last target disappears, the **Presence** binary sensor stays "on" for this duration before switching off. Default is 5 seconds.
        2. **Zone 1/2/3 X1, Y1, X2, Y2** — the corner coordinates (in mm) that define each rectangular zone.
    8. Buttons:
        1. **Restart** — reboots the LD2450 module.
        2. **Factory Reset** — restores the sensor to its default configuration.

    #### Installing Zone Mapper

    We recommend **[Zone Mapper](https://github.com/ApolloAutomation/zone-mapper)**, a free, open-source Home Assistant integration and dashboard card. It lets you draw detection zones on a radar map instead of manually entering coordinates. It works with any mmWave sensor that reports X/Y coordinates, including the LD2450.

    <iframe style="width: 100%; aspect-ratio: 16 / 9;" src="https://www.youtube.com/embed/lal0_o5qgpA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

    1. Make sure [HACS](https://hacs.xyz/) is installed in your Home Assistant instance.
    2. In HACS, click the **three dots** (upper right) → **Custom repositories**.
    3. Add `https://github.com/ApolloAutomation/zone-mapper` as type **Integration**.
    4. Add `https://github.com/ApolloAutomation/zone-mapper-card` as type **Dashboard**.
    5. Search for **Zone Mapper** in HACS and download both the integration and the card.
    6. Restart Home Assistant.
    7. Go to **Settings → Devices and Services → Add Integration** and search for **Zone Mapper**.

    After setup, a new **"Zone Mapper"** view is automatically added to your default dashboard.

    #### Using Zone Mapper

    1. Open the **Zone Mapper** view on your dashboard.
    2. Select your Sat1 device and pick the LD2450 **X/Y target entities** you want to track.
    3. **Draw zones** directly on the visual radar map: rectangles, ellipses, or freeform polygons with up to 32 points. You can create multiple zones and name them, such as "Desk", "Doorway", or "Bed".
    4. Use the **rotation** control to align the radar's orientation with your room layout.
    5. Each zone automatically creates an **occupancy binary sensor** in Home Assistant. That sensor turns on when a tracked target is inside the zone, making it ready for automations.

    ### LD2410 Custom UI Tuner Card

    #### ESPHome LD2410 Entities

    After installation, the LD2410 exposes several entities in Home Assistant. These are the main ones to know:

    1. Binary sensors:
        1. **Moving Target** - turns on when the sensor detects movement.
        2. **Still Target** - turns on when the sensor detects stationary presence.
        3. **Presence** - the main presence sensor. It combines moving and still detection, then follows the **Timeout** cooldown before switching off.
    2. Sensors:
        1. **Moving/still distance** - distance to the corresponding moving or still target.
        2. **G(1-8) moving/still energy** - energy values for each moving or still gate.
    3. Switches:
        1. **Engineering Mode** - enables fine-tuning and reports each gate's readings in real time. Leave it off when you are not tuning the sensor because it generates extra data.
        2. **Control Bluetooth** - enables the sensor's built-in Bluetooth so you can connect with the HLKRadarTool app. This is useful for firmware updates.
    4. Select:
        1. **Distance Resolution** - sets each gate to either 0.75 m or 0.2 m.
    5. Numbers:
        1. **Timeout** - sets the cooldown period between the last detected presence event and the main presence sensor switching off.
        2. **Max Moving/Still Distance Gate** - limits detection to a specific distance. For example, if this is set to 6 and distance resolution is 0.75 m, the maximum detection distance is 4.5 meters.
        3. **G(1-8) Moving/Still Threshold** - sets the presence threshold for each gate. If a gate's energy is higher than its threshold, the sensor reports presence in that gate.

    #### Installing Custom UI Tuner Card

    We built a custom UI card to make calibration easier.
    <br>![LD2410 Dashboard](/assets/ld2410_calibration_card.png){ width="100%" loading=lazy }</br>

    1. Install [Mushroom cards](https://github.com/piitaya/lovelace-mushroom), [Auto-entities card](https://github.com/thomasloven/lovelace-auto-entities), [Decluttering card](https://github.com/custom-cards/decluttering-card), [Vertical Stack In Card](https://github.com/ofekashery/vertical-stack-in-card), and [Bar card](https://github.com/custom-cards/bar-card) from HACS.
    2. Add this to the bottom of your dashboard YAML in raw edit mode. You only need to do this once per dashboard:

        ```yaml
        decluttering_templates:
          ld2410:
            card:
              type: horizontal-stack
              cards:
                - type: custom:vertical-stack-in-card
                  cards:
                    - type: custom:mushroom-entity-card
                      entity: switch.[[device]]_engineering_mode
                      name: Preset edit mode
                      icon_color: pink
                      layout: horizontal
                      tap_action:
                        action: toggle
                      hold_action:
                        action: more-info
                      double_tap_action:
                        action: none
                    - type: custom:mushroom-number-card
                      entity: number.[[device]]_timeout
                      name: Detection cooldown
                      layout: horizontal
                      display_mode: buttons
                    - type: custom:mushroom-select-card
                      entity: select.[[device]]_distance_resolution
                      name: Gate resolution
                      icon_color: green
                      layout: horizontal
                    - type: custom:mushroom-entity-card
                      entity: switch.[[device]]_control_bluetooth
                      icon_color: indigo
                      name: Bluetooth
                      tap_action:
                        action: toggle
                      hold_action:
                        action: more-info
                      double_tap_action:
                        action: none
                    - type: custom:mushroom-template-card
                      secondary: >-
                        {{ iif(is_state(entity, 'on'), 'Detected, ' +
                        states('sensor.[[device]]_still_distance') + ' cm', 'Not
                        detected') }}
                      primary: 'Still presence'
                      icon: mdi:motion-sensor
                      entity: binary_sensor.[[device]]_still_target
                      icon_color: '{% if(is_state(entity, "on")) %} red {% endif %}'
                      layout: horizontal
                      multiline_secondary: false
                    - type: custom:mushroom-template-card
                      secondary: >-
                        {{ iif(is_state(entity, 'on'), 'Detected, ' +
                        states('sensor.[[device]]_moving_distance') + ' cm', 'Not
                        detected') }}
                      primary: 'Moving presence'
                      icon: mdi:motion-sensor
                      entity: binary_sensor.[[device]]_moving_target
                      icon_color: '{% if(is_state(entity, "on")) %} red {% endif %}'
                      layout: horizontal
                      multiline_secondary: false
                  title: 'Settings: common'
                - type: custom:decluttering-card
                  template: ld2410_gates
                  variables:
                    - device: '[[device]]'
                    - type: still
                - type: custom:decluttering-card
                  template: ld2410_gates
                  variables:
                    - device: '[[device]]'
                    - type: moving
          ld2410_gates:
            card:
              type: custom:auto-entities
              filter:
                template: >-
                  [ 
                  {{
                  dict(
                    type='custom:mushroom-number-card',
                    entity='number.[[device]]_max_[[type]]_distance_gate',
                    name='Max detection gate',
                    display_mode='buttons',
                    icon='mdi:tape-measure',
                    layout='horizontal',
                    secondary_info='none',
                    icon_color='green',
                  )
                  }},
                  {% for i in [0, 1, 2, 3, 4, 5, 6, 7, 8] %}  {{
                  dict(
                    type='custom:mushroom-number-card',
                    entity='number.[[device]]_g' + i|string + '_[[type]]_threshold',
                    display_mode='slider',
                    icon_type='none',
                    primary_info='name',
                    secondary_info='state',
                    name='Gate ' + i|string,
                    card_mod={
                      'style':
                        {
                          'mushroom-number-value-control$': {
                             'mushroom-slider$': '.slider { height: 24px !important;}'
                          },
                          '.':'mushroom-number-value-control {height: 24px;}'
                        }
                    }
                  )
                  }},
                  {{
                  dict(
                    type='custom:bar-card',
                    direction='right',
                    columns=1,
                    height=16,
                    positions=dict(
                      indicator='off',
                      icon='off',
                      name='off',
                    ),
                    entities=[
                        {
                          'entity': 'sensor.[[device]]_g' + i|string + '_[[type]]_energy',
                          'color': 'orange'
                        }
                      ]
                  )
                  }},
                  {% endfor %}
                  ]
              card_param: cards
              card:
                type: custom:vertical-stack-in-card
                title: 'Gates: [[type]]'
        ```

    3. Add the following card to your dashboard. Replace the `device` value with your Satellite1 name as it appears in entity IDs, such as `satellite1_92fb28`.

        ```yaml
        type: custom:decluttering-card
        template: ld2410
        variables:
            - device: satellite1_9a72b3
        ```

    #### Using Custom UI Tuner Card

    1. Blue bars are threshold sliders. Orange bars are energy indicators. Place the sensor where its 120-degree detection area covers the useful parts of the room while avoiding as much unwanted movement as possible.

    2. Turn on the **Engineering Mode** switch.

    3. Set the maximum gate based on the room length. If you are not sure which gate to use, move near the far edge of the room, check which gate detects movement, and use that value for **Max Moving/Still Distance Gate**. It is fine to set the threshold slightly higher because energy values can jump.
    4. Finally, calibrate for an empty room. Step out, let the readings settle for about a minute, then adjust the moving and still thresholds so they are higher than the energy levels for the corresponding gates.

=== "Beta"

    ### mmWave Sensors Are Automatically Detected

    The latest firmware automatically detects if/which mmWave sensor is connected to your Sat1. To confirm detection, open your Sat1's **Diagnostics** section and scroll to the bottom to see which radar is listed.

    !!! WARNING "BREAKING CHANGE: Sat1 mmWave Entites Have Changed "

        Your previous Sat1 mmWave automations may break due to new/different radar entities being exposed to the Sat1 ESPHome UI.

    ### Radar Tuner WebUI

    The built-in **Radar Tuner WebUI** lets you visually calibrate your mmWave sensor from a web browser. You do not need Home Assistant dashboard cards or manual entity tuning.

    <div class="grid cards" markdown>

    -   :material-numeric-1-circle:{ .lg .middle } __Open Sat1 ESPHome Device UI__

        ---

        ![Image title](../assets/presence-sensors/mmwave_radar_tuner_toggle.png){ loading=lazy }
        With a mmWave attached your Satellite1, go to **"Settings -> Devices & Services -> ESPHome"** and find your Sat1 device 
        
        Toggle on **"Radar Tuner WebUI"** within the "Diagnostics" section.

    -   :material-numeric-2-circle:{ .lg .middle } __Open the Radar Tuner WebUI__

        ---

        ![Image title](../assets/presence-sensors/visit_radar_tuner_webUI.png){ loading=lazy }
        Open a web browser and navigate to your **Sat1's IP address** (for example, `http://192.168.1.xxx`), or click the **Visit** button in the Device Info section.

    </div>

    #### Tuning LD2450 Zones

    The LD2450 tuner lets you draw **up to 3 detection zones** plus an **exclusion zone** on a visual radar map. Click the canvas to add points and define each zone boundary. This gives you precise control over where presence is detected.

    ![Satellite1 Radar Tuner — LD2450](/assets/presence-sensors/radar_tuner_ld2450.png){ width="100%" loading=lazy }

    - **Zone 1 / Zone 2 / Zone 3**: Define areas where you want presence detection active.  Left click to add points, right click to remove them.  Click to move the shape around the screen.
    - **Exclusion Zone**: Mark areas to ignore, such as a fan or a window with moving curtains.
    - Adjust **Max Detection Range**, **Timeout**, **Stability**, and **Multi-Target Tracking** from the right-hand panel.  Read the info popups.
    - Click **"Save Zone"** after defining each zone, or **"Save All Zones"** to write the configuration to the sensor.  This will require to you reboot your Sat1.

    After tuning, the relevant presence sensors and states will appear in your Sat1's ESPHome Device UI, ready for use in Home Assistant automations.

    ![Satellite1 Radar Tuner — LD2450](/assets/presence-sensors/mmwave_esphome_sensors.png){ width="100%" loading=lazy }

    #### Tuning LD2410 Gates

    The LD2410 tuner provides a visual **gate energy chart** where you can see real-time moving and still energy levels for all 9 gates and adjust thresholds by dragging the dashed lines.

    ![Satellite1 Radar Tuner — LD2410](/assets/presence-sensors/radar_tuner_ld2410.png){ width="100%" loading=lazy }

    - **Blue bars** = Moving energy per gate. **Green bars** = Still energy per gate.
    - **Dashed lines** = Thresholds (drag up or down to adjust).
    - Set **Max Moving Gate** and **Max Still Gate** to restrict detection range.
    - Adjust the **Timeout** and **Distance Resolution** as needed.
    - Click **"Save All"** to write changes to the sensor.

    After tuning, the relevant presence sensors and states will appear in your Sat1's ESPHome Device UI, ready for use in Home Assistant automations.

---

## Updating mmWave Radar Sensor
Both the LD2410 and LD2450 can be updated over Bluetooth with the HLKRadarTool mobile app. Download the app, then watch the quick video below to learn how to access the sensor and change the firmware version.

<div style="display: flex; align-items: center; gap: 8px; margin: 1em 0;">
  <a href="https://apps.apple.com/us/app/hlkradartool/id1638651152">
    <img style="height: 44px;" src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg" alt="Download on the App Store"/>
  </a>
  <a href="https://play.google.com/store/apps/details?id=com.hlk.hlkradartool&hl=en_US&pli=1">
    <img style="height: 64px;" src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" alt="Get it on Google Play"/>
  </a>
</div>

<iframe style="width: 100%; aspect-ratio: 16 / 9;" src="https://www.youtube.com/embed/t8-JdVVVH34?si=3HRSFepdfceSfEtx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
