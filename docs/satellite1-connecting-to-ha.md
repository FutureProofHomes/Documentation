This is the same for every Satellite1, whichever form factor you have. A Smart Speaker is ready for it out of the box, and a Dev Kit or an in-ceiling unit is ready once it is assembled.

## First boot

Power it from the Hat's USB-C port, labelled **CORE/ESP32**, using a 30 W USB-C PD supply. On the 1.1 that is the only USB-C on the board.

On first boot the blue LEDs count down clockwise while the device flashes its XMOS audio processor. When they change to a sparkling warm white, it is waiting to be set up. A factory-fresh unit arrives in Bluetooth pairing mode, so you do not need a cable or an app beyond Home Assistant itself.

## Connect it to Home Assistant

You need a running Home Assistant instance and a 2.4 GHz Wi-Fi network. No internet connection is required, either now or later.

1.  **Find it in the Home Assistant app**

    ![Home Assistant showing a discovered Satellite1 device](/assets/ble_improv/3_improv_discovered_device.png){ width="280" loading=lazy }

    Open Home Assistant on a phone with Bluetooth on, go to Settings then Devices & Services, and tap Add next to the discovered Satellite1. The name ends in the last six characters of its MAC address.

2.  **Enter your Wi-Fi credentials**

    ![Entering Wi-Fi credentials in the Home Assistant app](/assets/ble_improv/4_improv_add_wifi_credentials.png){ width="280" loading=lazy }

    It has to be a 2.4 GHz network. Tap Connect.

3.  **Authorize from the device**

    ![Pressing the right action button on the Hat board](/assets/ble_improv/6_click_action_button.png){ width="280" loading=lazy }

    Press the right action button on the Hat. This is the step people miss, because it happens on the hardware rather than on the phone.

4.  **Continue once Wi-Fi connects**

    ![Successful Wi-Fi connection confirmation](/assets/ble_improv/8_improv_successful_wifi_connection.png){ width="280" loading=lazy }

    The app confirms the connection. Tap Continue.

5.  **Start the ESPHome setup**

    ![ESPHome setup request dialog](/assets/ble_improv/9_esphome_setup_request.png){ width="280" loading=lazy }

    Tap Ok when asked to set up ESPHome.

6.  **Pick the device**

    ![Selecting the Satellite1 in the ESPHome device list](/assets/ble_improv/10_esphome_select_device.png){ width="280" loading=lazy }

    Tap your Satellite1 in the list, then Submit.

7.  **Let it update**

    ![The wizard checking for firmware updates](/assets/ble_improv/12_wizard_checking_for_updates.png){ width="280" loading=lazy }

    The wizard pulls down the most recent firmware. This happens before anything else, so a new unit is current by the time you use it.

8.  **Say the wake word twice**

    ![The wake word detection test](/assets/ble_improv/13_wizard_first_wake_word_test.png){ width="280" loading=lazy }

    The wizard tests detection before it finishes, so you find out immediately rather than after setup.

9.  **Assign an area**

    ![Assigning the device to an area](/assets/ble_improv/15_wizard_assign_area.png){ width="280" loading=lazy }

    Pick the room it lives in. Home Assistant uses this for voice commands that depend on location.

10. **Choose wake word, assistant and voice**

    ![Choosing the wake word, assistant and voice](/assets/ble_improv/16_wizard_quick_pipeline_config.png){ width="280" loading=lazy }

    The defaults work. Change them here or later from the ESPHome device page.

!!! warning "Do not add it twice"

    ![Home Assistant offering to add the device again](/assets/ble_improv/17_ignore_device_discovered_cut.png){ width="40%" align=left loading=lazy }

    After the wizard finishes, Home Assistant may offer to add the Satellite1 to ESPHome again. Ignore it. Refreshing the page clears it.

That is it. Say the wake word and it should answer.

## Add an mmWave sensor

Optional, and the most common thing people add. An LD2450 gives the Satellite1 presence rather than motion, so a room stays occupied while you sit still in it. It tracks up to three people at once as X and Y coordinates, which lets you define up to three zones plus an exclusion zone for things that move but are not people, like a ceiling fan or a curtain.

![The 4-pin JST connector on the underside of the Satellite1.1 Hat](/assets/presence-sensors/sat1.1_ld2450_square.png){ width="60%" }

### Fitting it

The Satellite1.1 Hat has a 4-pin JST connector on its underside, so the sensor connects with the harness cable rather than being mounted on the board. On a Smart Speaker the sensor sits in the pocket printed into the front chamber, which means lifting the top plate off to route the cable.

!!! warning "Update the sensor's own firmware first"

    An LD2450 needs radar firmware newer than **V2.02.23090617** to work with ESPHome. It ships with whatever it shipped with, so check before fitting it. The update happens over Bluetooth from the HLKRadarTool mobile app, not from the Satellite1.

### Confirming it is seen

There is nothing to configure. The firmware works out which radar is attached and exposes the right entities on its own, with no reflash. To check, open the device under Settings, Devices & Services, ESPHome, and scroll to Diagnostics, where the detected radar is listed.

### Tuning the zones

![The Radar Tuner WebUI toggle in the Diagnostics section](/assets/presence-sensors/mmwave_radar_tuner_toggle.png){ width="60%" }

Turn on **Radar Tuner WebUI** in that same Diagnostics section, then open the Satellite1's IP address in a browser, or use the Visit button on the device page. The tuner draws what the radar sees, so you place zones against a live picture rather than guessing at coordinates.

![The Radar Tuner WebUI showing LD2450 zones](/assets/presence-sensors/radar_tuner_ld2450.png){ width="100%" }

## What to do next

Everything from here is optional.

- **Change the wake word, assistant or voice** from the device's page under Settings, Devices & Services, ESPHome.
- **Play music through it** with Music Assistant, which finds it over Sendspin with no extra setup.

[Troubleshooting :material-arrow-right:](satellite1-faqs.md){ .md-button }
