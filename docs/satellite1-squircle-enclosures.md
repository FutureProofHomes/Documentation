The "Squircle Enclosure Family" for the Satellite1 Dev Kit includes three optional speaker chamber sizes—small (1-inch), medium (2.5-inch), and large (3-inch)—with the top components of the design remaining identical across all sizes. The entire enclosure is designed to be assembled using M3 x 8mm screws.  You 3D print the enclosure at home and separately purchase and install one of our recommended speakers based on your preference.

<figure markdown="span">
  ![Squircle Enclosure Family](/assets/squircle-enclosure/family.jpg){ width="100%" }
  <figcaption>Large, Medium, and Small Squircle Enclosures</figcaption>
</figure>

## Understanding the Design

The "Top Plate", "Diffuser Ring", "PCB Spacer" & "Lock Ring" are common parts that are shared across all sizes of the squircle enclosure family.

<figure markdown="span">
  ![Squircle Enclosure Overview](/assets/squircle-enclosure/part_overview.png){ width="100%" }
  <figcaption>Cross-section of the Squircle Enclosure</figcaption>
</figure>

You can inpect individual .STEP and .STL files in the [Satellite1-Enclosures](https://github.com/FutureProofHomes/Satellite1-Enclosures/tree/main/DIY%20Enclosures/Squircle%20Enclosures/Geometry%20Files) repository.  We cannot release CAD project files due to commercial licensing restrictions.

## Choose a Speaker and Enclosure Size

<div class="grid cards" markdown>

-  :material-numeric-1-circle:{ .lg .middle } Large (3-Inch) Speaker Enclosure

    ---

    ![Large 3-Inch Speakers](/assets/squircle-enclosure/IMG_6841_min.jpg){ loading=lazy }

    * [Dayton Audio PC83-4](https://amzn.to/43eHaw2)
    * [Dayton Audio RS75-4](https://amzn.to/42egKsz)
    * [GRS 3FR-4](https://amzn.to/4kII61D)
    * [Visaton FRS8-4](https://amzn.to/43FgNOP)
    * [Tectonic TEBM46C20N-4B BMR](https://www.parts-express.com/Tectonic-TEBM46C20N-4B-BMR-3-Full-Range-Speaker-4-297-2157)
    * [FaitalPRO 3FE25](https://amzn.to/4jsB3Jp)

-   :material-numeric-2-circle:{ .lg .middle } Medium (2-Inch) Speaker Enclosure

    ---

    ![Medium 2-Inch Speakers](/assets/squircle-enclosure/IMG_6983.jpg){ loading=lazy }

    * [Dayton Audio ND65-4](https://amzn.to/43N5PrD)
    * [Dayton Audio ND64-4](https://amzn.to/3H7MN6G)
    * [Dayton Audio PC68-4](https://amzn.to/3HeSoIn)

-   :material-numeric-3-circle:{ .lg .middle } Small (1-Inch) Speaker Enclosure

    ---

    ![Small 1-Inch Speakers](/assets/squircle-enclosure/IMG_6985.jpg){ loading=lazy }

    * [DWEII 4pcs Mini Speaker Dupont Connectors](https://amzn.to/3HqLnEc)
    * [AOICRIE 2pcs 3 Watt Mini Dupont Connectors](https://amzn.to/3SSDtG6)
</div>

## Recommended Accessories

<div class="grid cards" markdown>

-  :material-numeric-1-circle:{ .lg .middle } 

    ---

    ![JST-XH cables](/assets/Accessories-jst.png){ loading=lazy }
    The 2.54mm JST-XH 2-Pin Male Connector goes in-between the Satellite1's built-in amplifier and your selected speaker.

    [Get it on Amazon](https://amzn.to/4ly9LDA){ .md-button .md-button--primary }

-   :material-numeric-2-circle:{ .lg .middle } Spade connectors and a crimper tool

    ---

    ![Recommended Spade Connectors](/assets/Accessories-spade-connector.jpg){loading=lazy }
    For the cleanest connection between the speaker and the JST-XH cable, we recommend using . If you prefer, you can solder the cable to the speaker terminals, or simply wrap the cable around the terminals—it’s entirely up to you.
    [Get it on Amazon](https://amzn.to/47YbzBo){ .md-button .md-button--primary }

</div>

## How to 3D Print the Enclosures

Download the appropriate pre-built `.3mf` project file and open in your favorite slicer software:

<div class="grid cards" markdown>
- [Download OrcaSlicer Project](https://github.com/FutureProofHomes/Satellite1-Enclosures/raw/refs/heads/main/DIY%20Enclosures/Squircle%20Enclosures/OrcaSlicer%20-%20Squircle%20Enclosure.3mf){ .md-button .md-button--primary }
- [Download Bambu Studio Project](https://github.com/FutureProofHomes/Satellite1-Enclosures/raw/refs/heads/main/DIY%20Enclosures/Squircle%20Enclosures/Bambu%20Studio%20-%20Squircle%20Enclosure.3mf){ .md-button .md-button--primary }
</div>

Remove unnecssary plates, depending on your speaker selection, enclosure type, and whether your printer supports multi-material or multi-part printing.

<figure markdown="span">
  ![Squircle Enclosure Overview](/assets/squircle-enclosure/slicer_software_screenshot.png){ width="100%" }
  <figcaption></figcaption>
</figure>

!!! info "Recommend PETG-HF"

    We recommend PETG-HF with 30% infill for ideal for acoustics. PLA with 15% infill will work as well.

!!! info "No Supports Required"

    Study the screenshot above and you'll see how to print each part such that no supports are needed.

!!! info "Screws Are Required"

    M3 x 8mm screws are required for assembly. To maintain thread integrity, minimize repeated installation and removal of screws.

!!! warning "Sensors are not supported, yet"

    Enclosing a "Dev Kit" affects sensor accuracy—lux, temperature, and humidity readings won’t reflect the room, and the top plate is not designed to support mmWave sensors.  Our upcoming [power-over-ethernet SHOE board](satellite1-poe-shoe-module-overview.md) and an PoE mid-plate will relocate the sensors into the speaker chamber and add a PoE port to the enclosure.

!!! warning "When playing music at full volume the wake word may not respond"

    This is caused by vibrations traveling through the enclosure to the microphones. We're working with experts to address this in the official injection-molded enclosures. Stay tuned.

## Assemble the Enclosure

### Top Plate Assembly

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } Install Diffuser Ring

    ---

    ![Press in place](/assets/squircle-enclosure/IMG_6828-min.jpg){ loading=lazy }
    If you printed the diffuser ring as a separate part, apply light pressure around the ring to snap it in place. If you used our multi-material print, you can skip this step.

-   :material-numeric-2-circle:{ .lg .middle } Align the FPH Logos

    ---

    ![Line-Up Parts](/assets/squircle-enclosure/IMG_6748-min.jpg){ loading=lazy }
    Find the two FPH logos on the top plate and lock ring. Line up the logos and the I/O ports.

-   :material-numeric-3-circle:{ .lg .middle } Snap Parts Together

    ---

    ![Snap Together](/assets/squircle-enclosure/IMG_6749-min.jpg){ loading=lazy }
    Sandwich the logos together and you'll feel both parts snap together.

-   :material-numeric-4-circle:{ .lg .middle } Practice Locking & Unlocking

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6750-min.jpg){ loading=lazy }
    Practice rotating the two parts. When the FPH logo is visible, the top plate is unlocked and can be mounted/unmounted from the speaker chamber.

-   :material-numeric-5-circle:{ .lg .middle } Align PCB Spacer to HAT

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6775-min.jpg){ loading=lazy }
    Align all four holes on the PCB spacer to the holes on the HAT. The taller standoffs will be closest to the I/O ports.

-   :material-numeric-6-circle:{ .lg .middle } Drop Dev Kit Into Position

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6780-min.jpg){ loading=lazy }
    Align the HAT's headphone jack with the round I/O port. Press the CORE board into the HAT board, ensuring the PCB spacer stays in place.

-   :material-numeric-7-circle:{ .lg .middle } Secure the Dev Kit to the Top Plate

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6781-min.jpg){ loading=lazy }
    By hand, secure the Dev Kit to the top piece with four M3 x 8mm screws. Do not overtighten the screws.
</div>

!!! success
    You have built your **Satellite1 Squircle Top Plate**!

### Mid-Plate Assembly

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } Find Nubs

    ---

    ![See Logos](/assets/squircle-enclosure/IMG_6753-min.jpg){ loading=lazy }
    Look closely at the mid-plate and feel the bottom side of the threads. You'll find four little nubs and holes that should align.

-   :material-numeric-2-circle:{ .lg .middle } Align Mid-Plate & Threads

    ---

    ![Line-Up Parts](/assets/squircle-enclosure/IMG_6755-min.jpg){ loading=lazy }
    Align the two parts using the nubs so that the I/O ports point north, toward the back of the enclosure.

-   :material-numeric-3-circle:{ .lg .middle } Screw Mid-Plate & Threads Together

    ---

    ![Snap Together](/assets/squircle-enclosure/IMG_6757-min.jpg){ loading=lazy }
    Flip the mid-plate over and screw the two parts together with four M3 x 8mm screws.

-   :material-numeric-4-circle:{ .lg .middle } Unlock Top Piece

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6766-min.jpg){ loading=lazy }
    Unlock the top piece and ensure the FPH logo is pointing north.

-   :material-numeric-5-circle:{ .lg .middle } Mount Top Piece to Mid-Plate

    ---

    ![Snap Together](/assets/squircle-enclosure/IMG_6767-min.jpg){ loading=lazy }
    Place the unlocked top piece over the threads so the FPH logo is pointing north, over the back of the enclosure.

-   :material-numeric-6-circle:{ .lg .middle } Practice Locking & Unlocking

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6768-min.jpg){ loading=lazy }
    Rotate the lock ring clockwise to lock the top piece in place. Practice locking and unlocking the top piece.
</div>

!!! success
    You have built your **Satellite1 Squircle Mid-Plate**!

### Speaker Chamber Assembly

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } Slide Mid-Plate Into Position

    ---

    ![See Logos](/assets/squircle-enclosure/IMG_6772-min.jpg){ loading=lazy }
    Slide the mid-plate into the speaker chamber.

-   :material-numeric-2-circle:{ .lg .middle } Screw Down Mid-Plate

    ---

    ![Line-Up Parts](/assets/squircle-enclosure/IMG_6773-min.jpg){ loading=lazy }
    Secure the mid-plate with four M3 x 8mm screws.

-   :material-numeric-3-circle:{ .lg .middle } Connect Speaker Cable

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6783-min.jpg){ loading=lazy }
    Connect the JST-XH 2.54 mm speaker cable connector to the HAT. (NOTE: You can also use Dupont cables if absolutely necessary.)

-   :material-numeric-4-circle:{ .lg .middle } Install Speaker Plug

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6798-min.jpg){ loading=lazy }
    Drop the speaker cable down through the mid-plate, leaving enough length to assemble easily. Use the speaker chamber plug and optional Blu-Tack reusable adhesive to create an airtight seal.

-   :material-numeric-5-circle:{ .lg .middle } Lock Top Piece

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6793-min.jpg){ loading=lazy }
    Position the unlocked top piece over the mid-plate threads with the FPH logo facing north, toward the back of the enclosure. Twist the lock ring clockwise to secure it.

-   :material-numeric-6-circle:{ .lg .middle } Add Polyfill

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6803-min.jpg){ loading=lazy }
    Add a generous amount of polyfill to the speaker chamber, leaving some room for air to flow through the ported vent.

-   :material-numeric-7-circle:{ .lg .middle } Secure & Connect Speaker

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6814-min.jpg){ loading=lazy }
    Screw your chosen speaker to its corresponding faceplate with four M3 x 8mm screws. Connect the speaker cable to the speaker. (NOTE: You can solder or wrap the speaker cables if absolutely necessary.)

-   :material-numeric-8-circle:{ .lg .middle } Screw Down Faceplate

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6816-min.jpg){ loading=lazy }
    Screw down the faceplate with six M3 x 8mm screws. Optionally use Blu-Tack reusable adhesive behind the faceplate to create an airtight seal.

-   :material-numeric-9-circle:{ .lg .middle } Push in Anti-Slip Ring

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6824-min.jpg){ loading=lazy }
    If you printed the TPU anti-slip ring, feel free to push it in now.

-   :material-numeric-10-circle:{ .lg .middle } Connect USB-C Power

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6831-min.jpg){ loading=lazy }
    Connect the USB-C cable to the receptacle to the right of the headphone jack.
</div>

!!! success
    You have built your **Satellite1 Squircle Enclosure**!  Time to go [play some music.](satellite1-streaming-music.md)