<a id="faq_anchor_factory_reset"></a>
???+ note "I messed something up, How do I start over?"

    [Perform a Factory Reset](/troubleshooting/#resetting-to-factory-settings){ .md-button .md-button--primary }

<a id="faq_anchor_inspect_logs"></a>
???+ note "How do I access the Sat1 logs?"

    [If you want to look at the logs, click here](/troubleshooting/#inspecting-logs){ .md-button .md-button--primary }

<a id="faq_anchor_temp_sensor"></a>
???+ note "Why is the temp sensor incorrect?"

    The temperature/humidity sensor is placed on the HAT near other warm components which cause the sensor to run hot. Look at the Sat1 settings and set a negative offset to compensate for this issue. Logically, if you put the Sat1 in the ceiling you're going to be getting the temperature for your attic, and if you place Sat1 in an enclosure you'll be getting the internal temperature.

    There are two key things to remember here:

    1. This is a "Dev Kit" and the sensors are on the device for development purposes.
    2. We are working on advanced enclosures which will place sensors in the correct location. Stay tuned.

```markdown
<a id="faq_anchor_wake_words"></a>
???+ note "What 'wake words' are supported?"
    
    Satellite1 currently supports "Hey Jarvis" and "Okay Nabu" wake words. This support is built directly into the Satellite1 firmware, so you do not need to install the "Open Wakeword" Add-On. We will be adding additional wake word options in the future.

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

<a id="faq_anchor_custom_wake_word"></a>
???+ note "How do I build my own custom wake word?"

    [This will require time and GPU horsepower.](https://github.com/kahrendt/microWakeWord/blob/november-update/notebooks/basic_training_notebook.ipynb){ .md-button .md-button--primary }

<a id="faq_anchor_report_issue"></a>
???+ note "How do I get help or report issues?"
    Need further help or have suggestions for the product or documentation? Reach out!

    [There are many ways to contact us, click here](/troubleshooting/#need-more-help){ .md-button .md-button--primary }