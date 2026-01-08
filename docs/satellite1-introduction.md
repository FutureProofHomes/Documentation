The Satellite 1 Developer Kit is the first version of our private voice assistant hardware and is the foundation for the larger ecosystem we're building.  The Dev Kit comprises of two PCB boards that we call the "Hat" (round board) and the "Core" (rectangular board).  When you connect these two components together you get the [Satellite1 Dev Kit](https://futureproofhomes.net/products/satellite1-pcb-dev-kit).

<figure markdown="span">
  <video width="100%" class="video-js" loop="" autoplay="" preload="none" muted="" playsinline="" poster="https://futureproofhomes.net/cdn/shop/files/0001.jpg?v=1732152100">
    <source src="https://cdn.shopify.com/videos/c/o/v/84cc43e4fb6a4d4bb303d9beab397b3f.mp4" type="video/mp4"></source>
  </video>
  <figcaption>Animation shows how to attach the rectangular Core Board to the round Hat Board, with an optional mmWave presence sensor.</figcaption>
</figure>

Your Satellite1 Dev Kit can also be installed in one of our many enclsoures and speaker kits to become a more complete product.  [Read more here](satellite1-smart-speaker-enclosure-kit.md).
<figure markdown="span">
  ![Smart Speaker Enclosure Kit Photoshoot](/assets/smart-speaker-enclosure-kit/white_gray_enclosure.jpg){ width="100%" }
  <figcaption>Purchase all the parts from us or build your own creation at home</figcaption>
</figure>

## Quick Live Demo
When properly set up the Satellite1 can be even more powerful than some of the mainstream voice assistants out there.  Watch the live demo section of our launch video to get a sense of the Satellite1 capabilities:

<iframe style="width: 100%; aspect-ratio: 16 / 9;" src="https://www.youtube.com/embed/RoGTLnAQEOY?si=KzaQY0I-9bBqWJge&amp;start=258" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Detailed Specifications & Features
You can read detailed sepecifications about the hardware on their product pages.

- [Satellite1 Dev Kit](https://futureproofhomes.net/products/satellite1-pcb-dev-kit)

## Requirements
The Satellite1 has a few requirements to get up and running.

1. An active installation of [Home Assistant](https://www.home-assistant.io/installation/)
2. A 2.4 GHz WiFi network (internet is not required)

## Satellite1 vs. Home Assistant Voice Preview Edition

The following table compares the main features of the Sat1 and Home Assistant Voice PE products.  Both products run the same ESP32-S3 and XMOS chip.  Our firmwares are also extremely similar (by design, to increase engagement and keep the community moving together). We think it is fair to say that the Sat1 is more feature rich and produces better sound.  Read below:

| Feature               | Satellite1                                                                                          | Home Assistant Voice PE                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| **Microphones**       | Four high-performance microphones (XMOS firmware uses two microphones currently.  Future firmware upgrade will utilize all 4 microphones). | Two microphones designed to hear voice commands in most environments.                 |
| **Speaker Output**    | 25W speaker amplifier capable of 48 kHz audio streaming. Also allows 3.5mm jack for external speakers. | Built-in 3W speaker for 48 kHz playback; includes a 3.5mm stereo jack for external speakers. |
| **Environmental Sensors** | Includes room temperature, humidity, and luminosity sensors; supports adding mmWave presence detection (LD2410 or LD2450). | Primarily focused on voice assistance; does not include additional environmental sensors. |
| **Form Factor**       | Available as a development kit with 4 buit-in buttons and components for assembly; official enclosure planned for future release. | Comes in a ready-to-use injection-molded case with physical controls, including a mute switch and volume dial. |                                   |
| **Power**             | Powered by USB-C PD (Power Delivery), enabling the extra power needed for the 25W amplifier.       | Powered by USB-C.                                                                      |
| **Expansion**         | Includes two 40-pin expansion connectors for powerful future accessories.                                   | Grove port for limited expansion.                                                               |
| **LED Ring**          | 24 LEDs for visual feedback.                                                                       | 12 LEDs for visual feedback.                                                           |
| **Software**          | [ESPHome Firmware very similar to Home Assistant Voice](https://github.com/FutureProofHomes/Satellite1-ESPHome)  | [ESPhome firmware for Home Assistant Voice](https://github.com/esphome/home-assistant-voice-pe)                                                           |