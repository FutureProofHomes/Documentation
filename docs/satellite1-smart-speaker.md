A Smart Speaker is three kits assembled. Buy them separately and put it together yourself, or print the enclosure and buy only the parts that go in it.

## What you need

| | |
|---|---|
| **Dev Kit** | Core and Hat boards, antenna, power supply |
| **Enclosure Kit** | Printed enclosure, 22 M3x10mm screws, hex wrench, screw guide, sealing foam |
| **Electronics Kit** | Woofer, tweeter, two-way crossover, audio cabling |

Plus three household tools that are in none of the kits: scissors, a small Phillips screwdriver, and needle-nose pliers.

!!! warning "A Dev Kit in a sealed box behaves differently"

    A Dev Kit is designed to run on a bench. Putting one inside an airtight enclosure pushes it further than that, and two things change. The temperature, humidity and light sensors read the inside of the box rather than the room. At full volume the wake word can be harder to hear if the enclosure is not sealed properly or is sitting on a surface that resonates.

## Assembly

1.  **Remove the speaker hole tab**

    ![Removing the speaker hole tab with pliers](/assets/smart-speaker-enclosure-kit/remove_tab.jpg){ loading=lazy }

    Take the tab out of the speaker hole with a pair of pliers.

2.  **Apply the sealing foam**

    ![Sealing foam applied around the front enclosure](/assets/smart-speaker-enclosure-kit/apply_sealing_foam.jpg){ loading=lazy }

    Run the foam around the perimeter of the front enclosure piece, the tweeter and the woofer. Trim the excess with scissors and keep the offcuts, you need them again in step 5.

3.  **Install the speaker drivers**

    ![Woofer and tweeter installed in the front chamber](/assets/smart-speaker-enclosure-kit/install_speaker_drivers_edited.jpg){ loading=lazy }

    Fit the tweeter with four M3x10mm hex screws, terminals facing north and south. Fit the woofer with another four, both terminals facing north.

4.  **Wire the crossover**

    ![Crossover cable mapping](/assets/smart-speaker-enclosure-kit/crossover_cable_mapping.jpg){ loading=lazy }

    ![Crossover wiring detail](/assets/smart-speaker-enclosure-kit/crossover_wiring.jpg){ loading=lazy }

    Orient the crossover so that no blue terminal faces south. Connect the supplied JST-XH cable to the west-facing terminal with a small Phillips screwdriver. On the north and east terminals, the 5.3 mm red wires go to positive and the 2.8 mm black wires to negative. The supplied jumpers optionally boost bass or treble.

5.  **Mount the crossover and connect the speakers**

    ![Crossover mounted and speaker cables connected](/assets/smart-speaker-enclosure-kit/crossover_speaker_cables_edited.jpg){ loading=lazy }

    Two M3x10mm screws hold the crossover to the front piece. Connect the cables to the drivers, then pack sealing foam around the JST-XH cable where it passes through the speaker hole, so the chamber stays airtight.

6.  **Insert the screws**

    ![Seven screws inserted using the screw guide tool](/assets/smart-speaker-enclosure-kit/all_screws_with_screw_guide_edited.jpg){ loading=lazy }

    Seven M3x10mm screws into the front chamber, using the screw guide tool so none go in too far. Leave the bottom one out for now.

7.  **Fit the antenna and close the chambers**

    ![Wi-Fi antenna in the stealth pocket](/assets/smart-speaker-enclosure-kit/antenna_mount_annotated_cropped_new.JPG){ loading=lazy }

    Slide the Wi-Fi antenna into the stealth pocket, or adhere it to the back of the speaker chamber, depending on your enclosure. This applies to the Satellite1.1 Core, which needs the external antenna to reach Wi-Fi at all. A previous generation Core has the antenna built in, so skip this step.

    ![Aligning the back chamber with the front](/assets/smart-speaker-enclosure-kit/mount_back_chamber.jpg){ loading=lazy }

    Align the two chamber halves with the JST wire clear and the foam forming a seal, then slide them together, front piece moving down and back piece moving up.

8.  **Fasten everything**

    ![Dropping in the bottom screw](/assets/smart-speaker-enclosure-kit/add_bottom_screw.jpg){ loading=lazy }

    ![Tightening the screws in an alternating pattern](/assets/smart-speaker-enclosure-kit/fasten_all_screws.jpg){ loading=lazy }

    Drop in the bottom screw and start it loosely. Then tighten all of them evenly in an alternating pattern until you feel resistance, roughly four or five turns. Do not overtighten.

9.  **Mount the boards**

    ![IPEX antenna connector on the Core board](/assets/smart-speaker-enclosure-kit/stealth_pocket_%20annotated_cropped.JPG){ loading=lazy }

    Press the antenna's gold IPEX connector onto the Core board, then press the Core and Hat together through the 40-pin header. Connect the optional LD2450 mmWave 4-pin cable to the underside of the Hat.

    ![Connecting the JST cable](/assets/smart-speaker-enclosure-kit/connect_JST_cable.jpg){ loading=lazy }

    ![Boards mounted on the enclosure posts](/assets/smart-speaker-enclosure-kit/mounted_dev_kit.jpg){ loading=lazy }

    Route the cables through their printed raceways. With the headphone jack facing the rear, rest the Hat on the four mounting posts and hand-tighten four hex screws.

10. **Fit the top piece**

    ![Snapping the LED diffuser into the top piece](/assets/smart-speaker-enclosure-kit/push_in_diffuser.jpg){ loading=lazy }

    ![Pressing the top piece onto the enclosure](/assets/smart-speaker-enclosure-kit/mount_top_piece.jpg){ loading=lazy }

    Snap the LED diffuser into the top piece, then press the assembly down onto the enclosure's four ball joints, headphone jack opening to the rear. If you printed the multi-material top, the diffuser is already part of it, so there is nothing to snap in.

!!! success "That is a Satellite1"

    Power it from the Dev Kit's 30 W USB-C adapter, into the Hat's USB-C port labelled CORE/ESP32. The LEDs count down in blue while it flashes the XMOS processor, then sparkle warm white when it is ready to pair.

## Printing it yourself

The enclosure files are published, so you can print it rather than buying the Enclosure Kit and buy only the parts that go inside.

[Print the enclosure :material-arrow-right:](satellite1-print-enclosure.md){ .md-button }
