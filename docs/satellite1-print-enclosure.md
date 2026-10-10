The enclosure is published for anyone to print or remix. Printing it yourself replaces the Enclosure Kit, so you buy only the boards and the audio parts that go inside.

## Get the files

3MF project files, STL and STEP are all published.

[GitHub :material-github:](https://github.com/FutureProofHomes/Satellite1-Enclosures/tree/main/OEM%20Enclosures/Satellite1.1%20Smart%20Speaker%20Enclosure%20Kit){ .md-button }
[MakerWorld :material-printer-3d:](https://makerworld.com/models/2615819-futureproofhomes-oem-satellite1-1-smart-speaker){ .md-button }

## What you are printing

| Part | Notes |
|---|---|
| **Front chamber** | Holds the drivers and the crossover. Has a pocket for an LD2450 mmWave sensor |
| **Back chamber** | Carries the bass port and a dedicated pocket for the external Wi-Fi antenna |
| **Top plate** | Either one multi-material part with the diffuser built in, or a plain top you pair with a separate diffuser |
| **LED diffuser** | Sits over the 24-LED ring. Part of the multi-material top, or printed on its own and snapped in |
| **Screw guide tool** | Stops you driving the screws in too far during assembly |

The retail Enclosure Kit is printed in Bambu Lab PETG-HF, Dark Gray 33103 or White 33100, which is what the Charcoal Gray and Bone White finishes are.

### Two ways to do the top

The top and diffuser are published both as a single multi-material part and as two separate parts. Pick on the printer you have rather than on the result, because they finish the same.

- **Multi-material** prints the top and the diffuser together, so there is nothing to assemble and no seam. It needs a printer that can change material mid-print.
- **Separate parts** print the top and the diffuser individually, and you snap the diffuser in during assembly. This works on any single-extruder machine, and it lets you choose the diffuser material independently.

## Slicer settings

0.4 mm nozzle, dry Bambu-grade PETG throughout. No supports are needed on any part.

| Parts | Walls | Infill |
|---|---|---|
| Front and back speaker chambers | 3 perimeters | 30% cubic |
| Top plate, screw guide, diffuser | 3 perimeters | 15% cubic |

The chambers carry more infill than the rest because they are doing acoustic work, not just holding a shape. An under-filled chamber flexes, and a chamber that flexes leaks bass and colors the sound.

Print the diffuser in transparent PETG, or white PLA, so the LED ring reads clearly through it. Anything opaque defeats it. On the multi-material top that applies to the diffuser region rather than to a separate part.

!!! warning "An airtight seal is the point"

    The front chamber is sealed and the back is ported, and the enclosure only sounds right if that holds. Layer gaps, a warped mating face or a loose fit around the JST cable will all cost you bass. This is the part worth reprinting if it comes out badly.

## What you still have to buy

Printing replaces the Enclosure Kit, not the parts inside it. You still need the Dev Kit for the boards and the Electronics Kit for the audio components, along with the screws, hex wrench and sealing foam the Enclosure Kit would otherwise have supplied.

!!! note "The drivers are not arbitrary"

    The enclosure is acoustically and mechanically designed around a specific woofer, tweeter and crossover, chosen for how they pair with the Hat's amplifier. Substituting other drivers, or reshaping the enclosure to fit them, affects both sound quality and wake word performance. The Electronics Kit bundles the matched set, or the parts are sold individually.

## Then build it

[Build a Smart Speaker :material-arrow-right:](satellite1-smart-speaker.md){ .md-button .md-button--primary }
