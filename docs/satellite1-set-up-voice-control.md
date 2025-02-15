In this section we will configure your Satellite1 so it can control smart devices in your home intuitively.  By the end of this section you should be able to say:

- "Hey Jarvis, are any doors unlocked in the home?"
- "Hey Jarvis, lock those doors please."
- "Hey Jarvis, what is the difference between a black hole and white hole?"
- "Hey Jarvis, close the garage door and turn on the TV then tell me a joke."

## What is a Voice Pipeline?

Think about your interaction with any voice assistant:

1. **Wake Word** - You say a special phrase, like "Hey, Jarvis!"
2. **Speech-to-Text** - Your voice command is recorded and converted to a text transcription.
3. **Conversation Agent** - The text transcription is processed by a rules-based engine (or perhaps an LLM) which executes your command and generates a text response.
4. **Text-to-Speech** - The text response is converted into a synthetic voice response that is played back through the speaker.

That's a voice pipeline. It's the backbone of any voice assistant. Each step in a voice pipeline can be modified and customized to fit your needs. What wake word do you want? What language are you speaking? Do you want a standard voice response or to hear Arnold Schwarzenegger speak back to you? Do you want Home Assistant, Google, or OpenAI to process and execute your command? Follow the steps below to set up a voice pipeline for your Satellite1.

## Create a Voice Pipeline:

1. Go to **Settings -> Voice Assistants -> Add Assistant**
   <br>![Create Pipeline](/assets/Pipeline0.png){ width="100%" loading=lazy }>


2. **Name your pipeline. Select your preferred Conversation Agent, Speech-to-Text, and Text-to-Speech engine.**  
   <br>![Configure Pipeline](/assets/Pipeline1.png){ width="100%" loading=lazy }>

## Standard Conversation Agents

There are two standard voice pipelines we recommend trying out to get your feet wet:

???+ abstract "Home Assistant's Cloud Assist Pipeline (Requires paid Home Assistant Cloud account, response times are fast!)"
    [Set up Cloud Assist Pipeline](https://www.home-assistant.io/voice_control/voice_remote_cloud_assistant/){ .md-button .md-button--primary }

???+ abstract "Home Assistant's Local Assist Pipeline (Free and completely private, response times depend on your hardware)"
    [Set up Local Assist Pipeline](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/){ .md-button .md-button--primary }

## Local AI Conversation Agents

???+ tip " The FutureProofHomes team is working on a [Local AI Base Station](https://futureproofhomes.net/pages/ai-base-station) that "just works". Therefore, these docs will avoid sending you down a deep local AI rabbit hole. :) Thanks for your patience & stay tuned!"

Once you have one of the standard pipelines operational, you can upgrade to a Generative AI conversation agent. These agents allow the voice assistant to respond to more natural, conversational commands like, “It’s dark in here,” to turn on the lights, instead of requiring specific phrases like, “Turn on the living room lights.” Implementing completely local Generative AI LLMs, however, is not for the faint of heart. Your results may vary depending on factors such as the model you choose (e.g., Llama, Qwen, etc.), the number of entities exposed, how those entities and their aliases are named, the GPU’s capabilities (more VRAM is better), and many other variables. If you’re ready to take on this challenge, [here are some tutorial videos to help you get started](https://www.youtube.com/results?search_query=ollama+llama+home+assistant). Good luck!

???+ abstract "Ollama AI Powered Conversation Agent (Free, requires a GPU, and can be hard to set up with simi-reliable function calling.)"
    [Set up Ollama Conversation Agent](https://www.home-assistant.io/integrations/ollama/){ .md-button .md-button--primary }


## Cloud AI Conversation Agents

???+ danger "Warning: You are entrusting a cloud-based artificial intelligence that does not protect your privacy with control over your home. Proceed with caution!"

???+ abstract "Google AI Conversation Agent (Free, but will collect your data.)"
    [Set up Google AI Conversation Agent](https://www.home-assistant.io/integrations/google_generative_ai_conversation/){ .md-button .md-button--primary }

???+ abstract "OpenAI ChatGPT Conversation Agent (Expensive, and not open at all, despite the marketing name, and will collect your data.)"
    [Set up OpenAI ChatGPT Conversation Agent](https://www.home-assistant.io/integrations/openai_conversation/){ .md-button .md-button--primary }

NOTE: The following prompt has perfomed well with both OpenAI and Google's conversation agents.

```
Your name is Jarvis and you are a voice assistant for Home Assistant.
Answer questions about the world truthfully.
Answer in plain text without markdown language. 
Keep responses simple and to the point.
Always use 12hr time formats.
```

<br>![Add Prompt](/assets/prompt.png){ width="100%" loading=lazy }>

## Combine Conversation Agents

???+ abstract "Combine a standard conversation agent with an AI conversation agent (It's like magic!)"
    ???+ tip "Requires Home Assistant version 2024.12.1 or later"
    A "fall back" pipeline will first use a non-AI conversation agent to process your request, and if that fails it will _fall back_ to your preferred AI conversation agent. Combining these two conversation agents results in an almost magical voice experience and is highly recommended.

    Simply toggle on the **"Prefer handling commands locally"** switch underneath your Generative AI conversation agent:
   <br>![Prefer handling commands locally](/assets/googleGPT0.png){ width="100%" loading=lazy }>

    [Read more about this feature release](https://www.home-assistant.io/blog/2024/12/04/release-202412/#let-your-voice-assistant-fall-back-to-an-llm-based-agent){ .md-button .md-button--primary }

## Assign a Voice Pipeline

1. Go to **Settings -> Devices & Services -> ESPHome** and click **"1 device"** under your Satellite1 device.  
   <br>![Go to Device](/assets/Pipeline4.png){ width="100%" loading=lazy }>

2. **In the Configuration section, select your Voice Pipeline.**  
   <br>![Assistant Dropdown](/assets/Pipeline5.png){ width="100%" loading=lazy }>

3. **You can also set your preferred wake word. (NOTE: If you want to build your own custom wake word, then [read here](/faqs#faq_add_more_wake_words))**  
   <br>![Set Wake Word](/assets/Pipeline7.png){ width="100%" loading=lazy }>

Congratulations! You've created your own voice pipeline for your Satellite1.

## Exposing Entities

Your home assistant likely has hundreds if not thousands of entities. If you want to use them in your voice assistant, then you need to expose them to your voice assistant. Here's how:

1. Go to **Settings -> Voice Assistants -> Expose** and select the entities you want to control via your voice assistant.
   <br>![Select entities to expose](/assets/Expose Entities.png){ width="100%" loading=lazy }</br>

2. Enable the "Assist" toggle switch and consider adding alias names that you might use when referring to the entity.
   <br>![Add aliases](/assets/Expose Settings.png){ width="100%" loading=lazy }</br>