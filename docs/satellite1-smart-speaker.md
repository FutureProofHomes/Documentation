Build a Satellite1 Smart Speaker at home from three kits: the [Dev Kit](satellite1-dev-kit.md) for the boards, the [Enclosure Kit](satellite1-enclosure-kit.md) for the cabinet, and the [Electronics Kit](satellite1-electronics-kit.md) for the drivers and crossover.

## Before You Begin

You'll need a few household tools that aren't included in any kit:

- Scissors
- Small phillips head screwdriver
- Needle nose pliers

!!! warning "Dev Kit + Enclosure Limitations"

    Dev Kits are designed for use on your electronics bench, but this enclosure kit pushes the dev kit to its full potential, though a few limitations apply.

    1. Temp, hum, lux  [Read more here.](/satellite1-faqs/#why-is-the-temp-or-lux-sensor-incorrect)
    2. At full volume, the wake word may not be heard perfectly.  Still the wake word should respond if the enclosure is airtight and not on a vibrating surface.

## Watch the Instructional Video

!!! danger "Important Correction to Video Tutorial"

    The crossover is incorrectly oriented in the video.  Rotate it 180° before installing.  [Follow photos and documentation below.](#assemble-the-kit)

<iframe style="width: 100%; aspect-ratio: 16 / 9;" src="https://www.youtube.com/embed/n5yNEhcAjWU?si=QPOJhOR9q13SHaoC&amp;start=189" title="Satellite1 Smart Speaker Enclosure Kit" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Assemble the Kit
<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Remove Speaker Hole Tab__

    ---

    ![Image title](/assets/smart-speaker-enclosure-kit/remove_tab.jpg){ loading=lazy }
    Remove the speaker hole tab with a pair of pliers.

-   :material-numeric-2-circle:{ .lg .middle } __Apply Sealing Foam__

    ---

    ![Image title](/assets/smart-speaker-enclosure-kit/apply_sealing_foam.jpg){ loading=lazy }
    Adhere the sealing foam around the perimeter of the front enclosure piece, tweeter and woofer.  Cut any excess foam with scissors and keep for later.
    

-   :material-numeric-3-circle:{ .lg .middle } __Install Speaker Drivers__

    ---

    ![Image title](/assets/smart-speaker-enclosure-kit/install_speaker_drivers_edited.jpg){ loading=lazy }
    1. Use four (4) M3x10mm hex screws to install the tweeter with the terminals facing north and south.

    2. Use another four (4) M3x10mm hex screws to install the woofer with both speaker terminals facing north.

-   :material-numeric-4-circle:{ .lg .middle } __Prepare Crossover Wiring__

    ---

    ![Image title](/assets/smart-speaker-enclosure-kit/crossover_cable_mapping.jpg){ loading=lazy }
    ![Image title](/assets/smart-speaker-enclosure-kit/crossover_wiring.jpg){ loading=lazy }
    1. Orient the crossover so no blue terminal faces south. 

    2. Use a small phillips head screwdriver to connect the supplied JST-XH cable to the west-facing terminal. 
    3. On the north and east terminals, secure the 5.3 mm red wires to positive (+) and the 2.8 mm black wires to negative (–). 
    4. Optionally use the supplied jumpers to boost bass and/or treble.

-   :material-numeric-5-circle:{ .lg .middle } __Install Crossover & Connect Speakers__

    ---

    ![Image title](/assets/smart-speaker-enclosure-kit/crossover_speaker_cables_edited.jpg){ loading=lazy }
    1. Use two (2) M3x10mm hex screws to securely mount the crossover to the front piece.  Connect cables to speakers.  

    2. We recommend applying sealing foam around the JST-XH cable to ensure an airtight seal at the speaker hole.

-   :material-numeric-6-circle:{ .lg .middle } __Insert Screws__

    ---

    ![Image title](/assets/smart-speaker-enclosure-kit/all_screws_with_screw_guide_edited.jpg){ loading=lazy }
    Insert seven (7) M3x10mm hex screws into the front chamber, use the screw guide tool to not drive them in too far. Do not add a screw at the bottom.
    

-   :material-numeric-7-circle:{ .lg .middle } __Mount Antenna & Back Chamber__

    ---

    ![Image title](/assets/smart-speaker-enclosure-kit/antenna_mount_annotated_cropped_new.JPG){ loading=lazy }
    Depending on your enclosure and satellite version, you can slide the WiFi antenna into the dedicated “Stealth Pocket” or adhere it to the back of the speaker chamber.  If you have an original Satellite1 then the antenna is built-in and you can skip this step.

    ![Image title](/assets/smart-speaker-enclosure-kit/mount_back_chamber.jpg){ loading=lazy }
    Align the two chamber parts together, making sure the JST wire is not pinched and that the foam forms an airtight seal. Slide the parts together with the front piece moving downward and the back piece moving upward.


-   :material-numeric-8-circle:{ .lg .middle } __Fasten All Screws__

    ---

    ![Image title](/assets/smart-speaker-enclosure-kit/add_bottom_screw.jpg){ loading=lazy }
    Drop the bottom screw into place and use the hex wrench to loosely fasten.

    ![Image title](/assets/smart-speaker-enclosure-kit/fasten_all_screws.jpg){ loading=lazy }
    Evenly tighten all the screws in an alternating pattern until you feel resistance (approx 4-5 turns), be careful to not overtighten the screws.

-   :material-numeric-9-circle:{ .lg .middle } __Mount the PCB Dev Kit__

    ---
    ![Image title](/assets/smart-speaker-enclosure-kit/stealth_pocket_ annotated_cropped.JPG){ loading=lazy }
    1. Gently press the WiFi antenna's gold IPEX connector to the Core board ([see details here](satellite1-assembly.md)).  
    
    2. Firmly press the Core/Hat boards together via the 40-pin header.
    3. Connect the optional LD2450 mmWave 4-pin cable to to the bottom of the Hat.
    4. Route the cables through their respective 3D printed raceways.
    5. Ensuring the headphone jack is facing the rear, rest the Sat1 Hat on the enclosure's four mounting posts and hand-tighten four hex screws to secure the PCBs to the enclosure.
    ![Image title](/assets/smart-speaker-enclosure-kit/connect_JST_cable.jpg){ loading=lazy }
    ![Image title](/assets/smart-speaker-enclosure-kit/mounted_dev_kit.jpg){ loading=lazy }

-   :material-numeric-10-circle:{ .lg .middle } __Assemble Top Piece & LED Diffuser__

    ---

    ![Image title](/assets/smart-speaker-enclosure-kit/push_in_diffuser.jpg){ loading=lazy }
    ![Image title](/assets/smart-speaker-enclosure-kit/mount_top_piece.jpg){ loading=lazy }
    1. Snap the LED diffuser into the top piece.

    2. Lightly push the top piece assembly down on the enclosure's 4 ball joints making sure the headphone jack opening is facing the rear.
</div>

!!! success "Congratulations on Assembling your Satellite1 Smart Speaker!"

    Power up the speaker with the Dev Kit's supplied 30W power USB-C power adapter and follow the necessary steps to [connect to Home Assistant](satellite1-connecting-to-ha.md), and then [stream some music](satellite1-streaming-music.md)!

## Print-at-Home
The 3D-printable 3MF project files, STL and STEP files are published online for anyone who wants to print or remix the enclosure at home.

#### Links

- [FutureProofHomes GitHub](https://github.com/FutureProofHomes/Satellite1-Enclosures/tree/main/OEM%20Enclosures/Satellite1.1%20Smart%20Speaker%20Enclosure%20Kit)
- [MakerWorld](https://makerworld.com/models/2615819-futureproofhomes-oem-satellite1-1-smart-speaker)

#### Printing Parameters

- We recommend using 0.4mm nozzle diameter and dry Bambu-grade PETG filament.
- Use 3 wall perimeter and 30% cubicle infill for the front and back speaker chamber parts
- Use 3 wall perimeter and 15% cubicle infill for the top, screw guide and diffuser
- Print the diffuser in transparent PETG or even white PLA for the best results.
- No supports required!

!!! info "Compatible Speaker Drivers"

    The enclosure is acoustically and mechanically engineered around a specific set of drivers, chosen for sound quality and for how they pair with the Satellite1's amplifier and crossover.

    We sell all of them. The [Electronics Kit](satellite1-electronics-kit.md) bundles the woofer, tweeter, crossover, and cables, or you can buy each part on its own:

    - [3" Mid-Range Woofer, 4Ω 20W](https://futureproofhomes.net/products/3-inch-woofer-4ohm-20w)
    - [Tweeter, 4Ω 20W](https://futureproofhomes.net/products/tweeter-4ohm-20w)
    - [Two-Way Speaker Crossover](https://futureproofhomes.net/products/two-way-speaker-crossover)

    Substituting other drivers, or modifying the enclosure to fit them, may affect both sound quality and wake-word performance.

    Have fun hacking!