The Smart Speaker is a Satellite1 that arrives finished. It ships pre-assembled and boxed, in Charcoal Gray or Bone White, with the firmware already installed. Unbox it, plug it in, and pair it.

![Charcoal Gray and Bone White Smart Speakers side by side](/assets/products/satellite1-desktop/hero.jpg){ width="100%" }

[Buy a Smart Speaker :material-cart:](https://futureproofhomes.net/products/satellite1-smart-speaker){ .md-button .md-button--primary }

## It is a real speaker

This is the part that separates the Smart Speaker from the other form factors. A Dev Kit on a bench can drive a speaker you supply. The Smart Speaker is a two-way design, woofer and tweeter through a crossover, in an enclosure built around the Hat's amplifier.

| | |
|---|---|
| **Woofer** | 3 inch mid-range, 15 W nominal and 20 W peak at 4 ohm, 80 Hz to 6 kHz |
| **Tweeter** | 1.2 inch neodymium dome, 15 W nominal and 20 W peak at 4 ohm, 2.5 kHz to 20 kHz |
| **Crossover** | Two-way passive |
| **Amplifier** | The Hat's 25 W mono output, driving both through the crossover |
| **Enclosure** | Sealed front chamber with a ported back chamber |

So it plays music properly rather than just acknowledging commands, which is why the firmware carries Sendspin and works with Music Assistant out of the box.

## Two colors, printed not molded

The enclosure is 3D printed in Bambu Lab PETG-HF, in Charcoal Gray or Bone White, with a multi-material top plate and a transparent LED diffuser so the 24-LED ring reads clearly through it.

Printing rather than molding is what makes the enclosure revisable. It is also why the models are published for anyone to print.

## Room for the options

The enclosure is designed with the add-ons in mind rather than retrofitted for them. The front chamber has a pocket for an LD2450 mmWave sensor, and the back chamber has a dedicated pocket for the external Wi-Fi antenna.

![Two Smart Speakers with their top plates removed, showing the Hat board](/assets/products/satellite1-desktop/pair-hat.jpg){ width="100%" }

*The top plate lifts off to reach the Hat board, which is how the mmWave sensor and antenna get fitted.*

## Or build one yourself

A Smart Speaker is three kits assembled: the Dev Kit for the boards, the Enclosure Kit for the printed parts, and the Electronics Kit for the drivers and crossover. You can also print the enclosure at home and buy only the parts that go inside it.

[Build it yourself :material-arrow-right:](satellite1-smart-speaker.md){ .md-button .md-button--primary }
[Print the enclosure :material-arrow-right:](satellite1-print-enclosure.md){ .md-button }

## Quick live demo

When properly set up the Satellite1 can be even more powerful than some of the mainstream voice assistants out there. Watch the live demo section of our launch video to get a sense of what it can do:

<iframe style="width: 100%; aspect-ratio: 16 / 9;" src="https://www.youtube.com/embed/n5yNEhcAjWU?si=mcycJb4gBk4zbLtX&amp;start=25" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Satellite1 vs. Home Assistant Voice Preview Edition

The following table compares the main features of the Sat1 and Home Assistant Voice PE products. Both products run the same ESP32-S3 and XMOS chip. Our firmwares are also extremely similar (by design, to increase engagement and keep the community moving together). We think it is fair to say that the Sat1 is more feature rich and produces better sound. Read below:

| Feature               | Satellite1                                                                                          | Home Assistant Voice PE                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| **Microphones**       | Four high-performance microphones (XMOS firmware uses two microphones currently.  Future firmware upgrade will utilize all 4 microphones). | Two microphones designed to hear voice commands in most environments.                 |
| **Speaker Output**    | 25W speaker amplifier capable of 48 kHz audio streaming. Also allows 3.5mm jack for external speakers. | Built-in 3W speaker for 48 kHz playback; includes a 3.5mm stereo jack for external speakers. |
| **Environmental Sensors** | Includes room temperature, humidity, and luminosity sensors; supports adding mmWave presence detection (LD2410 or LD2450). | Primarily focused on voice assistance; does not include additional environmental sensors. |
| **Form Factor**       | Available as a development kit or pre-assembled speaker. | Comes in a ready-to-use injection-molded case with physical controls, including a mute switch and volume dial. |                                   |
| **Power**             | Powered by USB-C PD (Power Delivery), enabling the extra power needed for the 25W amplifier.       | Powered by USB-C.                                                                      |
| **Expansion**         | Includes FX23L expansion connectors for powerful future accessories.                                   | Grove port for limited expansion.                                                               |
| **LED Ring**          | 24 LEDs for visual feedback.                                                                       | 12 LEDs for visual feedback.                                                           |
| **Software**          | [ESPHome Firmware very similar to Home Assistant Voice](https://github.com/FutureProofHomes/Satellite1-ESPHome)  | [ESPhome firmware for Home Assistant Voice](https://github.com/esphome/home-assistant-voice-pe)                                                           |
