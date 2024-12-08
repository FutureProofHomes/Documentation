---
title: Troubleshooting
description: Troubleshooting Guide for your new Satellite1
---
## Troubleshooting your new Satellite1

## Resetting the Satellite1 to Factory Settings

1) Press and KEEP holding the RIGHT [Action] button for Approximately 15 seconds until the red LEDs start to make a clockwise circle. Keep holding the action button until all LEDs or extinguished.  The LEDs will glow blue, and you can then release the button. The blue LEDs will then also start to extinguish themselves in a clockwise fashion one at a time. 

2) Wait until thThe LEDs will glow blue, and you can then release the button. The blue LEDs will then also start to extinguish themselves in a clockwise fashion one at a time.

3) Wait until this sequence has been completed which takes a couple of minutes And all the LEDs have gone out. 

4) Wait a couple more minutes and the board will reset and the LEDs will go all sparkly. Which indicates the board has started up and is now in the same state as when you received it from the factory.

## Configuring using the Easy Method

[Start over using the Easy Method ](Start%20Here.md#EasyMode)

## Flashing from the Browser (Expert/Advanced)
!!! note 
    Note, you must use a browser that supports flashing like Chrome,, Brave or Safari

[Flash from your browser here ](Start%20Here.md#ExpertMode)

## <a name="Logs" /a> Using the logs to troubleshoot problems

Connect your Satellite1 to your computer using a USB-C cable. Choose your serial port then click the connect button.

!!! note 
    Note, you must use a browser that supports flashing like Chrome,, Brave or Safari

<div id="firmware-installer" markdown="1">
  <esp-web-install-button id="install-button" manifest="https://raw.githubusercontent.com/FutureProofHomes/Documentation/refs/heads/main/manifest.json" install-supported></esp-web-install-button>
</div>

Choose Logs & Console:

<img width="150" alt="image" src="/assets/TroubleshootingLogsConsole.png">

If you click on "Reset Device" you should see a whole bunch of useful messages and information.  Scroll backup and take a look.  

<img width="700" alt="image" src="/assets/TroubleshootingLogs.png">

Scroll to the bottom and issue a command "Hey Jarvis, what time is it?"

<img width="700" alt="image" src="/assets/TroubleshootingHeyJarvis.png">
