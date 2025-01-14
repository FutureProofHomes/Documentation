## Set Up Music Assistant

Your new Satellite1 can control your home now but what about streaming music? The good news is there's a giant 25 Watt amplifier built into Satellite1 and if you have a good speaker or headphones (and the appropriate [power supply](./recommended-accessories.md/) you'll be able to stream high-quality music to it with music assistant from Home Assistant.  Follow this excellent guide to get Music Assistant (MA) installed and configured to stream to your Satellite1.

!!! warning "Music Assistant get added to Home Assistant Core!"

    This is a great thing! It makes MA easier to install.  However, my understanding that this version of Music Assistant does not have "voice control capabilities" (yet).  So, as of December, 2024 we will recommend installing Music Assistant via the old-fashioned way - by using HACS (Home Assistant Community Store).

!!! tip "A Couple Tips:"

    1. Spotify ONLY works if you are a paying subscriber.  This may or may not be addressed in future versions of MA.
    2. Watch your volume!  The 25W amplifier on the Sat1 can blow little speakers.

[Install Music Assistant via HACS](https://music-assistant.io/integration/installation/#installation-of-the-deprecated-hacs-integration){ .md-button .md-button--primary }

## Add a Music Provider

After installing Music Assistant you'll want to add a source for your Music:

[Connect a Music Provider to MA](https://music-assistant.io/music-providers/){ .md-button .md-button--primary }

## Add your Sat1 to Music Assistat

1. <b>After adding a music provider you'll want to add your Satellite1 to MA, go to setttings:</b>
<br>![Music Assistant](/assets/MA0.png){ width="100%" loading=lazy }</br>

2. <b>Add Home Assistnat as Player Provider</b>
<br>![Music Assistant](/assets/MA1.png){ width="100%" loading=lazy }</br>
<br>![Music Assistant](/assets/MA2.png){ width="100%" loading=lazy }</br>

3. <b>Add your Satellite1 to the list of players:</b>
<br>![Music Assistant](/assets/MA3.png){ width="100%" loading=lazy }</br>
<br>![Music Assistant](/assets/MA4.png){ width="100%" loading=lazy }</br>

4. <b>That's it!  Select your Sattelite1 as your Player Provider & play some music.</b>
<br>![Music Assistant](/assets/MA5.png){ width="100%" loading=lazy }</br>
<br>![Music Assistant](/assets/MA6.png){ width="100%" loading=lazy }</br>

## Controlling Music with Your Voice

!!! warning "Beta Feature"

    These capabilities are still rough around the edges.  It will get better in time.  Read the documentation carefully before you conclude something broken.  In reality it may just not work as you expect :)

There are three ways to control music with your voice:

??? abstract "I want to control my music without an AI/LLM and have less capabilites."

    [Use Custom HA Intents to Control Music](https://music-assistant.io/integration/voice/#ha-assist){ .md-button .md-button--primary }

??? abstract "I want to control my music with an AI/LLM and have more capabilities that work often, but not perfectly."

    [Use OpenAI to Control Your Music](https://music-assistant.io/integration/voice/#ma-specific-conversation-agent){ .md-button .md-button--primary }

??? abstract "I want to control my music with an AI/LLM and have more capabilities that work often, but not perfectly."

    [Use a Local LLM to Control Your Music](https://music-assistant.io/integration/voice/#llm-conversation-agent){ .md-button .md-button--primary }