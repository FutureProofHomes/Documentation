## Connect the PCBs
The Satellite1 comes in 2 pieces: 

- The "Hat" (round board) 
- The "Core" (rectangular board)

You'll notice a standard Raspberry Pi 40-pin connector on the Hat board (marked in red). Carefully align the Core board's 2 rows of pins with the Hat's 40 pin connector and press them together.

![Mount Core to Hat](/assets/mount_core_to_hat.png){ width="100%" }

## (Optional) mmWave Presence Sensors
The Satellite1 HAT has two ports for optionally mounting external mmWave presence sensors: LD2410 or LD2450. [Please read more about setting up and calibrating your presence sensors here.](satellite1-presence-sensors.md)

<figure markdown="span">
  ![LD2410 mmWave](/assets/presence-sensors/sat1_ld2410.jpg){ width="100%" loading="lazy"}
  <figcaption>LD2410 Mounted on Sat1 HAT</figcaption>
</figure>

<figure markdown="span">
  ![LD2450 mmWave](/assets/presence-sensors/sat1_ld2450.jpg){ width="100%" loading="lazy"}
  <figcaption>LD2450 Mounted on Sat1 HAT</figcaption>
</figure>

## First Boot - Powering On
The below instructions assume you have connected the HAT to the CORE and are powering the Satellite1 for the first time:

1. Take a USB-C cable and plug one end into the USB socket on the Hat labeled "CORE/ESP".
2. Plug the other end into a [9V USB-C power supply](satellite1-recommended-accessories.md#power-supply) (if you want to power a speaker from the HAT), or a computer 5V USB-C connection (if you're plugging into the headphone jack).
![ESP32 Power & Data Port](/assets/sat1_inputs_and_outputs.jpg){ width="100%" }
3. Upon first boot, you will see the blue LEDs count down clockwise as the device flashes the XMOS audio processor.
4. Finally, the LEDs will begin to sparkle a warm white color. Congrats! Move to the next step.

<!-- ### Sensor Positioning
When the sensor is directly mounted to the HAT it will point in the direction of the microphone and LEDs, which may work for your situation. However, you can also use the sensors' included JST cable to position the sensor in any orientation you'd like so it is not directly mounted to the HAT.

![Sensor JST cable](/assets/presence-sensors/sensor_jst_cable.jpg){ width="100%" loading="lazy"} -->

<!-- Watch this video to see how easy it is to assemble your Satellite1 boards.
<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> -->