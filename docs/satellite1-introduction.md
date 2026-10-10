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

### How that compares

The two other local voice speakers people weigh this against are both built around a single small driver. That is the right call for speech, and it is also the ceiling on what they can do with music.

| | Satellite1 Smart Speaker | Home Assistant Voice PE | Third Reality Voice/Music Assistant |
|---|---|---|---|
| **Drivers** | 3 inch woofer and 1.2 inch tweeter | One internal speaker | One 3 W, 4 ohm speaker |
| **Crossover** | Two-way passive | None | None |
| **Amplifier** | 25 W mono Class-D, TAS2780 | 3.1 W mono Class-AB, TPA6211A1 | Not published |
| **Power input** | USB-C PD, up to 20 V at 5 A | USB-C, 5 V at 2 A | USB-C |
| **Line out** | 3.5 mm jack | 3.5 mm jack | Not listed |

Specifications are as each vendor publishes them. Nabu Casa does not list the Voice PE amplifier in its specifications, but it does publish the full KiCad schematic, which names the part. Third Reality publishes firmware rather than hardware design files, so their amplifier is not documented anywhere we can find.

The power row is the one that explains the rest. A 5 V, 2 A supply is 10 W for the entire device, which sets a ceiling on the amplifier no matter which part you choose. USB-C Power Delivery is what gives the Satellite1 the headroom to drive two drivers properly, and it is the reason an underpowered supply shows up as quiet or distorted audio.

Both of the others are good at what they are for, and neither is trying to be a music speaker. The difference is that a Satellite1 does both jobs, so a room does not need a voice puck next to a separate speaker.

## Two colors, printed not molded

The enclosure is 3D printed in Bambu Lab PETG-HF, in Charcoal Gray or Bone White, with a multi-material top plate and a transparent LED diffuser so the 24-LED ring reads clearly through it.

Printing rather than molding is what makes the enclosure revisable. It is also why the models are published for anyone to print, and why you can [build one yourself](satellite1-build.md) from the Dev Kit, Enclosure Kit and Electronics Kit, or [print the enclosure](satellite1-print.md) and buy only the parts that go inside it.

## Room for the options

An LD2450 mmWave sensor is the one part that is genuinely optional, and the enclosure is designed for it rather than retrofitted. The front chamber has a pocket printed for it.

![Two Smart Speakers with their top plates removed, showing the Hat board](/assets/products/satellite1-desktop/pair-hat.jpg){ width="100%" }

*The top plate lifts off to reach the Hat board, which is how the mmWave sensor gets fitted.*

## Set it up

Firmware is installed at the factory, so there is nothing to flash and nothing to assemble. Power it from the supplied USB-C adapter and it comes up ready to pair.

[Getting Started :material-arrow-right:](satellite1-connecting-to-ha.md){ .md-button .md-button--primary }
