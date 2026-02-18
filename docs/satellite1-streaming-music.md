This guide will show you how to stream multi-room syncronized music to one or many Sat1 devices around your home using [Music-Assistant.io](https://www.music-assistant.io/).  You can stream from Spotify, Apple Music, Tidal etc.  And your Sat1 speaker can operate as a Spotify Connect speaker or Airplay speaker so you can stream music directly from your phone.

## Install Music Assistant
There are a many ways to install Music Assistant in your home.  Read their documentation to get started.

[Install Music Assistant](https://www.music-assistant.io/installation/){ .md-button .md-button--primary }

---

## Add a Music Provider

Add a music source provider like Spotify, Apple Music, YouTube Music, or many other sources by following the instructions below.

!!! INFO "Some of the music providers require a paid subscription to use within Music Assistant."

[Connect a Music Provider to MA](https://music-assistant.io/music-providers/){ .md-button .md-button--primary }

---

## Start the Snapcast Server

We recommend connecting your Sat1 to Music Assistant using the built-in Snapcast server. This enables flexible audio streaming in the following configurations:

- **Single Speaker** – Stream audio to one Satellite1 speaker.
- **Stereo Pair** – Connect two Satellite1 speakers as a left/right stereo pair.
- **Multi-Room Audio** – Sync two or more Satellite1 speakers for synchronized playback across multiple rooms (similar to Sonos).

_NOTE: Yes we plan to support Nabu Casa's Sendspin protocol after futher development.  However, as of Feb 2026 we find Snapcast to be more reliable._

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Start your Snapcast Server__

    ---

    ![Install Snapserver](/assets/MA_add_snapserver.png){ loading=lazy }  
    In Music Assistant navigate to **"Settings -> Providers -> Add a new provider"** and select **"Snapcast"** to install the Snapserver. Leave all the server settings at default.  Your Satellite1 speakers will automatically appear in Music Assistant.

-   :material-numeric-2-circle:{ .lg .middle } __Configure Your Speakers__

    ---

    ![Name Sat1 Snapcast Speaker](/assets/MA_user_friendly_name.png){ loading=lazy }  
    In Music Assistant, edit each speaker’s settings by navigating to **"Settings -> Players"** then click **"Configure"** next to each speaker.  Assign a clear, recognizable name to every device.

    We also strongly recommend disabling the **“Enable volume normalization”** setting in each speaker’s configuration.  Alternatively you could leave volume normalization enabled and change the target level in the speakers **Advanced Settings** section at the bottom of the page.  
    
    This ensures your Sat1 speaker can reach its full output level and perform at maximum volume.  

</div>

!!! INFO "Snapcast Network Requirements"
    - Ports 1704 & 1705 must be open for the Snapserver to communicate with the Sat1 Snapclient.
    - Ports 4953 through 5153 must be open per [Music Assistant's Snapcast requirements](https://www.music-assistant.io/player-support/snapcast/).
    - mDNS is recommended for the Snapserver to autodetect the Sat1 Snapclient.

!!! info "Sat1 Snapcast Speaker(s) Missing?"
    - Check that the correct ports are open and mDNS is operational.
    - Toggle Snapcast off/on in the Sat1 ESPHome device settings.
    - Manually add your Snapserver's IP address to the Sat1's firmware.  [Read more here.](/satellite1-modifying-the-firmware)


## Controlling Snapcast Speaker Groups

This is how you dynamically add/remove Sat1 speakers to a group for synchronized multi-room music playback.

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Play Music on Main Speaker__

    ---

    ![Play Music on Main Speaker](/assets/MA_main_speaker.png){ loading=lazy }  
    Click a track, choose **"Play On"**, select your main speaker, then click the track again and choose **"Play Now"**.

-   :material-numeric-2-circle:{ .lg .middle } __Show All Speakers__

    ---

    ![Show other Sat1 Snapclient speakers](/assets/MA_show_speakers.png){ loading=lazy }  
    Open the Now Playing side panel by clicking the **:material-speaker: icon**.

-   :material-numeric-3-circle:{ .lg .middle } __Manage Speaker Group__

    ---

    ![Add or Remove Speakers from group](/assets/MA_select_speaker_groupings.png){ loading=lazy }  
    Click in the blank area next to the song tile to expand and view all Snapcast speakers. Select or deselect speakers to add or remove them from the group.

    !!! Info "Sat1 Snapcast Speaker(s) Drifting Out of Sync or Stuttering?"
        - Inspect Sat1 ESPHome Device settings to make sure it has a strong WiFi connection
        - Restart the Snapcast Server from Music Assistant's Music Provider settings
        - Toggle Snapcast off/on in the Sat1 ESPHome device settings
        - Turn off Music Assistant DSP Equalizer
        - Run your own Snapserver instead of the one built-in to Music Assistant
</div>

---

## Setup Snapcast Stereo Playback & Static Grouping

This feature lets you semi-permanently group Sat1 speakers, such as combining all your upstairs speakers into one group or pairing two Sat1 speakers for stereo sound.

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Create a Group Player__

    ---

    ![Create a Group](/assets/MA_snapcast_speakers.png){ loading=lazy }  
    Go to MA **"Settings -> Players"** and select **"Add Group Player"**.

-   :material-numeric-2-circle:{ .lg .middle } __Name the Stereo Pair Group__

    ---

    ![Name the Stereo Pair](/assets/MA_stereo_pair.png){ loading=lazy }  
    Select **"Snapcast Group Type"**. Keep **"Dynamic Group"** off. Give the group a name and add the two Sat1 speakers you want in the stereo pair.

-   :material-numeric-3-circle:{ .lg .middle } __Set Channel Output__

    ---

    ![Set speaker to correct channel](/assets/HA_channel_selection.png){ loading=lazy }  
    In Home Assistant, navigate to **"Settings -> Devices & Services -> ESPHome"** and set the correct **"Speaker Channel Output"** for each speaker.

    !!! Info "Tips:"
        - Channel selection only relates to the built-in speaker and not audio coming out of the headphone jack.
        - If Music Assistant's volume control is not controlling all speakers in the group, then restart things.

</div>

---

## DSP to Achieve Better Sound

Using Music Assistant's DSP equalizer can significantly improve the sound quality of your Sat1.

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Open Speaker DSP Settings__

    ---

    ![Open Speaker DSP Settings](/assets/MA_open_DSP_settings.png){ loading=lazy }  
    Go to MA **"Settings -> :material-speaker: icon"** and select **"Open DSP Settings"**.

-   :material-numeric-2-circle:{ .lg .middle } __Adjust DSP__

    ---

    ![Equalize Audio](/assets/MA_DSP_settings.png){ loading=lazy }  
    Adjust the DSP settings to your liking.

    !!! info "Read about DSP"
        - [DSP Parametric EQ](https://www.music-assistant.io/dsp/parametriceq/)
        - [DSP Tone Controls](https://www.music-assistant.io/dsp/tonecontrols/)

</div>

!!! Warning "DSP & Snapcast Speaker Grouping"

    When multiple speakers are added to a Snapcast group your Music Assistant DSP settings are not rendered.  We've opened a PR with Music Assistant to temporarily workaround this issue and in the future we plan to introduce Gain and EQ control directly within the Satellite1.

---

## Controlling Music with Your Voice

!!! Warning "Beta Feature Zone!"

    These capabilities are still rough around the edges. Please be patient. :)

Not only do we want to say, *"Hey Jarvis, turn down the volume"* or *"Hey Jarvis, play the next song"*, but we also want to say, *“Hey Jarvis, play the Beatles,”* and have it play on that speaker (or at least ask which speaker to use). Currently, this is hard to do, but not impossible.

To achieve all this, I highly recommend reading [Music Assistant’s Voice Support Repository](https://github.com/music-assistant/voice-support). However, I have personally found these implementations to be cumbersome and unreliable and instead have been using a different solution I'll share here (although it does currently require cloud AI).

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Cloud AI Conversation Agent__

    ---

    ![Cloud AI Pipeline](/assets/MA_google_ai_pipline.png){ loading=lazy }  
    Use a voice pipeline with a Cloud AI conversation agent. Tick on **"Prefer handling commands locally"** to get the best results.

-   :material-numeric-2-circle:{ .lg .middle } __Edit Speaker Device__

    ---

    ![Edit MA Speakers in HA](/assets/MA_integration_speaker_naming.png){ loading=lazy }  
    In Home Assistant, navigate to **"Settings -> Devices & Services -> Music Assistant"** and open the context menu to **"Edit Device"** for each speaker.

-   :material-numeric-3-circle:{ .lg .middle } __Good Naming Conventions__

    ---

    ![Name Device](/assets/MA_name_device.png){ loading=lazy }  
    Give the device an intuitive name. Be sure to assign an area. Click **Update**.

-   :material-numeric-4-circle:{ .lg .middle } __Entity Settings__

    ---

    ![Name Device](/assets/MA_expose_speaker.png){ loading=lazy }  
    Click on the newly renamed device to see all its entities. Then click on the actual media player entity in the controls section. Click the **settings :gear: icon**.

-   :material-numeric-5-circle:{ .lg .middle } __Expose Speaker to Assist__

    ---

    ![Name Device](/assets/MA_voice_assistant.png){ loading=lazy }  
    Click on **"Voice assistants"** and toggle on **"Assist"** to expose the Music Assistant speaker to your voice assistant.

</div>

!!! Info "My Results:"
    - Playing a song by **artist** or **track name** works fairly well.  
    - If you don’t specify a speaker, it *sometimes* chooses the right one automatically; therefore it is best to **explicitly specify which speaker** you want to control.  
    - You **can’t control multiple speakers** in an area (yet).  
    - You **can’t group or ungroup Snapcast speakers** (yet).  