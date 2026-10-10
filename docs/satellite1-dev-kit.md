The Dev Kit is the platform with nothing around it. Two boards, an antenna and a power supply, which is every Satellite1 before anyone decides what shape it should be.

It runs perfectly well like this. Bare on a bench it is a working voice assistant with a speaker jack, and it is also the starting point for anyone building their own enclosure.

![The Satellite1 Dev Kit laid out: Hat board, antenna, USB-C cable and power adapter](/assets/products/satellite1-dev-kit/hero.jpg){ width="100%" }

[Buy a Dev Kit :material-cart:](https://futureproofhomes.net/products/satellite1-pcb-dev-kit){ .md-button .md-button--primary }

## What comes in the box

| | |
|---|---|
| **Core board** | The rectangular one, ESP32-S3 |
| **Hat board** | The round one, XMOS XU316, microphones, LED ring, buttons, amplifier |
| **Wi-Fi antenna** | External, IPEX connector |
| **Power** | 30 W USB-C PD adapter and cable, US, EU or UK plug |

Full specifications are on the Platform Overview, for the [Core board](satellite1.md#core-board) and the [Hat board](satellite1.md#hat-board).

## What does not

| | Where it comes from |
|---|---|
| Speaker drivers, crossover, audio cabling | Electronics Kit |
| Enclosure parts, screws, sealing foam | Enclosure Kit, or print your own |
| mmWave presence sensor | Sold separately, see [Getting Started](satellite1-connecting-to-ha.md#add-an-mmwave-sensor) |

You only need those if you are building the Dev Kit into a finished speaker. For bench use, the box has everything.

## Assembly

1.  **Attach the antenna**

    ![Pressing the antenna connector onto the Core board](/assets/mount_antenna_to_core.png){ loading=lazy }

    Press the antenna's connector onto the mating connector on the Core board, next to the ESP32 chip.

    !!! warning "The 1.1 needs this"

        The Satellite1.1 Core uses an external antenna rather than one on the board, so without it you will not reach Wi-Fi at all. Any antenna with an IPEX connector works if the supplied one does not suit your installation. A previous generation Core has the antenna built in.

2.  **Press the Core onto the Hat**

    ![Aligning the Core board with the Hat's 40-pin header](/assets/mount_core_to_hat.png){ loading=lazy }

    The Hat carries a Raspberry Pi standard 40-pin header. Line the Core's two rows of pins up with it and press the boards together firmly. You should be able to feel the pins protruding through the top of the Hat with a fingertip. If you cannot, it is not seated.

3.  **Attach an mmWave sensor**

    Optional. The Satellite1.1 Hat has a 4-pin JST connector on its underside for an LD2450, so the sensor connects by cable rather than being mounted on the board. Fitting and tuning are covered in [Getting Started](satellite1-connecting-to-ha.md#add-an-mmwave-sensor).

4.  **Connect a speaker**

    ![A speaker driver connected to the JST-XH speaker connector](/assets/attach_speaker_to_dev_kit.jpg){ loading=lazy }

    The amplified JST-XH connector drives a speaker directly. A 4 ohm full-range driver rated to 30 W is the best match, though smaller drivers and 8 ohm drivers work too. You can skip this and use the 3.5 mm line out into powered speakers instead.

5.  **Power it on**

    ![The USB-C power adapter connected to the CORE/ESP32 port](/assets/attach_power_adapter_to_dev_kit.jpg){ loading=lazy }

    Use the supplied 30 W adapter, into the Hat's USB-C port, labelled **CORE/ESP32**. It is the only USB-C on a 1.1 Hat.

    On first boot the blue LEDs count down clockwise while the device flashes its XMOS audio processor. When they change to a sparkling warm white, it is ready to pair.

[Connect it to Home Assistant :material-arrow-right:](satellite1-connecting-to-ha.md){ .md-button .md-button--primary }

## Building it into something

The Dev Kit is step one of every self-build. The [Smart Speaker build guide](satellite1-smart-speaker.md) picks up from here, or you can [print the enclosure](satellite1-print-enclosure.md) first and buy only the parts that go inside it.

!!! note "The Hat also fits a Raspberry Pi, unofficially"

    The Hat will mount to a Raspberry Pi instead of a Core, and there is an [alpha firmware](https://github.com/FutureProofHomes/Satellite1-RPi-Image) you are welcome to try. We do not support it and cannot promise it keeps working. Others experimenting with it are in the [Discord community](https://discord.futureproofhomes.net).
