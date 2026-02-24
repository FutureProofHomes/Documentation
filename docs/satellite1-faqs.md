<a id="faq_anchor_factory_reset"></a>
???+ note "I messed something up, how do I start over?"

    1. [Remove the Sat1 from ESPHome](satellite1-troubleshooting.md/#removing-the-sat1from-esphome)
    2. [Flash the device back to factory firmware.](satellite1-flash-via-usb-c.md)

<a id="faq_anchor_inspect_logs"></a>
???+ note "How do I access the Sat1 logs?"

    [If you want to look at the logs, click here](/satellite1-troubleshooting/#inspecting-sat1-esp32-logs){ .md-button .md-button--primary }

<a id="faq_anchor_wake_words"></a>
???+ note "What wake words are supported?"
    
    The Satellite1 uses ESPHome's [microWakeWord](https://esphome.io/components/micro_wake_word.html) and supports the "Hey Jarvis" and "Okay Nabu" wake words.

<a id="faq_add_more_wake_words"></a>
???+ note "How do I add other wake words to the Sat1?"

    You'll need to [modify and compile your own Satellite1 firmware](/satellite1-modifying-the-firmware/) to add alternate compatible MicroWakeWords.  We recommend TaterTotterson's collection: 
    
    1. https://github.com/TaterTotterson/microWakeWords

<a id="faq_create_custom_wake_word"></a>
???+ note "How do create my own wake word?"

    You will need a GPU, knowledge, and sample data to train your own wake word.  Enjoy the journey and share what you create.  We recommend TaterTotterson's work: 
    
    1. https://github.com/TaterTotterson/microWakeWord-Trainer-Nvidia-Docker
    2. https://github.com/TaterTotterson/microWakeWord-Trainer-AppleSilicon

<a id="faq_anchor_wake_word_success"></a>
???+ note "The wake word isn't always responding!"
    
    1. Try both "Okay Nabu" and "Hey Jarvis" wake word.
    2. Increase the "Wake Word Sensitity" setting in the Sat1 ESPHome Device settings.
    3. Speak normally. Project your voice in the direction of the microphones. Don't scream.
    4. Ensure the microphones are unobstructed and the device isn’t placed in an enclosed space (like a shelf) or in a room with highly reflective surfaces (such as marble floors) that can cause echoes.
    5. Wake word detection may be more challenging for non-English speakers with accents or for higher-pitched voices (such as some women and children), as the wake words are not specifically trained for these voice profiles.  Read above to consider training your own wake word.
    6. Loud background noise—such as running water, wind, children shouting, oven hoods, or a TV—can significantly interfere with wake word detection, though XMOS firmware updates will continue to improve performance in these challenging conditions over time.
    7. Try creating your own wake word (See FAQ above)

    Still having issues? This will get better in time. We have lots of ideas to solve these problems.

<a id="faq_anchor_no_sound"></a>
???+ note "Why don’t I hear any audio through the speaker?"

    Ensure you're powering your Satellite1 using the USB-C port on the HAT labeled "CORE/ESP32".
    
    The other USB-C port on the HAT labeled "XMOS/SNDCARD" is intended for XMOS development only and will not enable the amplifier.

<a id="faq_anchor_distorted_sound"></a>
???+ note "Why does my speaker sound crackly, distored and possibly blown?"

    Your Sat1 is likely under-powered.  Check your "USB-C Power Draw" Sensor in the Sat1's ESPHome UI.  You should see approx. 30W of power.

<a id="faq_anchor_speaker_too_quiet"></a>
???+ note "My Sat1 speaker is too quiet.  I want moar boom in my music!"

    1. Ensure your Sat1 is receiving at least 30W or more of power by checking the "USB-C Power Draw" sensor in its ESPHome UI.
    2. In Music Assistant, open the Sat1 speaker’s Player Settings, disable both "Enable volume normalization (EBU-R128 based)" and "Enable limiting to prevent clipping" checkboxes, then increase the gain in Music Assistant’s DSP [(read more here)](/satellite1-streaming-music/#start-the-snapcast-server).

<a id="faq_anchor_report_issue"></a>
???+ note "How do I get help or report issues?"
    Need further help or have suggestions for the product or documentation? Reach out!

    [There are many ways to contact us, click here](/satellite1-troubleshooting/#need-more-help){ .md-button .md-button--primary }