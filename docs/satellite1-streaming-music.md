## Set Up Music Assistant

Your new Satellite1 can now control your home, but what about streaming music? Here’s a guide to help you install and configure Music Assistant (MA) to stream music directly to your Satellite1.

!!! warning "Music Assistant gets added to Home Assistant Core!"

    This is great news—it makes installing Music Assistant (MA) much easier! However, as of December 2024, it’s important to note that this version of Music Assistant does not yet include “voice control capabilities.” We recommend [reviewing Music Assistant’s guidelines on setting up voice control capabilities](https://www.music-assistant.io/integration/voice/) for the most up-to-date information.

[Install Music Assistant](https://www.music-assistant.io/installation/){ .md-button .md-button--primary }

## Add a Music Provider

After installing Music Assistant you'll want to add a source for your Music:

[Connect a Music Provider to MA](https://music-assistant.io/music-providers/){ .md-button .md-button--primary }

## Add your Sat1 to Music Assistant

1. <b>After adding a music provider, you'll want to add your Satellite1 to MA. Go to settings:</b>
<br>![Music Assistant](/assets/MA0.png){ width="100%" loading=lazy }</br>

2. <b>Add Home Assistant as Player Provider</b>
<br>![Music Assistant](/assets/MA1.png){ width="100%" loading=lazy }</br>
<br>![Music Assistant](/assets/MA2.png){ width="100%" loading=lazy }</br>

3. <b>Add your Satellite1 to the list of players:</b>
<br>![Music Assistant](/assets/MA3.png){ width="100%" loading=lazy }</br>
<br>![Music Assistant](/assets/MA4.png){ width="100%" loading=lazy }</br>

4. <b>That's it! Select your Satellite1 as your Player Provider & play some music.</b>
<br>![Music Assistant](/assets/MA5.png){ width="100%" loading=lazy }</br>
<br>![Music Assistant](/assets/MA6.png){ width="100%" loading=lazy }</br>

## Controlling Music with Your Voice

!!! warning "Beta Feature"

    These capabilities are still rough around the edges.  It will get better in time.  Read the documentation carefully before you conclude something broken.  In reality it may just not work as you expect :)

There are three ways to control music with your voice:

??? abstract "I want to control my music without an AI/LLM and have fewer capabilities."

    [Use Custom HA Intents to Control Music](https://github.com/music-assistant/voice-support?tab=readme-ov-file#option-1-local-assistant-blueprint){ .md-button .md-button--primary }

??? abstract "I want to control my music with a cloud-based AI/LLM and have more capabilities that work often, but not perfectly."

    [Use OpenAI to Control Your Music](https://github.com/music-assistant/voice-support?tab=readme-ov-file#option-2-local-assist-enhanced-by-an-llm-integration-like-open-ai-conversation-chatgpt-or-google-generative-ai-gemini){ .md-button .md-button--primary }

??? abstract "I want to control my music with an AI/LLM that I run locally and have more capabilities that work often, but not perfectly."

    [Use a Local LLM to Control Your Music](https://github.com/music-assistant/voice-support?tab=readme-ov-file#option-3-script-which-can-be-used-as-a-tool-by-an-llm-integration-like-open-ai-conversation-chatgpt-or-google-generative-ai-gemini){ .md-button .md-button--primary }
