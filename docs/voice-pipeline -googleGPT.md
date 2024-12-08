## Advanced Pipelines: Setting up the Google GPT pipleline

Now that your device is hearing you and responding, you can add advanced functionality by using Google's GPT LL< (Large Language Model).
Follow this guide to get Google Generative AI configured

https://www.home-assistant.io/integrations/google_generative_ai_conversation/

<a href="https://www.home-assistant.io/integrations/google_generative_ai_conversation/" target="_blank">Installing Google Generative AI</a>


## Set up a Voice Pipeline in Home Assistant

Navigate Home Assistant as follows

**/Settings/Voice Assistants/Add Assistant**

<img width="60%" alt="image" src="/assets/Pipeline0.png">

Now give your assistant a name, and make sure you enable these options:

<img width="60%" alt="image" src="/assets/googleGPT0.png">

Turning on the "Prefer handling commands locally" option above is very important.  When you issue a command like "Turn on the light", it will be handled by Home Assistant.  Saying "Why is the sky blue" isn't understood by Home Assistant, and that gets shuttled off to Google's Generative AI server which formulates a response and sends it back to your Satellit1. How cool is that? 

Lastly, click "Create"

<img width="60%" alt="image" src="/assets/Pipeline2.png">

You now have an advanced "Voice Pipeline" that adds many more capabilities to your Satellite1.

<img width="60%" alt="image" src="/assets/googleGPT1.png">

Next you'll want to select that pipeline on your new Satellite1
Navigate Home Assistant as follows

**/Settings/Devices & Services/ESPHome/**   

Click on "1 device" directly under the Satellite1 device

<img width="60%" alt="image" src="/assets/Pipeline4.png">

Scroll down to the Configuration section, and make sure your new Voice Pipeline you configured in the previous steps is selected

<img width="40%" alt="image" src="/assets/googleGPT2.png">


## Finishing up

You should now be able to say "Hey Jarvis (or Ok Nabu), tell me a joke" and Satellite1 should answer!

Congtatulations!  You've completed the advanced setup of your new Satellite1 Voice Assistant and added the Google Generative AI voice piple line that it can use to listen and speak in advanced ways.