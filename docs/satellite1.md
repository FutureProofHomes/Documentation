Every Satellite1 is built from the same two circuit boards.

A Smart Speaker on a shelf, a flush-mounted enclosure in a ceiling, and a bare pair of boards on a workbench all run the same silicon, the same firmware and the same sensors. The only thing that changes is the box around them.

We did that on purpose. One set of electronics means there is only one firmware to maintain and one set of instructions to follow, so a fix written for the desktop unit reaches the in-ceiling one in the same release. It also means you can repair or upgrade part of a Satellite1 instead of replacing all of it.

![The Satellite1 Hat board with its Wi-Fi antenna, USB-C cable and power adapter](/assets/products/satellite1-dev-kit/hero.jpg){ width="100%" }

*The Hat board, the external Wi-Fi antenna and USB-C power. This is what sits inside a Smart Speaker and behind a ceiling grille, and it is also what you get on its own as a Dev Kit.*

## Satellite1 is a platform

Most hardware companies ship a product, and a year later they ship a different one. The two share a brand and not much else. Different board, different firmware, different accessories, and a separate end of life for each.

Satellite1 works the other way round. Satellite1 itself is the platform, and the Smart Speaker, the In-Ceiling Enclosure and the Dev Kit are products built on top of it.

| | |
|---|---|
| **Products**<br>What you buy. A packaging decision, not a capability one | Smart Speaker · In-Ceiling Enclosure · Dev Kit |
| **Platform**<br>Identical in every Satellite1 ever shipped | Core board · Hat board · ESPHome · Sendspin |

### Two boards and two protocols

The Core and the Hat are the hardware half of the platform. The software half is just as consistent.

The firmware is built with [ESPHome](https://esphome.io/). That matters more than it sounds. It is why a Satellite1 turns up in Home Assistant as a proper device with no custom integration to install, why every sensor and button appears as an entity on its own, and why you can [fork the whole firmware](https://github.com/FutureProofHomes/Satellite1-ESPHome) if you want your hardware to do something we never planned for.

Audio runs on Sendspin, Nabu Casa's streaming protocol, which replaced Snapcast in v0.2.0. It works with Music Assistant straight away, with no provider setup, port configuration or server to install, and it is what keeps several Satellite1 units playing in sync with each other.

Those four pieces are what we mean by the platform. Everything else is how it gets packaged.

The distinction matters for three reasons.

### Updates reach hardware you already own

Because every unit runs the same silicon, a change to the platform lands on hardware that is already installed in people's homes. The Hat has four microphones and the current firmware uses two of them, so switching the other two on is a firmware release rather than a new speaker. Snapcast being replaced by Sendspin worked the same way. Attach an mmWave radar and the firmware works out which model it is and exposes the right entities without a reflash. Buying a Satellite1 early does not leave you stuck with the worst version of it.

### Form factor does not change what it can do

Choosing between a desktop unit and a ceiling enclosure is a decision about the room, not about capability. The microphones, amplifier, sensors and Home Assistant integration are the same either way, and there is no premium tier holding anything back. The choice is reversible too, since the boards move between enclosures.

### You can extend it yourself

The [firmware is on GitHub](https://github.com/FutureProofHomes/Satellite1-ESPHome), the enclosure models are published for anyone to print, and the Hat has an FX23L expansion connector for hardware that does not exist yet. The Hat will even physically mount to a Raspberry Pi instead of a Core, though that one is an experiment rather than a product.

So the products listed below are not the full list of things a Satellite1 can be. They are the ones we have packaged, and a Dev Kit and a 3D printer are enough to add to the list.

!!! warning "Raspberry Pi is not officially supported"

    The Hat board will mount to a Raspberry Pi instead of a Core, and there is an [alpha firmware](https://github.com/FutureProofHomes/Satellite1-RPi-Image) you are welcome to try. It is there to play with, not to rely on. We do not provide support for it, and we cannot promise it will keep working or that it will ever become a supported configuration. If you want to experiment, other people trying it are in the [Discord community](https://discord.futureproofhomes.net).

## The two boards

<div class="grid cards" markdown>

-   __Core board__

    ![The rectangular Satellite1.1 Core board](/assets/products/satellite1-dev-kit/core-board.jpg){ width="100%" }

    The rectangular one. An ESP32-S3 that runs the ESPHome firmware and handles Wi-Fi and Bluetooth.

-   __Hat board__

    ![The round Satellite1.1 Hat board](/assets/products/satellite1-dev-kit/hat-board-top.jpg){ width="100%" }

    The round one. It carries the XMOS XU316 audio processor, the microphone array, the 25 W amplifier, the LED ring, the buttons and the environmental sensors.

</div>

They stack. The Core mounts onto the Hat, and that assembly is a Satellite1. The enclosure, drivers, crossover and mounting hardware are all packaging around it.

## Core board

The Satellite1.1 Core runs the ESPHome firmware and does the talking to Home Assistant.

| | |
|---|---|
| **Processor** | ESP32-S3, dual-core 32-bit LX7 @ 240 MHz |
| **Memory** | 512 KB SRAM, 16 MB flash, 8 MB PSRAM |
| **Radios** | 2.4 GHz Wi-Fi, Bluetooth 5 (LE) |
| **Antenna** | External, IPEX connector, required on the 1.1 |

!!! warning "The 1.1 will not reach Wi-Fi without its antenna"

    The Satellite1.1 Core, which is what has shipped since February 17, 2026, uses an external antenna rather than one on the board. It is not an accessory. Without it the board does not get on the network at all.

    If the supplied antenna is too large for your installation, any antenna with an IPEX connector will work. The previous generation Core has the antenna built in and needs nothing.

## Hat board

The Satellite1.1 Hat is where the voice assistant actually happens.

| | |
|---|---|
| **Audio processor** | XMOS XU316, 16-core 32-bit RISC @ 800 MHz, 1024 KB SRAM, 8 MB flash |
| **Microphones** | Four-microphone array |
| **Amplifier** | 25 W mono (TAS2780) |
| **Line out** | 3.5 mm jack (PCM5122) |
| **Feedback** | 24-LED ring, 4 tactile buttons |
| **Environment** | Ambient light (LTR-303ALS), temperature and humidity (AHT20) |
| **Presence** | Headers for LD2410 or LD2450 mmWave radar, plus a 4-pin JST LD2450 connector underneath |
| **Expansion** | FX23L connector |
| **Connectors** | USB-C labelled CORE/ESP32, SPKR OUT for a driver, 4-pin JST for mmWave, 40-pin header for the Core |
| **Power in** | USB-C Power Delivery, 30 W recommended, supports up to 20 V @ 5 A |

!!! note "Four microphones, two in use"

    The array has four microphones and the current XMOS firmware uses two of them. Switching the other two on is a firmware upgrade rather than new hardware, so it will reach boards that are already in the field.

The 1.1 Hat has a single USB-C, labelled CORE/ESP32, so there is only one place power can go. The board also carries an XMOS/SNDCARD silkscreen beside it, but those pads are unpopulated on this revision. Earlier Hats did fit a second connector there, which is why older instructions warn about using the wrong one.

USB-C PD is doing real work here rather than just charging. The 25 W amplifier needs the headroom, so an underpowered supply usually shows up as quiet or distorted audio rather than as a power fault.

Having a dedicated 800 MHz audio processor next to the ESP32 is why wake word detection and echo cancellation keep working while music is playing. The ESP32 never has to choose between listening and getting on with its job.

## How it compares

The other two local voice devices people weigh a Satellite1 against are the Home Assistant Voice Preview Edition and the Third Reality Voice/Music Assistant. Both are finished voice devices. The difference is less about any single specification and more about what happens after you buy one.

| | Satellite1 | Home Assistant Voice PE | Third Reality Voice/Music Assistant |
|---|---|---|---|
| **Microphones** | Four, two in use | Two | Two |
| **Audio processor** | XMOS XU316 | XMOS XU316 | No dedicated processor published |
| **Environmental sensors** | Temperature, humidity, ambient light | None | None listed |
| **Presence** | LD2450 mmWave | None | None listed |
| **Expansion** | FX23L connector | Grove port | None listed |
| **Network** | 2.4 GHz Wi-Fi, optional PoE1 | 2.4 GHz Wi-Fi | 2.4 GHz Wi-Fi |
| **Firmware** | ESPHome | ESPHome | Custom Linux on an ARM A53 |

Two honest notes on that table. The audio processor row is a tie, because Voice PE runs the same XMOS part we do, and our firmwares are deliberately similar so the community moves together. And the Third Reality unit is a Linux satellite rather than an ESPHome device, which makes it a different kind of thing rather than a worse one.

What the table does show is the extension story. The sensors, the mmWave headers, the expansion connector and the PoE option are all there because a Satellite1 is meant to be the thing in the room that does several jobs, not only the thing you talk to.

Audio output is a separate question, and it is compared on the
[Smart Speaker overview](satellite1-introduction.md#how-that-compares).

## Pick a form factor

<div class="grid cards" markdown>

-   ![Charcoal Gray and Bone White Smart Speakers](/assets/products/satellite1-desktop/hero.jpg){ width="100%" }

    __Smart Speaker__

    Pre-assembled and boxed, in Charcoal Gray or Bone White. Unbox it, power it, talk to it.

    [Buy](https://futureproofhomes.net/products/satellite1-smart-speaker){ .md-button }
    [Docs](satellite1-introduction.md){ .md-button }

-   ![The Satellite1 Core and Hat boards with antenna and power adapter](/assets/products/satellite1-dev-kit/kit-contents-with-core.jpg){ width="100%" }

    __Dev Kit__

    Core and Hat, antenna and power, and nothing else. It runs perfectly well bare on a bench, and it is the starting point if you want to build your own.

    [Buy](https://futureproofhomes.net/products/satellite1-pcb-dev-kit){ .md-button }
    [Docs](satellite1-dev-kit.md){ .md-button }

</div>

## Options

Form factor is one choice. These are separate ones, and they work on any Satellite1 whichever box it came in, so you can pick any combination.

<div class="grid cards" markdown>

-   :material-ethernet:{ .lg .middle } __PoE1__

    ---

    Power and network over a single Ethernet run instead of USB-C power plus Wi-Fi. Handy anywhere that pulling a cable is easier than finding an outlet, which covers most ceilings.

-   :material-radar:{ .lg .middle } __mmWave presence__

    ---

    An LD2450 radar, so a Satellite1 can tell whether someone is in the room rather than just whether something moved. The firmware works out which sensor is attached and exposes the right entities on its own, so an LD2410 from an earlier build still works.

</div>

Neither one changes the voice assistant. They change how a unit is powered and what it can sense, which is why we treat them as options rather than as different versions.
