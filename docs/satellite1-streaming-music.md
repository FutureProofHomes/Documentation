This guide will show you how to stream syncronized music to one or many Sat1 devices around your home using Music Assistant, an open-source music player for Home Assistant that supports a wide range of providers, including Spotify, Apple Music, YouTube Music, and more.

## Install Music Assistant
There are a few ways to install Music Assistant. Please read more here:

[Install Music Assistant](https://www.music-assistant.io/installation/){ .md-button .md-button--primary }

---

## Add a Music Provider

Add a music provider like Spotify, Apple Music, YouTube Music, or many other sources by following the instructions below.

!!! INFO "You must have a paid subscription to some of these music providers to use them with Music Assistant."

[Connect a Music Provider to MA](https://music-assistant.io/music-providers/){ .md-button .md-button--primary }

---

## Add Sat1 via Home Assistant Protocol

If you don't care about synchronized multi-room music playback, this is a great way to get started.  

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Add HA Player Provider__

    ---

    ![Connect HA to MA](/assets/MA1.png){ loading=lazy }  
    Go to **"Settings -> Add Player Provider"** and select **"Home Assistant MediaPlayers"**.

-   :material-numeric-2-circle:{ .lg .middle } __Import HA Media Players__

    ---

    ![Name Sat1 HA speaker](/assets/MA3.png){ loading=lazy }  
    Select the Home Assistant media players you want Music Assistant to stream music to.

-   :material-numeric-3-circle:{ .lg .middle } __Name Your HA Speakers__

    ---

    ![Name Sat1 HA speaker](/assets/MA_name_ha_speaker.png){ loading=lazy }  
    Go to MA **"Settings -> :material-speaker: icon"** and select **"Configure"**. Name your Sat1 and keep the HA settings at default.

</div>

!!! INFO "Sendspin Support Coming Soon"
    Please stay tuned to future firmware updates.

---

## Add Sat1 via Snapcast Protocol

If you have multiple Satellite1 devices, you can use our Snapcast implementation to stream synchronized multi-room music or even pair two Sat1 speakers together for true left/right stereo sound.

!!! INFO "Software Requirements"
    - Sat1 must be running firmware v1.0.3 or higher.
    - Home Assistant should be running 2025.7.x or higher.
    - Music Assistant should be running 2.5.7 or higher.
  
!!! INFO "Network Requirements"
    - Ports 1704 & 1705 must be open for the Snapserver to communicate with the Sat1 Snapclient.
    - Ports 4953 through 5153 must be open per [Music Assistant's Snapcast requirements](https://www.music-assistant.io/player-support/snapcast/).
    - mDNS is recommended for the Snapserver to autodetect the Sat1 Snapclient.

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Add Snapcast Player Provider__

    ---

    ![Install Snapserver](/assets/MA_add_snapserver.png){ loading=lazy }  
    Go to MA **"Settings -> Add Player Provider"** and select **"Snapcast"** to install the Snapserver. Leave all the server settings at default.

-   :material-numeric-2-circle:{ .lg .middle } __Name Your Sat1 Snapcast Speakers__

    ---

    ![Name Sat1 Snapcast Speaker](/assets/MA_user_friendly_name.png){ loading=lazy }  
    Go to MA **"Settings -> :material-speaker: icon"** and select **"Configure"**. Name your Sat1 and keep the Snapclient settings at default.

    !!! info "Sat1 Snapcast Speaker(s) Missing?"
        - Power cycle the Sat1.
        - Play music on any visible Snapcast speaker to view the hidden speakers grouped with it.  This can happen after snapserver restarts.
        - Check that the correct ports are open.
        - Manually add your Snapserver's IP address to the Sat1's firmware.  [Read more here.](/satellite1-modifying-the-firmware)

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

    When multiple speakers are added to a Snapcast group your Music Assistant DSP settings are not rendered.  We've opened a PR with Music Assistant to temporarily workaround this issue and in the future we will introduce Gain and EQ control directly within the Satellite1.

---

## Snapcast Multi-Room Music Playback & Dynamic Grouping

This will enable you to dynamically add or remove speakers to a group for synchronized multi-room music playback.

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
        - Restart the Snapcast Server from Music Assistant's Music Provider settings
        - Restart Sat1
        - Turn off Music Assistant DSP Equalizer on all speakers
        - Run your own Snapserver instead of the one built-in to Music Assistant 
        - Make sure your Sat1 has a reliable Wi-Fi connection

</div>

---

## Snapcast Multi-Speaker Stereo Playback & Static Grouping

This feature lets you semi-permanently group Sat1 speakers, such as combining all your upstairs speakers into one group or pairing two Sat1 speakers for stereo sound.

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Create a Group Player__

    ---

    ![Create a Group](/assets/MA_snapcast_speakers.png){ loading=lazy }  
    Go to MA **"Settings -> :material-speaker: icon"** and select **"Add Group Player"**.

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