## Inspecting Sat1 ESP32 Logs

1. Connect the Sat1 to your computer using a USB-C cable. 
2. Click the connect button below and select the correct JTAG device.
3. Choose Logs & Console:

<div id="firmware-installer" markdown="1">
<esp-web-install-button id="install-button" manifest="https://raw.githubusercontent.com/FutureProofHomes/Documentation/refs/heads/main/manifest.json" install-supported></esp-web-install-button>
</div>

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


## Removing the Sat1from ESPHome
1. In your Home Assistant, go to Settings -> Devices and Services -> ESPHome and click the 3 dots next to the Satellite1 and select "Delete".
    ![Delete ESPHome ESPHome](/assets/delete_sat1_esp_device.png){ width="100%" }
2. If you "Took Control" of the Sat1 in your ESP Home Device Builder then go to Settings -> Add-Ons -> ESPHome Device Builder and open the Web UI to click the 3 dots next to the Satellite1 and select "Delete".
    ![Remove from ESPHome Builder](/assets/delete_sat1_from_esp_builder.png){ width="100%" }
    
## Force the CORE Board into Boot Mode:
1. Unplug the Sat1 from power.
2. If the CORE is mounted to the HAT, press and hold the Right/Action button on the HAT, then apply power to the HAT's "ESP32/CORE" USB-C port.  Let go of the Right/Action button after 3 seconds.
![HAT BOOT Button](/assets/right_action_button.jpg){ width="100%" }
3. If the CORE is NOT mounted to the HAT, press and hold the "Boot" botton on the CORE, then apply power to the CORE's USB-C port.  Let go of the "Boot" button after 3 seconds.
![CORE BOOT Button](/assets/boot_reset_button.jpg){ width="100%" }
4. From here you can [Flash the Sat1 via a USB-C cable](satellite1-flash-via-usb-c.md)

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