## Satellite1 Power Supplies

??? Note "As of July 2025, The Satellite1 comes with the necessary USB-C cable and Power Adapter incldued in the Dev Kit."

 <br>![20W Power Adapter](/assets/accessory_20W_power_brick.jpg){ width="40%" loading=lazy }</br>
 If you must purchase a third-party adapter we recommend a 3A @ 9V USB-C Power Delivery Adapter.
 <br>[Get it on Amazon](https://amzn.to/4fRLZ1f){ .md-button .md-button--primary }

 <br>![USB-C Cables](/assets/accessory_usb_c_cables.jpg){ width="40%" loading=lazy }</br>
 <br>Don't forget some standard USB-C cables.  These have been solid in my testing:
 <br>[Get it on Amazon](https://amzn.to/42gcVEZ){ .md-button .md-button--primary }


## Speakers and Connectors
You can hear audio from the Satellite1 by plugging headphones or powered speakers into the 3.5 mm jack, or by connecting a single full-range 4 ohm speaker to the built-in 25 watt amplifier using the JST-XH connector on the bottom of the HAT.

<br>![Connect speaker to Sat1](/assets/Accessories-speaker.png){ width="40%" loading=lazy }</br>

Here are the supplies to connect a speaker to your Sat1:

<br>![JST-XH cables](/assets/Accessories-jst.png){ width="40%" loading=lazy }</br>
<br>JST XH2.54-2P 2.54mm Pitch 2 Pin Male Connector
<br>[Get it on Amazon](https://amzn.to/4ly9LDA){ .md-button .md-button--primary }

<br>![Recommended Dayton Audio Speaker](/assets/dayton_audio.jpg){ width="40%" loading=lazy }</br>
<br> The Speakers we recommend depend on which enclosure you choose.
<br>[See Our Speaker & Enclosure Recommendations](/satellite1-squircle-enclosures){ .md-button .md-button--primary }

<br>![Recommended Spade Connectors](/assets/Accessories-spade-connector.jpg){ width="40%" loading=lazy }</br>
<br> For the cleanest connection between the speaker and the JST-XH cable, we recommend using spade connectors and a crimper tool. If you prefer, you can solder the cable to the speaker terminals, or simply wrap the cable around the terminals—it’s entirely up to you.
<br>[Get it on Amazon](https://amzn.to/47YbzBo){ .md-button .md-button--primary }


## mmWave Human Presence Detectors

Your Sat1 also supports the Human Presence Sensing Radar Modules LD2410 or LD2450.  Please be sure to read about how to calibrate your mmWave sensors.
[Learn How to Install mmWave](/satellite1-presence-sensors){ .md-button .md-button--primary }

<br>![LD2410 mmWave](/assets/Accessories-mmwave-HLK-LD2410.png){ width="40%" loading=lazy }</br>
<br>HLK-LD2410 mmWave is smaller sensor that is good at presence detection if the occupant is still in the room.  Note that this sensor can only detect one person at a time and cannot determine exactly where the person is in the room.  If multiple people are in the room it will focus on the person with the most "energy" or motion.
<br>[Get it on Amazon](https://amzn.to/3C6utsf){ .md-button .md-button--primary }

<br>![LD2450 mmWave](assets/accessory_mmwave_ld2450.jpg){ width="40%" loading=lazy }</br>
<br>HLK-LD2450 mmWave is a larger sensor that offers everything the ld2410 has, plus it can detect up to 3 moving persons and their position in the room.  NOTE: this sensor is not yet supported by ESPHome and we're dependent on a PR that we hope Home Assistant will soon merge.
<br>[Get it on Amazon](https://amzn.to/4hcKtrK){ .md-button .md-button--primary }