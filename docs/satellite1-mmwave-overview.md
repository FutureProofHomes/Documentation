Satellite1 supports mmWave radar sensors for detecting human presence in a room. This is useful when you want Sat1 to automate actions like turning on a light or starting a conversation when someone enters.

Two sensors are supported. Pick one based on how much detail you need about *where* people are, not just *whether* they're there.

<div class="grid cards" markdown>

-  :material-numeric-1-circle:{ .lg .middle } __LD2410 mmWave module__

    ---

    The LD2410 is a small but capable presence sensor. It detects both motion and still human presence up to 6 meters away, with a detection angle of +/-60 degrees. For best results, tune it after installation. It can also detect through materials like glass walls and thin plywood.

    <figure markdown="span">
      ![LD2410 mmWave](/assets/presence-sensors/sat1_ld2410.jpg){ loading=lazy}
      <figcaption>Original Sat1 with direct-mounted LD2410</figcaption>
    </figure>

    ???+ warning "The LD2410B includes Bluetooth for updating the radar firmware. The standard LD2410 does not include Bluetooth. Sat1 is compatible with both versions."
    [Get LD2410 on Amazon](https://amzn.to/3C6utsf){ .md-button .md-button--primary }

-   :material-numeric-2-circle:{ .lg .middle } __LD2450 mmWave module__

    ---

    The LD2450 is a more advanced presence sensor. It can track up to 3 moving occupants while also detecting still human presence up to 8 meters away. It has a detection angle of +/-60 degrees and can detect through materials like glass walls and thin plywood.

    <figure markdown="span">
      ![LD2450 mmWave](/assets/presence-sensors/sat1_ld2450.jpg){ loading=lazy}
      <figcaption>Original Sat1 with direct-mounted LD2450</figcaption>
    </figure>
    <figure markdown="span">
      ![LD2450 4-pin mmWave](/assets/presence-sensors/sat1.1_ld2450_square.png){ loading=lazy}
      <figcaption>Latest Sat1.1 supports LD2450 connected with the 4-pin harness cable</figcaption>
    </figure>

    ???+ warning "The LD2450 must be running firmware version greater than V2.02.23090617 to work with ESPHome. Learn how to [update the firmware](satellite1-mmwave-installation.md#updating-the-radar-firmware)."
    [Get LD2450 and Cable](https://futureproofhomes.net/products/ld2450-mmwave-human-presence-sensor){ .md-button .md-button--primary }
</div>

## Understanding the LD2410

  1. **Gate**: the LD2410 divides its detection range into distance bands called gates. Each gate can be tuned separately. Think of the gates like layers extending outward from the sensor. The LD2410 has 8 useful gates, plus gate 0, which is usually not helpful for tuning.

  2. **Distance Resolution**: distance resolution controls the size of each gate. The LD2410 can use 75 cm or 20 cm per gate. At 75 cm per gate, the maximum range is `0.75 * 8 =` 6 meters. At 20 cm per gate, the maximum range is 1.6 meters, but tuning can be more precise.

  3. **Energy**: energy is the amount of detected activity in a gate. More movement usually creates a higher energy value.

## Understanding the LD2450

  1. **Target Tracking**: unlike the gate-based LD2410, the LD2450 tracks up to 3 individual targets at the same time using X/Y coordinates. Each target reports its position, distance, speed, and direction, giving you a real-time map of where occupants are in the room.

  2. **Zones**: you can define up to 3 zones on the coordinate grid. When a target enters a zone, that zone's occupancy sensor turns on. You can also define an exclusion zone to ignore motion from areas like a ceiling fan or a window with moving curtains.

## Next Steps

[Install a sensor :material-arrow-right:](satellite1-mmwave-installation.md){ .md-button .md-button--primary }
[Tune detection :material-arrow-right:](satellite1-mmwave-tuning.md){ .md-button }
