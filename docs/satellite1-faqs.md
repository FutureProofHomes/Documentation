<a id="faq_anchor_factory_reset"></a>
???+ note "I messed something up, how do I start over?"

    1. [Remove the Sat1 from ESPHome](satellite1-troubleshooting.md/#removing-the-sat1from-esphome)
    2. [Flash the device back to factory firmware.](satellite1-flash-via-usb-c.md)

???+ note "Why don't I hear any audio coming out of the speaker I connected?"

    You must have a 9V USB-C power supply with a capacity of 20W-30W. [Here are some recommended options.](satellite1-recommended-accessories.md)  You can check how much power your Sat1 is receiving by checking the ESPHome Diagnostics section.
    ![Remove from ESPHome Builder](/assets/esphome/4_esphome_diagnostics_section.png){ width="60%" }

<a id="faq_anchor_inspect_logs"></a>
???+ note "How do I access the Sat1 logs?"

    [If you want to look at the logs, click here](/satellite1-troubleshooting/#inspecting-sat1-esp32-logs){ .md-button .md-button--primary }

<a id="faq_anchor_temp_sensor"></a>
???+ note "Why is the temp sensor incorrect?"

    The temperature/humidity sensor is placed on the HAT near other warm components which cause the sensor to run hot. Look at the Sat1 settings and set a negative offset to compensate for this issue. Logically, if you put the Sat1 in the ceiling you're going to be getting the temperature for your attic, and if you place Sat1 in an enclosure you'll be getting the internal temperature.

    There are two key things to remember here:

    1. This is a "Dev Kit" and the sensors are on the device for development purposes.
    2. We are working on advanced enclosures which will place sensors in the correct location. Stay tuned.

<a id="faq_anchor_wake_words"></a>
???+ note "What wake words are supported?"
    
    The Satellite1 uses ESPHome's [microWakeWord](https://esphome.io/components/micro_wake_word.html) and supports the "Hey Jarvis" and "Okay Nabu" wake words.  If you'd like to add other wake word please read [How do I add other 'wake words'](/satellite1-faqs/#faq_build_custom_wake_word)]

<a id="faq_add_more_wake_words"></a>
???+ note "How do I add other wake words to the Sat1?"

    If you're a developer you can modify [the Sat1 firmware](https://github.com/FutureProofHomes/Satellite1-ESPHome/blob/3c4ff992ce5a7d21c2ff5dd76fc711d3b8321a94/config/common/voice_assistant.yaml#L46-L50) and add other compatible [MicroWakeWord models](https://github.com/esphome/micro-wake-word-models) or even [create your own custom wake word.](https://github.com/kahrendt/microWakeWord/blob/november-update/notebooks/basic_training_notebook.ipynb) 
    <br><br><b>NOTE:</b> The more wake words you add to the firmware the less resouces your Sat1 has for other tasks.

<a id="faq_anchor_wake_word_success"></a>
???+ note "The wake word isn't always responding!"
    
    1. Try both "Okay Nabu" and "Hey Jarvis".
    2. "Okay Nabu" is more trained and may have a higher success rate.
    3. Speak normally. Don't scream.
    4. Also. Don't. Speak. Like. a Robot. Just be normal.
    5. Don't lean into the speaker. Stand a normal 2+ feet away.
    6. Make sure the microphones are not obstructed and that the device is not tucked in a shelf or something similar which causes sound reflection. Same goes with marble floors that cause echoes in the room.
    7. If you have an accent it's going to be harder, but not impossible.
    8. If you have loud water running, wind blowing, kids screaming, oven hoods running... you're gonna have a bad time.

    Still having issues? This will get better in time. We have lots of ideas to solve these problems.

<a id="faq_anchor_report_issue"></a>
???+ note "How do I get help or report issues?"
    Need further help or have suggestions for the product or documentation? Reach out!

    [There are many ways to contact us, click here](/satellite1-troubleshooting/#need-more-help){ .md-button .md-button--primary }