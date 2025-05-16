## Inspecting Sat1 ESP32 Logs

??? abstract "I want to see Sat1 ESP32 logs via a USB-C cable."

    (NOTE: If you need lower level `DEBUG` logs then you're going to need to [adopt the Sat1 to your ESPHome Dashboard](/satellite1-modifying-the-firmware/#import-the-sat1-to-your-esphome-dashboard) and set log level from there.)

    1. Connect the Sat1 to your computer using a USB-C cable. 
    2. Click the connect button below and select the correct JTAG device.
    3. Choose Logs & Console:

    <div id="firmware-installer" markdown="1">
    <esp-web-install-button id="install-button" manifest="https://raw.githubusercontent.com/FutureProofHomes/Documentation/refs/heads/main/manifest.json" install-supported></esp-web-install-button>
    </div>

    <br>![Logs Console](/assets/TroubleshootingLogsConsole.png){ width="100%" loading=lazy }</br>

    If you click on "Reset Device" you should see a whole bunch of useful messages and information.  Scroll back up and take a look.  

    <br>![Troubleshooting Logs](/assets/TroubleshootingLogs.png){ width="100%" loading=lazy }</br>

    Scroll to the bottom and issue a command "Hey Jarvis, what time is it?"

    <br>![Troubleshooting Hey Jarvis](/assets/TroubleshootingHeyJarvis.png){ width="100%" loading=lazy }</br>

??? abstract "I want to see Sat1 ESP32 logs via my Wi-Fi network (Over the Air)"

    These instructions will come soon.  It's complicated depending on your environment.  

## Debugging your Voice Pipeline

Curious why your Sat1 is doing something different than what you'd expect?  Use Home Assistant pipeline debugging tools.

<br>![Debugging a Voice Pipeline](/assets/debug_assist.png){ width="100%" loading=lazy }</br>

1. Determine what pipeline your Sat1 is using by retracing these steps: [Assign a Voice Pipeline & Wake Word to your Satellite1](/satellite1-set-up-voice-control/#assign-a-voice-pipeline)
3. In Home Assistant, go to Settings -> Voice Assistants and select the 3 dots next to that pipeline.
4. Read here: [Debugging a Voice Pipeline](https://www.home-assistant.io/voice_control/troubleshooting/)


## Inspect Sat1 Audio Recording Files

Follow these steps to store a copy of your audio recordings in your Home Assistant server for inspection.

1. Modify your `configuration.yaml` file and add the following:

```yaml
assist_pipeline:
  debug_recording_dir: /share/assist_pipeline
```

2. Now go to that path in your Home Assistant (recommend using Studio Code Server) and listen to the files there.
3. Don't leave this on forever, it will clog up your server with audio recordings.


## Clear WiFi Credentials to Restart BLE Improv

1. Press and hold the RIGHT (Action) button for approximately 22 seconds until the red LEDs complete their clockwise circle.  When the LEDs glow blue you can release the action button and wait as the XMOS chip is erased.  This process may take a few minutes before the Satelllite1 finally reboots to the factory firmware.  Upon first boot you will see the blue LEDs complete another clockwise circle indicating the XMOS is being flashed with the facory embedded firmware.

2. Follow the steps to [Add your Satellite1 to Home Assistant](satellite1-connecting-to-ha.md)


## Resetting to Factory Settings
This process will erase all settings on the Sat1 device and restore the latest production firmware, returning it to factory-new condition. You will need a USB-C cable and a computer with an internet connection (Google Chrome browser recommended).

??? abstract "First, remove the Sat1 from ESPHome & Home Assistant"

    1. In your Home Assistant, go to Settings -> Devices and Services -> ESPHome and click the 3 dots next to the Satellite1 and select "Delete".
    ![Delete ESPHome ESPHome](/assets/delete_sat1_esp_device.png){ width="100%" }
    2. If you "Took Control" of the Sat1 in your ESP Home Device Builder then go to Settings -> Add-Ons -> ESPHome Device Builder and open the Web UI to click the 3 dots next to the Satellite1 and select "Delete".
    ![Remove from ESPHome Builder](/assets/delete_sat1_from_esp_builder.png){ width="100%" }


??? abstract "Then Flash your Satellite1 a Computer's USB-C Connection"

    1. Unplug the Sat1 from power.

    2. Press and the HAT's "Action" button OR the CORE's "Boot" button.
    ![CORE BOOT Button](/assets/boot_reset_button.jpg){ width="100%" }
    ![HAT BOOT Button](/assets/right_action_button.jpg){ width="100%" }

    3. While holding down the "Boot" button, plug the Sat1's "ESP32/CORE" connection into your computers USB-C port.  Let go of the "Boot" button after 3 seconds.
    ![ESP32 Power & Data Port](/assets/sat1_inputs_and_outputs.jpg){ width="100%" }

    4. Follow these steps to [Add your Satellite1 to Home Assistant via a USB-C cable](satellite1-connecting-to-ha.md#re-flashing-your-satellite1-via-a-usb-c-cable)

## Need More Help?

While we hope this documentation will answer all your questions, but we realize support is sometimes needed.  The FutureProofHomes team will do their best to keep up with support requests, but we also lean on our community to help all of us.  See the links below and decide which method of support is best for your needs.

!!! question "Have a general question and need quick help from the community?"

    [Chat with the Community on Discord :fontawesome-brands-discord:](https://discord.gg/BeBjWEPzMV){ .md-button }

!!! tip "Discord too chatty and you want a record of your general question?"

    [Start a Discussion on Github :fontawesome-solid-comments:](https://github.com/orgs/FutureProofHomes/discussions){ .md-button }

!!! success "Do you have a feature request you'd love to see?"
    Look through our existing Feature Requests first, then open a new request if necessary: <br>
    [Request a New Feature on Github :fontawesome-solid-rocket:](https://github.com/FutureProofHomes/Satellite1-ESPHome/issues/new?template=feature-request--.md){ .md-button }

!!! bug "Have you found a reproducible issue with the hardware or software? "
    [Report a Bug on Github :fontawesome-solid-bug:](https://github.com/FutureProofHomes/Satellite1-ESPHome/issues/new?template=bug-report--.md){ .md-button }