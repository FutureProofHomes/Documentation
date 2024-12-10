## Inspecting Logs

!!! note 
    Note, you must use a browser that supports flashing like Chrome, Brave or Safari

Connect your Satellite1 to your computer using a USB-C cable. Choose your serial port then click the connect button below.

<div id="firmware-installer" markdown="1">
  <esp-web-install-button id="install-button" manifest="https://raw.githubusercontent.com/FutureProofHomes/Documentation/refs/heads/main/manifest.json" install-supported></esp-web-install-button>
</div>

Choose Logs & Console:

<img width="60%" alt="image" src="/assets/TroubleshootingLogsConsole.png">

If you click on "Reset Device" you should see a whole bunch of useful messages and information.  Scroll backup and take a look.  

<img width="60%" alt="image" src="/assets/TroubleshootingLogs.png">

Scroll to the bottom and issue a command "Hey Jarvis, what time is it?"

<img width="60%" alt="image" src="/assets/TroubleshootingHeyJarvis.png">

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

[Back to Top](./troubleshooting.md/#inspecting-logs)