# Satellite1 FAQs

Common questions and step-by-step fixes in one place.

## Wake Words & Voice

### What wake words are supported? { .faq-question }
??? note "What wake words are supported?"
    The Satellite1 uses ESPHome's [microWakeWord](https://esphome.io/components/micro_wake_word.html) and supports **"Hey Jarvis"** and **"Okay Nabu"**.

### How do I add other wake words? { .faq-question }
??? note "How do I add other wake words?"
    [Modify and compile your own firmware](satellite1-modifying-the-firmware.md) to add compatible MicroWakeWords. We recommend [TaterTotterson's collection](https://github.com/TaterTotterson/microWakeWords).

### How do I create my own wake word? { .faq-question }
??? note "How do I create my own wake word?"
    You’ll need a GPU, sample data, and some know-how. We recommend TaterTotterson’s trainers:
    - [microWakeWord-Trainer-Nvidia-Docker](https://github.com/TaterTotterson/microWakeWord-Trainer-Nvidia-Docker)
    - [microWakeWord-Trainer-AppleSilicon](https://github.com/TaterTotterson/microWakeWord-Trainer-AppleSilicon)

### Why isn't the wake word responding? { .faq-question }
??? note "Why isn't the wake word responding?"
    1. Try both "Okay Nabu" and "Hey Jarvis".
    2. Increase **Wake Word Sensitivity** in the Sat1 ESPHome device settings.
    3. Speak normally toward the microphones; don’t shout.
    4. Keep microphones unobstructed. Avoid enclosed spots (e.g. inside a shelf) or very reflective rooms (e.g. marble floors).
    5. Detection can be harder for non-English accents or higher-pitched voices; consider training your own wake word (see above).
    6. Loud background noise (water, wind, TV, oven hoods) can interfere; XMOS firmware updates keep improving this.
    7. Still stuck? Try [adding or training a custom wake word](#how-do-i-create-my-own-wake-word) above.

---

## Audio Out & Playback

### Why don't I hear any audio? { .faq-question }
??? note "Why don't I hear any audio?"
    Use the USB-C port on the HAT labeled **"CORE/ESP"**. The port labeled **"XMOS/SNDCARD"** is for XMOS development only and does not drive the amplifier.  Check the **USB-C Power Draw** sensor in the Sat1 ESPHome UI; we recommend 30W of power.
    ![usbc power draw](/assets/usb-c_power_draw.png){ width="100%" }

### Why does my speaker sound distorted? { .faq-question }
??? note "Why does my speaker sound distorted?"
    The Sat1 is likely underpowered. Check the **USB-C Power Draw** sensor in the Sat1 ESPHome UI; you should see about 30W.
    ![Underpowered Sat1](/assets/underpowered.png){ width="100%" }

### Why is my speaker too quiet? { .faq-question }
??? note "Why is my speaker too quiet?"
    1. We recommend 30W of power.  Check the **USB-C Power Draw** sensor in the Sat1 ESPHome UI.
    2. In Music Assistant: open the Sat1 speaker’s Player Settings, disable **Enable volume normalization (EBU-R128 based)** and **Enable limiting to prevent clipping**, then increase gain in Music Assistant’s DSP. [Details here](satellite1-streaming-music.md#start-the-snapcast-server).
    ![usbc power draw](/assets/usb-c_power_draw.png){ width="100%" }

### Why is music or TTS stuttering? { .faq-question }
??? note "Why is music or TTS stuttering?"
    1. Make sure your Sat1 has a [good WiFi connection](#how-do-i-check-wifi-connection).
    2. Try other TTS voices.
    3. Try streaming music from Music Assistant's media player section to rule out MA.

---

## Audio In & Microphones

### How do I inspect audio recordings? { .faq-question }
??? note "How do I inspect audio recordings?"
    Store a copy of your audio recordings on the Home Assistant server for inspection:

    1. In Home Assistant, add to your `configuration.yaml`:

    ```yaml
    assist_pipeline:
      debug_recording_dir: /share/assist_pipeline
    ```

    2. Open that path in Home Assistant (e.g. Studio Code Server) and listen to the files.
    3. Don’t leave this on permanently; it will fill your server with recordings.


---

## Networking

### How do I check WiFi connection? { .faq-question }
??? note "How do I check WiFi connection?"
    The Sat1 includes a Wi-Fi Signal Strength sensor that should read between -30 dBm and -75 dBm. If the reading is lower than -75 dBm, your Sat1 may underperform. Move closer to the access point or upgrade to a Core Board with an external antenna.
    ![WiFi Signal Strength](/assets/wifi_signal_strength.png){ width="100%" }


### How do I switch to a new WiFi SSID or Password? { .faq-question }
??? note "How do I switch to a new WiFi SSID or Password?"
    [Wipe the Sat1 and flash fresh firmware](#how-do-i-flash-back-to-factory-settings).   Or just [wipe the credentials from the device](#how-do-i-clear-wifi-and-restart-ble-improv).

---

## LED Color Codes

### Why do my LEDs flash red after giving command? { .faq-question }
??? note "Why do my LEDs flash red after giving command?"
    Something is wrong with your voice pipeline in HA.  [Debug your voice pipeline.](#how-do-i-debug-the-voice-pipeline).

### Why are my LEDs twinkling red? { .faq-question }
??? note "Why are my LEDs twinkling red?"
    Your Sat1 cannot connect to your Home Assistant/ESPHome.  Typically a networking issue.  [Check your WiFi connection.](#how-do-i-check-wifi-connection)

### What do all the LED color codes mean? { .faq-question }
??? note "What do all the LED color codes mean?"
    We follow the same patterns as Nabu Casa.  [Read more here.](https://support.nabucasa.com/hc/en-us/articles/25764604971421-Status-colors-of-the-LEDs-status-LEDs-on-Home-Assistant-Voice-Preview-Edition)



## Logs & Debugging

### How do I view Sat1 logs? { .faq-question }
??? note "How do I view Sat1 logs?"
    1. Connect the Sat1 to your computer with a USB-C cable.
    2. Click the connect button below and select the correct JTAG device.
    3. Choose **Logs & Console**.

    <div id="firmware-installer" markdown="1">
    <esp-web-install-button id="install-button" manifest="https://raw.githubusercontent.com/FutureProofHomes/Documentation/refs/heads/main/manifest.json" install-supported></esp-web-install-button>
    </div>

### How do I debug the voice pipeline? { .faq-question }
??? note "How do I debug the voice pipeline?"
    In Home Assistant: **Settings → Voice Assistants**, click the 3-dot menu next to that pipeline. [Learn more here.](https://www.home-assistant.io/voice_control/troubleshooting/).

    ![Debugging a Voice Pipeline](/assets/debug_assist.png){ width="100%" loading=lazy }

---

## Factory Settings & Flashing Releases

### How do I completely remove the Sat1 from Home Assistant & ESPHome? { .faq-question }
??? note "How do I completely remove the Sat1 from Home Assistant & ESPHome?"
    1. In Home Assistant: **Settings → Devices and Services → ESPHome** → 3 dots next to the Satellite1 → **Delete**.
        ![Delete ESPHome device](/assets/delete_sat1_esp_device.png){ width="100%" }
    2. If you “Took Control” in ESPHome Device Builder: **Settings → Add-Ons → ESPHome Device Builder** → Open Web UI → 3 dots next to the Satellite1 → **Delete**.
        ![Remove from ESPHome Builder](/assets/delete_sat1_from_esp_builder.png){ width="100%" }

### How do I flash back to factory settings? { .faq-question }
??? note "How do I flash back to factory settings?"
    Connect your Sat1 to your computer and use our web flashing tool to [flash the device back to factory firmware](satellite1-flash-via-usb-c.md)

### How do I clear WiFi and restart BLE Improv? { .faq-question }
??? note "How do I clear WiFi and restart BLE Improv?"
    1. Press and hold the **RIGHT (Action)** button for about 22 seconds until the red LEDs complete a clockwise circle. When the LEDs turn blue, release the button and wait while the XMOS chip is erased (may take a few minutes). The Satellite1 will reboot to factory firmware; blue LEDs will complete another clockwise circle as the XMOS is flashed.
    2. [Add your Satellite1 to Home Assistant](satellite1-connecting-to-ha.md).

### What if flashing is failing or Sat1 is blinking on and off? { .faq-question }
??? note "What if flashing is failing or Sat1 is blinking on and off?"
    1. Unplug the Sat1 from power.
    2. **Remove the Core from the Hat board:** Hold the **Boot** button on the Core, then plug power into the USB-C port. Release Boot button after 3 seconds.  Now try to [flash the Sat1 via USB-C](satellite1-flash-via-usb-c.md).  Unplug and mount the Hat back to the Core board.
        ![CORE BOOT Button](/assets/boot_mode_core_board.png){ width="100%" }
    3. **If you really don't want to remove the Core board:** Hold the **Right/Action** button on the HAT, then plug power into the HAT’s **"ESP32/CORE"** USB-C port. Release the Action button after 3 seconds.  Try to [flash the Sat1 via USB-C](satellite1-flash-via-usb-c.md).
        ![HAT BOOT Button](/assets/right_action_button.jpg){ width="100%" }

### How do I update my Sat1? { .faq-question }
??? note "How do I update my Sat1?"
    1. Updates are delivered over the air. Simply click the “Update Available” button. If you don’t see an expected update, please restart your Sat1 and toggle the “Beta Firmware” switch.
    ![Update available button](/assets/update_available.png){ width="100%" }
    2. You can also update from our [Web Flasher Tool](satellite1-flash-via-usb-c.md)


## Need More Help?

While we hope this documentation will answer all your questions, we realize support is sometimes needed. The FutureProofHomes team will do their best to keep up with support requests, but we also lean on our community to help all of us. See the links below and decide which method of support is best for your needs.

!!! question "Have a general question and need quick help from the community?"

    [Chat with the Community on Discord :fontawesome-brands-discord:](https://discord.futureproofhomes.net){ .md-button }

!!! success "Do you have a feature request or reproducible bug?"
    Look through our existing tickets first, then open a new request if necessary: <br>
    [Request a feature on GitHub :fontawesome-solid-rocket:](https://github.com/FutureProofHomes/Satellite1-ESPHome/issues/new?template=feature-request--.md){ .md-button }
    [Report a bug :fontawesome-solid-bug:](https://github.com/FutureProofHomes/Satellite1-ESPHome/issues/new?template=bug-report--.md){ .md-button }

!!! failure "Hardware issue or need direct support?"
    [Email Support@futureproofhomes.net :material-email:](mailto:Support@FutureProofHomes.net){ .md-button }