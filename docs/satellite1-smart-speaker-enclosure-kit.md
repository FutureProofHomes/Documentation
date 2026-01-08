## Smart Speaker Enclosure Kit

The upcoming [Satellite1 Smart Speaker Enclosure Kit](https://futureproofhomes.net/products/satellite1-smart-speaker-enclosure-kit) converts your Satellite1 Dev Kit into a 2-way smart speaker. This guide explains how to assemble the kit are enjoy a powerful 2-way speaker and voice assistant.

<figure markdown="span">
  ![Smart Speaker Enclosure Kit Photoshoot](/assets/smart-speaker-enclosure-kit/white_gray_enclosure.jpg){ width="100%" }
  <figcaption>Optional "Charcoal Gray" or "Bone White" color choices</figcaption>
</figure>

## Assembly Requirements
1. [Satellite1 Dev Kit](https://futureproofhomes.ai/products/satellite1-pcb-dev-kit)
2. [Satellite1 Smart Speaker Enclosure Kit](https://futureproofhomes.ai/products/satellite1-smart-speaker-enclosure-kit) (Coming very soon!)
    

## Parts Included in Kit
<figure markdown="span">
  ![Smart Speaker Enclosure Kit Parts](/assets/smart-speaker-enclosure-kit/all_parts.jpg){ width="100%" }
  <figcaption>Parts inside the Smart Speaker Enclosure Kit</figcaption>
</figure>
- 3D printed speaker enclosure
    - Front & back piece
    - Top plate & LED diffuser
    - Screw-guide tool
- 3" Full-range, bass heavy woofer (20W, 4Ω)
- 1.2" Neodymium dome tweeter (20W, 4Ω)
- 2-Way passive crossover
- JST-XH cable
- 2 Red 5.3mm speaker cables
- 2 Black 2.8mm speaker cables
- Adhesive sealing foam
- M3 x 10mm mounting screws
- Hex wrench

## Tools not Included in Kit
- Scissors
- Small phillips head screwdriver
- Needle nose pliers

!!! warning "Dev Kit Enclosure Limitations"

    1. Please use the firmware's temperature & humidity offset capabilities to assist in more accurate readings from Hat's built-in sensors.
    2. This enclosure does not support the Dev Kit’s top-mounted mmWave connectors. It also does not support the luminosity sensors, as installing the Dev Kit inside the enclosure significantly reduces light reaching the sensors.
    3. When playing music at full volume the wake word may have difficulty hearing the room.  That said, this is our best performing enclosoure yet.

<!-- # Watch the Instructional Video
<iframe style="width: 100%; aspect-ratio: 16 / 9;" src="https://www.youtube.com/embed/WeOEl3jho1k?start=205" title="Satellite1 Smart Speaker Enclsoure Kit" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> -->

## Assemble the Kit
<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Remove Speaker Hole Tab__

    ---

    ![Image title](/assets/smart-speaker-enclosure-kit/remove_tab.jpg){ loading=lazy }
    Remove the speaker hole tab with a pair of pliers.

-   :material-numeric-2-circle:{ .lg .middle } __Apply Sealing Foam__

    ---

    ![Image title](/assets/smart-speaker-enclosure-kit/apply_sealing_foam.jpg){ loading=lazy }
    Adhere the sealing foam around the parameter of the front enclosure piece, tweeter and woofer.  Cut any excess foam with scissors and keep for later.
    

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

    2. Use a small phillips head screwdriver to connect the supplied JST-XH cable to the east-facing terminal. 
    3. On the north and west terminals, secure the 5.3 mm red wires to positive (+) and the 2.8 mm black wires to negative (–). 
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
    

-   :material-numeric-7-circle:{ .lg .middle } __Mount Back Chamber__

    ---

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

    ![Image title](/assets/smart-speaker-enclosure-kit/connect_JST_cable_3.jpg){ loading=lazy }
    ![Image title](/assets/smart-speaker-enclosure-kit/mounted_dev_kit.jpg){ loading=lazy }
    1. Press the Core and Hat PCBs firmly together ([see details here](satellite1-assembly.md)) and connect the JST-XH cable.
    
    2. Rest the Sat1 on the enclosure's four mounting posts while ensuring the headphone jack is facing the rear. Hand-tighten four (4) hex screws to secure the PCBs to the enclosure.
    

-   :material-numeric-10-circle:{ .lg .middle } __Assemble Top Piece & LED Diffuser__

    ---

    ![Image title](/assets/smart-speaker-enclosure-kit/push_in_diffuser.jpg){ loading=lazy }
    ![Image title](/assets/smart-speaker-enclosure-kit/mount_top_piece.jpg){ loading=lazy }
    1. Snap the LED diffuser into the top piece.

    2. Lightly push the top piece assembly down on the enclsoures 4 ball joints making sure the headphone jack opening is facing the rear.
</div>

!!! success "Congratuations on Assembling your Satellite1 Smart Speaker!"

    Plug-in with the Dev Kit's supplied 30W power USB-C power adapter and follow the necessary steps to [connect to Home Assistant](satellite1-connecting-to-ha.md), and then [stream some music](satellite1-streaming-music.md)!

## Print-at-Home
The 3D-printable 3MF project files, STL and STEP files are published online for anyone who wants to print or remix the enclosure at home.

#### Links

- [FutureProofHomes GitHub](https://github.com/FutureProofHomes/Satellite1-Enclosures/tree/main/OEM%20Enclosures/Satellite1%20Smart%20Speaker%20Enclosure%20Kit)
- [MakerWorld](https://makerworld.com/de/models/2195101-futureproofhomes-oem-satellite1-smart-speaker) (Coming Soon!)

#### Printing Parameters

- We recommend using 0.4mm nozzle diameter and dry Bambu-grade PETG filament.
- Use 3 wall perimeter and 30% cubicle infill for the front and back speaker chamber parts
- Use 3 wall perimeter and 15% cubicle infill for the top, screw guide and diffuser
- Print the diffuser in transparent PETG or even white PLA for the best results.
- No supports required!

!!! info "Compatible Speaker Drivers"

    The Satellite1 Smart Speaker Enclosure Kit is acoustically and mechanically engineered to work with a specific set of high-quality LG speaker drivers. These drivers were selected for their excellent sound quality, compatibility with the Satellite1 amplifier and crossover, and reliable availability in bulk from trusted suppliers.

    Due to packaging and supply-chain complexities during launch, which can result in mismatches between available enclosures and speakers, we do not currently sell the speaker drivers or other electronic components separately. We may offer an “electronics-only” kit after launch.

    If you choose to purchase the recommended speaker drivers from third-party online retailers, please be aware that counterfeit or cloned products do exist. Additionally, modifying the enclosure to accommodate alternative speaker drivers may affect sound quality and wake-word performance.

    Have fun hacking!

    - Tweeter MLT20-F4-S4830 (Sorry, no reliable supplier links we can confidently recommend.)
    - Woofer MLW78-F4-R6015 (Sorry, no reliable supplier links we can confidently recommend.)
    - [Crossover](https://amzn.to/49xXidZ) (Sorry, no reliable model number.)