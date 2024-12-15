## What is a Voice Pipeline?

Think about your interaction with any voice assistant:

1. **Wake Word** - You say a special phrase, like "Hey, Jarvis!"
2. **Speech-to-Text** - Your voice command is recorded and converted to a text transcription.
3. **Conversation Agent** - The text transcription is processed by a rules-based engine (or perhaps an LLM) which executes your command and generates a text response.
4. **Text-to-Speech** - The text response is converted into a synthetic voice response that is played back through the speaker.

That's a voice pipeline. It's the backbone of any voice assistant. Each step in a voice pipeline can be modified and customized to fit your needs. What wake word do you want? What language are you speaking? Do you want a standard voice response or to hear Arnold Schwarzenegger speak back to you? Do you want Home Assistant, Google, or OpenAI to process and execute your command? Follow the steps below to set up a voice pipeline for your Satellite1.

Please read all of the below. Then we highly recommend **[upgrading to a magical fallback conversation agent](/voice-pipeline/#magical-fall-back-conversation-agent)**. Also, don't forget to **[expose entities to your Satellite1 voice assistant!](/voice-pipeline/#exposing-entities)**

## General Steps to Create a Voice Pipeline:

1. Go to **Settings -> Voice Assistants -> Add Assistant**
   <img width="60%" alt="image" src="/assets/Pipeline0.png">

2. Name your pipeline. Select your preferred Conversation Agent, Speech-to-Text, and Text-to-Speech engine.
   <img width="60%" alt="image" src="/assets/Pipeline1.png">

## Standard Home Assistant Conversation Agents

There are two standard voice pipelines we recommend trying out to get your feet wet:

???+ abstract "Home Assistant's Cloud Assist Pipeline (Requires paid Home Assistant Cloud account, response times are fast!)"
    [Set up Cloud Assist Pipeline](https://www.home-assistant.io/voice_control/voice_remote_cloud_assistant/){ .md-button .md-button--primary }

???+ abstract "Home Assistant's Local Assist Pipeline (Free and completely private, response times depend on your hardware)"
    [Set up Local Assist Pipeline](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/){ .md-button .md-button--primary }

## Generative A.I. Conversation Agents

Once you have one of the standard pipelines above operational, you can decide to upgrade to a Generative AI conversation agent.

???+ abstract "Ollama AI Powered Conversation Agent (Free, requires a GPU, and can be hard to set up with proper function calling.)"
    [Set up Ollama Conversation Agent](https://www.home-assistant.io/integrations/ollama/){ .md-button .md-button--primary }

???+ abstract "Google A.I Powered Pipeline (Free, but will collect your data)"
    ???+ danger "Warning: You're giving a company with non-deterministic artificial intelligence ability control of your home and collect data on your usage. Be cautious!"
    [Set up Google AI Conversation Agent](https://www.home-assistant.io/integrations/google_generative_ai_conversation/){ .md-button .md-button--primary }

???+ abstract "OpenAI ChatGPT Powered Pipeline (Expensive, and not open at all, despite the marketing name.)"
    ???+ danger "Warning: You're giving a company with non-deterministic artificial intelligence ability control of your home and collect data on your usage. Be cautious!"
    [Set up OpenAI ChatGPT Conversation Agent](https://www.home-assistant.io/integrations/openai_conversation/){ .md-button .md-button--primary }

## Magical "Fall back" Conversation Agent

???+ abstract "Combine a standard conversation agent with an AI conversation agent (It's like magic!)"
    ???+ tip "Requires Home Assistant version 2024.12.1 or later"
    A "fall back" pipeline will first use a non-AI conversation agent to process your request, and if that fails it will _fall back_ to your preferred AI conversation agent. Combining these two conversation agents results in an almost magical voice experience and is highly recommended.

    Simply toggle on the **"Prefer handling commands locally"** switch underneath your Generative AI conversation agent:
    <img width="60%" alt="image" src="/assets/googleGPT0.png">

    [Read more about this feature release](https://www.home-assistant.io/blog/2024/12/04/release-202412/#let-your-voice-assistant-fall-back-to-an-llm-based-agent){ .md-button .md-button--primary }

## Assign a Voice Pipeline & Wake Word to your Satellite1

1. Go to **Settings -> Devices & Services -> ESPHome** and click "1 device" under your Satellite1 device.
   <img width="60%" alt="image" src="/assets/Pipeline4.png">

2. In the Configuration section, select your Voice Pipeline.
   <img width="60%" alt="image" src="/assets/Pipeline5.png">

3. You can also set your preferred wake word. (NOTE: If you want to build your own custom wake word, then [read here](/faqs#faq_anchor_custom_wake_word))
   <img width="60%" alt="image" src="/assets/Pipeline7.png">

Congratulations! You've created your own voice pipeline for your Satellite1.

## Exposing Entities

Your home assistant likely has hundreds if not thousands of entities. If you want to use them in your voice assistant, then you need to expose them to your voice assistant. Here's how:

1. Go to **Settings -> Voice Assistants -> Expose** and select the entities you want to control via your voice assistant.
   <img width="60%" alt="image" src="/assets/Expose Entities.png">

2. Enable the "Assist" toggle switch and consider adding alias names that you might use when referring to the entity.
   <img width="60%" alt="image" src="/assets/Expose Settings.png">

   [Back to Top](./voice-pipeline.md/#what-is-a-voice-pipeline)