## About the Dev Kit Speaker Enclosure

The Satellite1 Dev Kit Speaker Enclosure is a snap-fit enclosure that can be printed on a single plate. We highly recommend PETG filament, plus some Loctite (Blu-Tack) and speaker polyfill for the best acoustic results. This is our first-generation enclosure, and many revisions will come out as we iterate the product and receive feedback.

All the files necessary can be found in the [Satellite1-Enclosures Github Repo](https://github.com/FutureProofHomes/Satellite1-Enclosures).

<figure markdown="span">
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/31_pose_speaker.JPG){ width="100%" }
  <figcaption>25 watt BMR speaker fires down towards sound diffuser cone</figcaption>
</figure>

# Watch the Instructional Video
<iframe style="width: 100%; aspect-ratio: 16 / 9;" src="https://www.youtube.com/embed/WeOEl3jho1k?start=205" title="3D Print the World’s Best AI Voice Assistant (DIY)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Enclosure Limitations
Many of the below enclosure limitations are solved by our upcoming [power-over-ethernet SHOE board](satellite1-poe-shoe-module-overview.md)

Without the SHOE board there are some current limitations of the enclosure:

1. **The lux sensor will not give accurate readings of the room.**
<br>We will solve this with a light pipe and modified design.
2. **The temp/humidity sensor will not give accurate readings of the room.  Also the mmWave sensor is pointed up at the ceiling.**
<br>Our upcoming "SHOE" PCB will relocate these sensors down into the speaker chamber and expose a PoE port in the speaker.
3. **The light ring does not fully diffuse the LEDs.**
<br>We will solve this with a slightly modified diffuser.
4. **The mic pipes slightly decrease the accuracy of speech-to-text.**
<br>We will solve this once we get to plastic injection molded enclosures.
5. **The wake word does not respond when I'm playing music near full volume.**
<br>We will experiment with modified designs and gaskets to mitigate the vibrations in the enclosure which impact the microphone reference signal.
6. **The PCBs are hard to add/remove.**
<br>This is by design, with a little practice things become easier.

## Printing the Dev Kit Speaker Enclosure

The full speaker enclosure consists of 4 major parts.  If you don't have the necessary speaker you can print just the Satellite1 UFO enclosure.

![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/1_full_render_shot.png){ width="100%" }

??? tip "NOTE: Enclosures and geometry files may be specific to a hardware revision & speaker model number."

??? abstract "I want to quickly print using the pre-build slicer project file."

    ### Pre-Built Slicer Project File

    1. Determine your PCB hardware revision by reading the silkscreen on the PCBs.  i.e. "R2024.12.06"
    
    2. Determine the speaker model number you're running.  i.e. "Tectonic-TEBM46C20N-4B"
    
    3. Download the correct pre-built `.3mf` project file from the [Satellite1-Enclosures Github repository](https://github.com/FutureProofHomes/Satellite1-Enclosures) and open in your favorite slicer software.

        ![Satellite1 Speaker Enclosure Plate](/assets/dev_kit_enclosure/2_plated_render_shot.png){ width="100%" }

    4. Right-click on each part and select your desired filament.
    <br>**(NOTE #1:** PETG-HF is better for acoustics, but PLA will work too.) 
    <br>**(NOTE #2:** Set UFO Enclosure's "Light Ring" layer to transparent or white filament so you can see the LEDs.)
        ![Satellite1 Speaker Enclosure Filament](/assets/dev_kit_enclosure/3_select_filament.png){ width="100%" }

    5. After slicing and printing you see this is approx a 4.5h print.  Everything is "snap-fit" and requires no screws.
        ![Satellite1 Speaker Enclosure Filament](/assets/dev_kit_enclosure/4_slice_and_print.png){ width="100%" }

??? abstract "I want to create my own project from scratch in my slicer software."

    ### Custom-Built Slicer Project

    If you cannot or do not want to use our pre-built slicer project file then you can build your own plate from scratch:

    1. Add the necessary `.stl` geometry files to your slicer software from the [Satellite1-Enclosures Github repository](https://github.com/FutureProofHomes/Satellite1-Enclosures).
    2. Set your project to use the recommended settings.
        1. 0.2mm layer height
        2. 3 wall loops for strength
        3. 15% infill (increase this to 50% for the speaker enclosure for even better acoustics)
        4. (Optional) Arachne wall generator
        5. Supports are disabled EXCEPT the speaker chamber has "Build Plate Only Supports" enabled
        6. No-Brim
        ![Satellite1 Slicer Project Settings](/assets/dev_kit_enclosure/5_project_settings.png){ width="100%" }

## Assembling the Dev Kit Speaker Enclosure

1. Grab some Loctite (aka Blu-Tack) and generic speaker Polyfill.  Attach your chosen mmWave to the HAT.
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/6_enclosure_accessories.JPG){ width="100%" }
2. There are three locations where you'll see 2 mounting lips on the UFO enclosure. The goal is to get the Sat1 HAT sloted underneath the smaller bottom lip in all three locations, such that the LEDs are peaking through the square cutouts and into the light ring.
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/7_plastic_lips.JPG){ width="100%" }
3. Align the bottom (south) part of the Sat1 HAT under the bottom lip and press firmly at the top (north) of the Sat1 HAT near and around the USB-C ports and headphone jack.  Press around the parameter of the Sat1 HAT to snap in under all the bottom lips.  You'll know when you're done when the 4 buttons click perfectly.
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/7_snap_1.JPG){ width="100%" }
4. If you need to remove the HAT, pull on the corner of the wall near and lift up from the USB-C ports.
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/13_pull_tab_and_board_up.JPG){ width="100%" }
5. Roll your Loctite into a "snake" that you wrap around the speaker to make a gasket.
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/14_seal_speaker.JPG){ width="100%" }
6. Route the speaker cables up through the speaker chamber and out the top.  You only need 1 inch of cable coming out the top.
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/15_route_cable_bottom.JPG){ width="100%" }
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/16_route_cable_top.JPG){ width="100%" }
7. Add polyfill to the speaker chamber.
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/17_add_polyfill.JPG){ width="100%" }
8. Slot your speaker into the enclosure (the speaker should not sit flush due to the gasket) and lock it in with the lock ring.
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/18_mount_speaker.JPG){ width="100%" }
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/19_place_lock_ring.JPG){ width="100%" }
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/20_tighten_lock_ring.JPG){ width="100%" }
9. Choose the right speaker chamber plug based on the guage of your speaker cables and wedge it in as best as possible, leaving about 1 in of cable sticking out.  Cover the plug with Loctite.
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/21_enclosure_plug.JPG){ width="100%" }
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/22_plug_puddy.JPG){ width="100%" }
10. Connect the JST-XH connector to the bottom of the HAT and align then snap the UFO to the speaker chamber.
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/23_align_top.JPG){ width="100%" }
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/24_snap_top.JPG){ width="100%" }
11. Align and snap the speaker stand on.
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/25_align_stand.JPG){ width="100%" }
12. Find the "V" icon on the UFO enclosure.  This is where you'll plug the USB-C cable to the HAT/CORE which powers up the device.
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/26_ESP_port_close_up.JPG){ width="100%" }
  ![Satellite1 Speaker Enclosure](/assets/dev_kit_enclosure/27_ESP_port.JPG){ width="100%" }

Congrats on building your own Satellite1 Dev Kit Speaker Enclosure!