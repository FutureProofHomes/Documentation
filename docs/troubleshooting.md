## Inspecting Sat1 ESP32 Logs

??? abstract "I want to see Sat1 ESP32 logs via a USB-C cable."

    1. Connect the Sat1 to your computer using a USB-C cable. 
    2. Click the connect button below and select the correct JTAG device.
    3. Choose Logs & Console:

    <div id="firmware-installer" markdown="1">
    <esp-web-install-button id="install-button" manifest="https://raw.githubusercontent.com/FutureProofHomes/Documentation/refs/heads/main/manifest.json" install-supported></esp-web-install-button>
    </div>

    <img width="60%" alt="image" src="/assets/TroubleshootingLogsConsole.png">

    If you click on "Reset Device" you should see a whole bunch of useful messages and information.  Scroll backup and take a look.  

    <img width="60%" alt="image" src="/assets/TroubleshootingLogs.png">

    Scroll to the bottom and issue a command "Hey Jarvis, what time is it?"

    <img width="60%" alt="image" src="/assets/TroubleshootingHeyJarvis.png">

??? abstract "I want to see Sat1 ESP32 logs via my Wi-Fi network (Over the Air)"

    These instructions will come soon.  It's complicated depending on your environment.  

## Debugging your Voice Pipeline

Curious why your Sat1 is doing something different than what you'd expect?  Use Home Assistant pipeline debugging tools.

<img width="60%" alt="image" src="/assets/debug_assist.png">

1. Determing what pipeline your Sat1 is using by retracing these steps: [Assign a Voice Pipeline & Wake Word to your Satellite1](/voice-pipeline/#assign-a-voice-pipeline-wake-word-to-your-satellite1)
3. In Home Assitant, go to Settings -> Voice Assistants and select the 3 dots next to that pipeline.
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

## Resetting to Factory Settings

1. Press and hold the RIGHT (Action) button for approximately 15 seconds until the red LEDs start to make a clockwise circle. Keep holding the action button until all LEDs or extinguished.  The LEDs will glow blue, and you can then release the button. The blue LEDs will count down in a clockwise cirlce to wipe the ESP and XMOS chips.  This may take a few minutes.

2. In your Home Assistant, go to Settings -> Devices and Services -> ESPHome and click the 3 dots next to the Satellite1 and select "Delete".

3. Follow the steps to [Add your Satellite1 to Home Assistant](/#connecting-to-home-assistant)

## Need More Help?

The FutureProofHomes team will do their best to keep up with support requests, but we also lean on our community to help all of us.  See the links below and decide which method of support is best for your needs.

!!! question "Have a general question and need quick help from the community?"

    [Chat with the Community on Discord :fontawesome-brands-discord:](https://discord.gg/BeBjWEPzMV){ .md-button }

!!! tip "Discord too chatty and you want a record of your general question?"

    [Start a Discussion on Github :fontawesome-solid-comments:](https://github.com/orgs/FutureProofHomes/discussions){ .md-button }

!!! success "Do you have a feature request you'd love to see?"
    Look through our existing Feature Requests first, then open a new request if necessary: <br>
    [Requst a New Feature on Github :fontawesome-solid-rocket:](https://github.com/FutureProofHomes/Satellite1-ESPHome/issues/new?labels=bug&template=bug-report---.md){ .md-button }

!!! bug "Have you found a reproducable issue with the hardware or software? "
    [Report a Bug on Github :fontawesome-solid-bug:](https://github.com/FutureProofHomes/Satellite1-ESPHome/issues/new?labels=bug&template=bug-report---.md){ .md-button }

