## Connecting mmWave Sensors

The Satellite1 supports connecting mmWave radar sensors to detect human presence in the room.  This is handy if you'd like the Sat1 to automate turning on the light or to starting a conversation when an occupant enters the room.

The Sat1 HAT has headers for directly mounting either the LD2410 or LD2450 mmWave human presence sensors. Direct mounting is typically used for in-ceiling installations, since the sensor will point the same direction as the LEDs and microphones.

The latest Satellite1.1 HAT also adds an additional LD2450 connector on the underside of the board. This allows the sensor to be mounted in any orientation using a 4-pin JST-ZH cable.

<div class="grid cards" markdown>

-  :material-numeric-1-circle:{ .lg .middle } __LD2410 mmWave module__

    ---
    
    This is small, but powerful sensor. It can sense motion and still human presence for distances up to 6 meters. It has a detection angle +/-60 degrees, and should be fine-tuned for best performance. Also it can see through glass walls, thin plywood etc.

    <figure markdown="span">
      ![LD2410 mmWave](../assets/presence-sensors/sat1_ld2410.jpg){ loading=lazy}
      <figcaption>Original Sat1 with direct mounted LD2410</figcaption>
    </figure>
    

    ???+ warning "The LD2410(B) has bluetooth capabilities which helps update the radar's firmware, while the standard LD2410 does not have bluetooth.  The Sat1 is compatible with both."
    [Get LD2410 on Amazon](https://amzn.to/3C6utsf){ .md-button .md-button--primary }
    
-   :material-numeric-2-circle:{ .lg .middle } __LD2450 mmWave module__

    ---

    This is more powerful presence sensor. It can track the motion for 3 moving occupants in the room while also detecting still human presence for distances up to 8 meters. It has a detection angle +/-60 degrees and can also see through glass walls, thin plywood etc.

    <figure markdown="span">
      ![LD2450 mmWave](../assets/presence-sensors/sat1_ld2450.jpg){ loading=lazy}
      <figcaption>Original Sat1 with direct mounted LD2450</figcaption>
    </figure>
    <figure markdown="span">
      ![LD2450 4-pin mmWave](../assets/presence-sensors/sat1.1_ld2450_square.png){ loading=lazy}
      <figcaption>Latest Sat1.1 supports LD2450 connected via included cable</figcaption>
    </figure>

    ???+ warning "The LD2450 must be running firmware version V2.02.23090617 to work with ESPHome.  Learn how to [update the firmware by reading here](#updating-mmwave-radar-sensor)."
    [Get LD2450 and Cable](https://futureproofhomes.net/products/ld2450-mmwave-human-presence-sensor){ .md-button .md-button--primary }
</div>

???+ "Not all enclosures support mmWave"

    Only some of our enclosures accomodate a mmWave Sensor.

    1. Our new [Sat1.1 Smart Speaker](https://futureproofhomes.net/products/satellite1-smart-speaker) fits the LD2450 via the a 4-pin cable.
    2. Our older DIY [Cylindrical Enclosure](satellite1-cylindrical-enclosure.md) fits both mmWave sensors mounted directly to the Hat.
    3. In-Ceiling enclosures coming soon..

---

## Understanding the LD2410

  1. **Gate**: these sensors use a "gate" as definition of distance range. This is some range of distance, which can be tuned separately from others. Think of it as an "onion" layer, with center on sensor. There are 8 gates on LD2410 (plus gate 0, but it's effectively useless).

  2. **Distance Resolution**: the "thickness" of one gate. The LD2410 can have resolution of 75cm or 20cm per gate. With resolution of 75cm per gate, maximum distance is `0.75 * 8 =` 6 meters (sorry my Imperial-units-friends), while with 20cm it's 1.6 meters. But with latter you can achieve much better precision.

  3. **Energy**: basically "amount of presence" in the gate. The more actively you're moving—the more energy there will be.

## Understanding the LD2450

  1. **Target Tracking**: unlike the gate-based LD2410, the LD2450 tracks up to 3 individual targets simultaneously using X/Y coordinates. Each target reports its own position, distance, speed, and direction—giving you a real-time spatial map of occupants.

  2. **Zones**: You can define up to 3 geometric zones on the coordinate grid. Targets inside a zone trigger that zone's occupancy sensor.  You can also define "exclusion" zones to ignore targets inside the zone, e.g. a ceiling fan or a window with moving curtains

## mmWave Setup

=== "Stable"

    ### Flash the Appropriate mmWave Firmware 
    First, make sure you have flashed the appropriate mmWave firmware to the Satellite1 using a USB-C cable.

    [Flash your appropriate mmWave firmware](satellite1-flash-via-usb-c.md#re-flashing-your-satellite1-via-a-usb-c-cablef){ .md-button .md-button--primary }

=== "Beta"

    ### mmWave Sensors are Automatically Detected

    Our latest firmware will automatically detect if a mmWave is connected to your Sat1. Scroll to the bottom of your Sat1's Diagnostics section and see which radar is detected.

## Tuning LD2450 Zones

=== "Stable"

    ### ESPHome LD2450 Entities

    Don't be overwhelmed with the new entities that appear after installation. Let's familiarize ourselves with the key ones:

    1. Binary sensors:
        1. **Presence** — main presence sensor. True if any target (still or moving) is detected. Respects the **Timeout** cooldown before switching off.
        2. **Moving Target** — true when at least one target is actively moving.
        3. **Still Target** — true when a stationary target is detected.
    2. Sensors (global):
        1. **Target Count** — total number of targets currently detected (0–3).
        2. **Still Target Count** / **Moving Target Count** — breakdowns of the above by motion state.
    3. Sensors (per target, targets 1–3):
        1. **X** / **Y** — the target's position in mm on the coordinate grid described above.
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

    ### Installing Zone Mapper

    We recommend using the **[Zone Mapper](https://github.com/ApolloAutomation/zone-mapper)** — a free, open-source Home Assistant integration and dashboard card that lets you visually draw detection zones on a radar map instead of manually punching in coordinate numbers. It works with any mmWave sensor that reports X/Y coordinates, including the LD2450.

    <iframe style="width: 100%; aspect-ratio: 16 / 9;" src="https://www.youtube.com/embed/lal0_o5qgpA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

    1. Make sure [HACS](https://hacs.xyz/) is installed in your Home Assistant instance.
    2. In HACS, click the **three dots** (upper right) → **Custom repositories**.
    3. Add `https://github.com/ApolloAutomation/zone-mapper` as type **Integration**.
    4. Add `https://github.com/ApolloAutomation/zone-mapper-card` as type **Dashboard**.
    5. Search for **Zone Mapper** in HACS and download both the integration and the card.
    6. Restart Home Assistant.
    7. Go to **Settings → Devices and Services → Add Integration** and search for **Zone Mapper**.

    After setup, a new **"Zone Mapper"** view is automatically added to your default dashboard.

    ### Using Zone Mapper

    1. Open the **Zone Mapper** view on your dashboard.
    2. Select your Sat1 device and pick the LD2450 **X/Y target entities** you want to track.
    3. **Draw zones** directly on the visual radar map — rectangles, ellipses, or freeform polygons (up to 32 points). You can create multiple zones and name them (e.g. "Desk", "Doorway", "Bed").
    4. Use the **rotation** control to align the radar's orientation with your room layout.
    5. Each zone automatically creates an **occupancy binary sensor** in Home Assistant that turns on when a tracked target is inside the zone — ready for use in automations.

=== "Beta"
    
     A built-in **Radar Tuner WebUI** that lets you visually calibrate your mmWave sensor directly from a web browser — no Home Assistant dashboard cards or manual entity tweaking required.

      1. Open your Sat1's **ESPHome Device UI** in Home Assistant.
      2. Scroll down to the **Diagnostics** section.
      3. Toggle on **"Radar Tuner WebUI"**.
      4. Open a web browser and navigate to your **Sat1's IP address** (e.g., `http://192.168.1.xxx`), or you can simply click the "Visit Button" in the Device Info section.

      <figure markdown="span">
        ![mmWave radar tuner visit button](../assets/presence-sensors/visit_radar_tuner_webUI.png){ loading=lazy}
        <figcaption>Toggle on the Radar WebUI, then click the visit button</figcaption>
      </figure>

      The LD2450 tuner lets you draw **up to 3 detection zones** plus an **exclusion zone** on a visual radar map.  Click on the canvas to add points and define each zone's boundary.  This gives you precise spatial control over where presence is detected.

      ![Satellite1 Radar Tuner — LD2450](/assets/presence-sensors/radar_tuner_ld2450.png){ width="100%" loading=lazy }

      - **Zone 1 / Zone 2 / Zone 3**: Define areas where you want presence detection active.
      - **Exclusion Zone**: Mark areas to ignore (e.g., a fan, a window with moving curtains).
      - Adjust **Max Detection Range**, **Timeout**, **Stability**, and **Multi-Target Tracking** from the right-hand panel.
      - Click **"Save Zone"** after defining each zone, then **"Save All Zones"** to write the configuration to the sensor.

      After tuning, the relevant presence sensors and states will appear in your Sat1's ESPHome Device UI, ready for use in Home Assistant automations.

## Tuning LD2410 Gates

=== "Stable"

    ### ESPHome LD2410 Entities

    Don't be overwhelmed with several dozen new entities that appeared after installation.  Let's familiarize ourselves with the entities:  

    1.  Binary sensors:
        1. **Moving target** - sensor of moving target presence.
        2. **Still target** - still presence sensor. Mostly off, when moving target is present.
        3. **Presence** - main presence sensor. Populated by other two, with cooldown (see **Timeout** below).
    2. Sensors:
        1. **Moving/still distance** - sensors of the distance to corresponding target.
        2. **G(1-8) moving/still energy** - the value of energy for corresponding gate.
    3. Switches:
        1. **Engineering mode** - this switch will enable fine-tuning for sensor, and will report its readings to each gate in real time. Keep it off when not setting up your sensor, as it is pretty extensive operation.
        2. **Control Bluetooth** - enables built-in Bluetooth on sensor, so you could connect to it with HLK application and set it up from there. Useful, if you want to upgrade sensor firmware.
    4. Select:
        1. **Distance resolution** - you can choose gate length 0.75m or 0.2m
    5. Numbers:
        1. **Timeout** - will set the cooldown period for sensor (time from last presence detected to main presence sensor switching into "off" state).
        2. **Max moving/still distance gate** - will restrict sensor to a certain distance. E.g. if it's set to 6, and distance resolution is 0.75 - max sensor triggering distance will be 4.5 meters.
        3. **G(1-8) moving/still threshold**  - this setting will set the threshold for presence detection for each gate (movement or still presence respectively). If the amount of energy for the corresponding gate is greater than this threshold—the sensor will detect presence in that gate.

    ### Installing Custom UI Tuner Card

    We built UI card, to make calibration process more intuitive.
    <br>![LD2410 Dashboard](/assets/ld2410_calibration_card.png){ width="100%" loading=lazy }</br>

    1. Install [Mushroom cards](https://github.com/piitaya/lovelace-mushroom), [Auto-entities card](https://github.com/thomasloven/lovelace-auto-entities), [Decluttering card](https://github.com/custom-cards/decluttering-card), [Vertical Stack In Card](https://github.com/ofekashery/vertical-stack-in-card), and [Bar card](https://github.com/custom-cards/bar-card) from HACS.
    2. Put this to the very bottom of dashboard YAML in raw edit mode (this should be done once per dashboard):

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

    3. Put following card to your dashboard. Replace `device` field value with with your satellite name, as it appears in entities IDs, like `satellite1_92fb28`.

        ```yaml
        type: custom:decluttering-card
        template: ld2410
        variables:
            - device: satellite1_9a72b3
        ```

    ### Using Custom UI Tuner Card

    1. Blue bars are threshold sliders. Orange bars are energy indicators.  Set sensor in place, where its 120 degrees will be most useful, and catch the least of unnecessary movement.

    2. Turn on **Engineering mode** switch.

    - Set the maximum gate based on room length. If you struggle with correct number, just wave hands or jump in opposite corner, see which gate detects movement, and set that number to **Max moving/still distance gate**. (Don't hesitate, set threshold a bit higher - that energy values can jump!)
    - And finally, calibrate it for no presence: step out, let it settle for a bit (like a minute), and adjust moving and still thresholds, so they would be higher than energy levels for corresponding gates.

=== "Beta"
    
     A built-in **Radar Tuner WebUI** that lets you visually calibrate your mmWave sensor directly from a web browser — no Home Assistant dashboard cards or manual entity tweaking required.

      1. Open your Sat1's **ESPHome Device UI** in Home Assistant.
      2. Scroll down to the **Diagnostics** section.
      3. Toggle on **"Radar Tuner WebUI"**.
      4. Open a web browser and navigate to your **Sat1's IP address** (e.g., `http://192.168.1.xxx`), or you can simply click the "Visit Button" in the Device Info section.

      <figure markdown="span">
        ![mmWave radar tuner visit button](../assets/presence-sensors/visit_radar_tuner_webUI.png){ loading=lazy}
        <figcaption>Toggle on the Radar WebUI, then click the visit button</figcaption>
      </figure>

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
Both the LD2410 & LD2450 can be updated via the HLKRadarTool mobile app over bluetooth. Download the app, then watch the quick video below to see how to access the sensor and change the firmware version.

<div style="display: flex; align-items: center; gap: 8px; margin: 1em 0;">
  <a href="https://apps.apple.com/us/app/hlkradartool/id1638651152">
    <img style="height: 44px;" src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg" alt="Download on the App Store"/>
  </a>
  <a href="https://play.google.com/store/apps/details?id=com.hlk.hlkradartool&hl=en_US&pli=1">
    <img style="height: 64px;" src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" alt="Get it on Google Play"/>
  </a>
</div>

<iframe style="width: 100%; aspect-ratio: 16 / 9;" src="https://www.youtube.com/embed/t8-JdVVVH34?si=3HRSFepdfceSfEtx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
