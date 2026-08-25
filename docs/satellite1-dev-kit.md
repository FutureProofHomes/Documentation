The **Satellite1 Dev Kit** is the electronics at the heart of every Satellite1. It ships as two PCB boards that stack together — the "Core" (rectangular) and the "Hat" (round) — plus the power and antenna hardware needed to boot.

Every other kit builds on this one. If you are assembling a smart speaker at home, start here.

[View the Dev Kit on our store :material-cart:](https://futureproofhomes.net/products/satellite1-pcb-dev-kit){ .md-button .md-button--primary }

![Mount Core to Hat](/assets/mount_core_to_hat.png){ width="100%" }

## What's in the Box

- **Satellite1.1 Core board** — ESP32-S3 (dual-core LX7 @ 240 MHz, 16 MB flash, 8 MB PSRAM)
- **Satellite1.1 Hat board** — XMOS XU316 audio processor, microphone array, 24-LED ring, 4 tactile buttons, 25W amplifier
- **30W USB-C Power Delivery adapter and cable** — choose US, EU, or UK plug at checkout
- **2.4 GHz WiFi antenna** with IPEX connector cable

!!! warning "The antenna is required"

    All Satellite1 ordered on or after February 17, 2026 ship with an external antenna, and the board will not reach WiFi without it. If the included antenna is too large for your setup, any smaller antenna with an IPEX connector will work.

## What's Not Included

| Item | Where to get it |
|------|-----------------|
| Speaker drivers, crossover, and speaker cables | [Electronics Kit](satellite1-electronics-kit.md) |
| Enclosure parts, screws, and sealing foam | [Enclosure Kit](satellite1-enclosure-kit.md) |
| mmWave human presence sensor | [LD2450 sensor and harness](https://futureproofhomes.net/products/ld2450-mmwave-human-presence-sensor) — see [mmWave Sensors](satellite1-mmwave-overview.md) |

The Dev Kit runs perfectly well as a bare board on your bench. You only need the other kits if you want to build it into a finished speaker.

## Key Specifications

| | |
|---|---|
| **Processor** | ESP32-S3 dual-core 32-bit LX7 @ 240 MHz, 512 KB SRAM, 16 MB flash, 8 MB PSRAM |
| **Audio processor** | XMOS XU316, 16-core 32-bit RISC @ 800 MHz, 1024 KB SRAM, 8 MB flash |
| **Amplifier** | 25W mono output (TAS2780) |
| **Line out** | 3.5mm headphone jack (PCM5122) |
| **Sensors** | Ambient light (LTR-303ALS), temperature and humidity (AHT20) |
| **Presence detection** | Optional LD2410 or LD2450 mmWave radar |
| **Radios** | 2.4 GHz WiFi, Bluetooth 5 (LE) |
| **Expansion** | FX23L connector |
| **Power** | 30W USB-C PD recommended; boards support up to 20V @ 5A |

!!! question "Compatibility"

    The Hat board can also be mounted to a Raspberry Pi. [Raspberry Pi firmware is still in development](https://github.com/FutureProofHomes/Satellite1-RPi-Image) — if you want to help test it, find us in the [Discord community](https://discord.futureproofhomes.net).

## Next Steps

Firmware is installed at the factory, so the boards are ready to run as soon as they are assembled.

[Assemble the Dev Kit :material-arrow-right:](satellite1-assembly.md){ .md-button .md-button--primary }
[Connect to Home Assistant :material-arrow-right:](satellite1-connecting-to-ha.md){ .md-button }
