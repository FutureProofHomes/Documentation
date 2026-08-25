There are three ways to connect a mmWave sensor to a Satellite1. Which one you use depends on your Hat board revision and where the sensor needs to point.

Not sure which sensor to buy? Start with the [mmWave Overview](satellite1-mmwave-overview.md).

## Connection Methods

The Sat1 HAT has headers for directly mounting either the LD2410 or LD2450. Direct mounting is typically best for in-ceiling installations, because the sensor points in the same direction as the LEDs and microphones.

The latest Satellite1.1 HAT also includes an LD2450 connector on the underside of the board. This lets you mount the sensor in any orientation with a 4-pin JST-ZH cable.

<div class="grid cards" markdown>

-  :material-numeric-1-circle:{ .lg .middle } __LD2450 Cable Connect (Recommended)__

    ---

    <figure markdown="span">
      ![LD2450 4-pin mmWave](/assets/presence-sensors/sat1.1_ld2450_square.png){ loading=lazy}
      <figcaption>Latest Sat1.1 Hat board offers a 4-pin JST cable.</figcaption>
    </figure>
    [Get LD2450 and Harness Cable](https://futureproofhomes.net/products/ld2450-mmwave-human-presence-sensor){ .md-button .md-button--primary }

-   :material-numeric-2-circle:{ .lg .middle } __LD2450 Direct Connect__

    ---

    <figure markdown="span">
      ![LD2450 mmWave](/assets/presence-sensors/sat1_ld2450.jpg){ loading=lazy}
      <figcaption>Original Sat1 with direct-mounted LD2450</figcaption>
    </figure>

-  :material-numeric-3-circle:{ .lg .middle } __LD2410 Direct Connect__

    ---

    <figure markdown="span">
      ![LD2410 mmWave](/assets/presence-sensors/sat1_ld2410.jpg){ loading=lazy}
      <figcaption>Original Sat1 with direct-mounted LD2410</figcaption>
    </figure>
</div>

## Enclosure Compatibility

???+ "Not all enclosures support mmWave"

    Only some Satellite1 enclosures support mmWave sensors.

    1. Our new [Sat1.1 Smart Speaker](https://futureproofhomes.net/products/satellite1-smart-speaker) fits the LD2450 using a 4-pin cable.
    2. Our older DIY [Cylindrical Enclosure](satellite1-cylindrical-enclosure.md) fits both mmWave sensors when mounted directly to the HAT.
    3. In-ceiling enclosures are coming soon.

## Confirming Detection

The latest firmware automatically detects if and which mmWave sensor is connected to your Sat1. To confirm detection, open your Sat1's **Diagnostics** section and scroll to the bottom to see which radar is listed.

!!! note "Upgrading from v0.1.x mmWave firmware?"

    Your previous Sat1 mmWave automations may need updates because v0.2.0 exposes new radar entities in the Sat1 ESPHome UI.

## Updating the Radar Firmware

!!! warning "Required for the LD2450"

    The LD2450 must be running firmware newer than **V2.02.23090617** to work with ESPHome. Check and update it before tuning.

Both the LD2410 and LD2450 can be updated over Bluetooth with the HLKRadarTool mobile app. Download the app, then watch the quick video below to learn how to access the sensor and change the firmware version.

<div style="display: flex; align-items: center; gap: 8px; margin: 1em 0;">
  <a href="https://apps.apple.com/us/app/hlkradartool/id1638651152">
    <img style="height: 44px;" src="https://developer.apple.com/assets/elements/badges/download-on-the-app-store.svg" alt="Download on the App Store"/>
  </a>
  <a href="https://play.google.com/store/apps/details?id=com.hlk.hlkradartool&hl=en_US&pli=1">
    <img style="height: 64px;" src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" alt="Get it on Google Play"/>
  </a>
</div>

<iframe style="width: 100%; aspect-ratio: 16 / 9;" src="https://www.youtube.com/embed/t8-JdVVVH34?si=3HRSFepdfceSfEtx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Next Steps

[Tune detection :material-arrow-right:](satellite1-mmwave-tuning.md){ .md-button .md-button--primary }
