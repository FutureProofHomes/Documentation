## Overview
The "Squircle Enclosure Family" for the Satellite1 Dev Kit includes three optional speaker chamber sizes—small (1-inch), medium (2.5-inch), and large (3-inch)—with the top components of the design remaining identical across all sizes. The entire enclosure is designed to be assembled using M3 x 12mm screws.

## Understanding the Design
<figure markdown="span">
  ![Squircle Enclosure Overview](/assets/squircle-enclosure/part_overview.png){ width="100%" }
  <figcaption>Common parts of all squircle enclosures are the Top Plate, Diffuser Ring, PCB Spacer & Lock Ring</figcaption>
</figure>

## Choose an Enclosure & Speaker Model

<div class="grid cards" markdown>

-   :material-numeric-3-circle:{ .lg .middle } Large (3-Inch) Speaker Enclosure

    ---

    ![Large 3-Inch Squircle Enclosure](/assets/squircle-enclosure/IMG_6841_min.jpg){ loading=lazy }
    <br> [Dayton Audio PC83-4](https://amzn.to/43AgLry)
    <br> [Dayton Audio RS75-4](https://amzn.to/42egKsz)
    <br> [GRS 3FR-4](https://amzn.to/4kII61D)
    <br> [Visaton FRS8-4](https://amzn.to/43FgNOP)
    <br> [Tectonic TEBM46C20N-4B BMR](https://www.parts-express.com/Tectonic-TEBM46C20N-4B-BMR-3-Full-Range-Speaker-4-297-2157)
    <br> [FaitalPRO 3FE25](https://amzn.to/4jsB3Jp)

-   :material-numeric-2-circle:{ .lg .middle } Medium (2-Inch) Speaker Enclosure

    ---

    ![Medium 2-Inch Squircle Enclosure](/assets/squircle-enclosure/coming_soon.jpg){ loading=lazy }
    <br> [Dayton Audio ND65-4](https://amzn.to/43N5PrD)
    <br> [Dayton Audio ND64-4](https://amzn.to/3H7MN6G)
    <br> [Dayton Audio PC68-4](https://amzn.to/3HeSoIn)

-   :material-numeric-1-circle:{ .lg .middle } Small (1-Inch) Speaker Enclosure

    ---

    ![Small 1-Inch Squircle Enclosure](/assets/squircle-enclosure/coming_soon.jpg){ loading=lazy }
    <br> [DWEII 4pcs Mini Speaker Dupont Connectors](https://amzn.to/3HqLnEc)
    <br> [AOICRIE 2pcs 3 Watt Mini Dupont Connectors](https://amzn.to/3SSDtG6)
</div>

## Enclosure Limitations
Many of the below enclosure limitations are solved by our upcoming [power-over-ethernet SHOE board](satellite1-poe-shoe-module-overview.md)

Without the SHOE board there are some current limitations of the enclosure:

1. **The lux sensor will not give accurate readings of the room.**
<br>We will solve this with a light pipe and updated enclosure designs.  This can also be solved by our upcoming SHOE board and relocating the lux sensor down in the speaker chamber.

2. **The temp/humidity sensor will not give accurate readings of the room.  Also the mmWave sensor is pointed up at the ceiling.**
<br>Our upcoming "SHOE" PCB will relocate these sensors down into the speaker chamber while also giving a PoE port to the enclosure!

3. **The wake word may not respond when playing music at full volume.**
<br>We will experiment with modified enclosure designs, gaskets, and better audio echo cancellation firmware to mitigate vibrations in the enclosure.

## How to 3D Print the Enclosures

<figure markdown="span">
  ![Squircle Enclosure Overview](/assets/squircle-enclosure/slicer_software_screenshot.png){ width="100%" }
  <figcaption>Remove any plates you don't need, depending on your speaker choice, enclosure type, and whether your printer supports multi-material or multi-part printing.</figcaption>
</figure>

### Pre-Built Slicer Project File
    
1. Download the appropriate pre-built `.3mf` project file from our Github repository and open in your favorite slicer software:
    1. [Get OrcaSlicer Project File](https://github.com/FutureProofHomes/Satellite1-Enclosures/tree/main/Squircle%20Enclosures/Project%20Files){ .md-button .md-button--primary }
    2. [Get Bambu Studio Project File](https://github.com/FutureProofHomes/Satellite1-Enclosures/tree/main/Squircle%20Enclosures/Project%20Files){ .md-button .md-button--primary }

2. Right-click on each part in your slicer software and select your desired filament.
    1. **NOTE #1:** PETG-HF is better for acoustics, but PLA will work too.
    2. **NOTE #2:** Set Diffuser Ring to transparent or white filament so you can see the LEDs.

3. No supports are needed.

### Custom-Built Slicer Project

If you cannot or do not want to use our pre-built slicer project file then you can build your own plate from scratch:

1. Add the necessary `.stl` geometry files to your slicer software from the [Satellite1-Enclosures Github repository](https://github.com/FutureProofHomes/Satellite1-Enclosures).
2. Set your project to use the recommended settings.
    1. 0.2mm layer height
    2. 3-6 wall loops for strength
    3. Minimum 15% infill (increase this to 50% for the speaker enclosure for even better acoustics)
    4. (Optional) Arachne or Gyroid wall generator
    6. No-Brim

## Top Plate Assembly

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } Install Diffuser Ring

    ---

    ![Press in place](/assets/squircle-enclosure/IMG_6828-min.jpg){ loading=lazy }
    If you printed the diffuser ring as a separate part, apply light pressure around the ring to snap it in place. If you used our multi-material print, you can skip this step.

-   :material-numeric-2-circle:{ .lg .middle } Align the FPH Logos

    ---

    ![Line-Up Parts](/assets/squircle-enclosure/IMG_6748-min.6747){ loading=lazy }
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
    By hand, secure the Dev Kit to the top piece with four M3 x 12mm screws. Do not overtighten the screws.
</div>

!!! success
    You have built your **Satellite1 Squircle Top Plate**!

## Mid-Plate Assembly

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
    Flip the mid-plate over and screw the two parts together with four M3 x 12mm screws.

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

## Speaker Chamber Assembly

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } Slide Mid-Plate Into Position

    ---

    ![See Logos](/assets/squircle-enclosure/IMG_6772-min.jpg){ loading=lazy }
    Slide the mid-plate into the speaker chamber.

-   :material-numeric-2-circle:{ .lg .middle } Screw Down Mid-Plate

    ---

    ![Line-Up Parts](/assets/squircle-enclosure/IMG_6773-min.jpg){ loading=lazy }
    Secure the mid-plate with four M3 x 12mm screws.

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
    Screw your chosen speaker to its corresponding faceplate with four M3 x 12mm screws. Connect the speaker cable to the speaker. (NOTE: You can solder or wrap the speaker cables if absolutely necessary.)

-   :material-numeric-8-circle:{ .lg .middle } Screw Down Faceplate

    ---

    ![Rotate Parts to Unlock](/assets/squircle-enclosure/IMG_6816-min.jpg){ loading=lazy }
    Screw down the faceplate with six M3 x 12mm screws. Optionally use Blu-Tack reusable adhesive behind the faceplate to create an airtight seal.

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