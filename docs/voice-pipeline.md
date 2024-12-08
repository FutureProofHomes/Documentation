## Setting up your Satellite one to talk and listen

Now that your device is recognized by Home Assistant, you'll want to breathe some life into in so it can hearwhat you say and respsond to your commands.  That involves a few steps to get a basic Voice Pipleline installed that can recognize basic Home Assistant command like "Turn on the bedroom light".  For more advanced interactions, see Advanced Pipelines.

!!! note
    This guide assumes you already have the ESPHome Add-On installed.  If not, then install ESPHome first and come back to this guide and continue. Satellite1 uses ESPHome for all its configuration.
    
    <a href="https://esphome.io/guides/getting_started_hassio.html" target="_blank">Instructions for installing ESPHome</a>

## Set up a Voice Pipeline in Home Assistant

The easiest method is simply to navigate Home Assistant as follows

**/Settings/Voice Assistants/Add Assistant**

<img width="60%" alt="image" src="/assets/Pipeline0.png">

Now give your assistant a name, and choose your preferred option.  Most of the defaults should work fine.

<img width="60%" alt="image" src="/assets/Pipeline1.png">

Lastly, click "Create"

<img width="60%" alt="image" src="/assets/Pipeline2.png">

You now have a "Voice Pipeline" that will soon be able to hear and speak.

<img width="60%" alt="image" src="/assets/Pipeline3.png">

Next you'll want to select that pipeline on your new Satellite1
Navigate Home Assistant as follows

**/Settings/Devices & Services/ESPHome/**   

Click on "1 device" directly under the Satellite1 device

<img width="60%" alt="image" src="/assets/Pipeline4.png">

Scroll down to the Configuration section, and make sure your new Voice Pipeline you configured in the previous steps is selected

<img width="60%" alt="image" src="/assets/Pipeline5.png">

You should also set your preferred wake word

<img width="60%" alt="image" src="/assets/Pipeline7.png">

You'll also notice here that there are a few other things you can play with.  You can toggle the switches to turn on the LED Ring, and mute the Microphone.  You can also set the hue and brightness of the LED ring here.  Try it!

<img width="60%" alt="image" src="/assets/Pipeline8.png">


Each of these setting has an immediate effect.  No need to restart anything.

## Finishing up

You should now be able to say "Hey Jarvis (or Ok Nabu), what time is it?" and Satellite1 should answer!

Congtatulations!  You've completed the basic setup of your new Satellite1 Voice Assistant and added a voice piple line that it can use to listen and speak.

## Advanced Voice Pipeline Options

You can add advanced features to your Voice Asistant quite easily!
Controlling Home Assistant is done by providing the AI access to the Assist API of Home Assistant. You can control what devices and entities it can access from the <a href="https://my.home-assistant.io/redirect/voice_assistants" target="_blank">Exposed Entities page</a>. The AI is able to provide you information about your devices and control them.

[Using Googles Generative AI Voice Pipeline ](voice-pipeline -googleGPT.md)