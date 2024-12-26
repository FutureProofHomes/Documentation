## Introduction

Congrats on your shiny new Satellite1 Voice Assistant & Multi-Sensor hardware!  In this opening section we will teach you how to assemble your Satellite1 and get it fully functional.   This guide is presented in several steps. Each step will bring more functionality to your new toy.

Use the links in the naviation bar on the left of this screen to walk through each section to get your device up and running.  In this section, we'll get it assembled, powered on and recognized by Home Assistant.

## Assembling the Satellite1

<figure markdown="span">
  <video width="100%" class="video-js" loop="" autoplay="" preload="none" muted="" playsinline="" poster="https://futureproofhomes.net/cdn/shop/files/0001.jpg?v=1732152100">
    <source src="https://cdn.shopify.com/videos/c/o/v/84cc43e4fb6a4d4bb303d9beab397b3f.mp4" type="video/mp4"></source>
  </video>
  <figcaption>Animation shows how to attach the rectangular Core Board to the round Hat Board, with an optional mmWave sensor.</figcaption>
</figure>

The Satellite1 comes in 2 pieces, the "Hat" or round board and the "Core" the rectangular board.  You'll notice a standard 40 pin connector on the Hat board (marked in red).  Carefully align the Core board's 2 rows of pins with the Hat's 40 pin connector and press them together.  It will snap together.  Make sure the Core's pins have fully seated into the Hat.

<img width="60%" alt="image" src="/assets/mount_core_to_hat.png">

 <!-- Watch this video to see how easy it is to assemble your Satellite1 boards.
<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> -->

## Powering on the Satellite1
1. Take a USB-C cable and plug one end into the USB socket on the Hat labeled "CORE/ESP".
2. Plug the other end into a USB-C power supply, or a computer. ([Recommended power adapters](recommended-accessories.md#power-supply))
3. Upon first boot you will see a the blue LED's count down clockwise as the device flashes the XMOS audio processor chip.
4. Finally the LEDs will begin to sparkle a warm white color.  Congrats!  Move to the next step:

## Connecting to Home Assistant
Your Satellite1 arrives pre-flashed with all the necessary firmware to get you up and running quickly. You have 2 choices: 

??? abstract "I want to set up via my iPhone or Android device with Bluetooth. (Recommended)"

    <!-- <iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> -->

    Open the Home Assistant Companion App on your Android or iPhone.  Make sure Bluetooth on your phone is on!  Click on settings:

    <img width="60%" alt="image" src="https://github.com/user-attachments/assets/38cb8fb9-beae-42d5-8568-1eb682d93e41">

    Then click on Devices & Services:

    <img width="60%" alt="image" src="https://github.com/user-attachments/assets/107a03d2-8dbe-4a9f-b05f-1f7a7fa6bfd0">

    You should now see a new device has been discovered.  Tap the notification:

    <img width="60%" alt="image" src="https://github.com/user-attachments/assets/42fe24c6-bddf-431e-b993-9190de732bd5">

    Follow the prompts to set up the new device:

    <img width="60%" alt="image" src="https://github.com/user-attachments/assets/22b8d9c9-f182-44c4-bea6-9e2b6a78e41b">

    When you see the following screen, press the Action Button on the Hat labeled "RIGHT"

    <img width="60%" alt="image" src="https://github.com/user-attachments/assets/8ec83264-1fc1-447d-a571-3f22b8eb0e3a">

    Next you'll enter your WiFi credentials to get the Sat1 connected to your network:

    <img width="60%" alt="image" src="https://github.com/user-attachments/assets/76800e3c-46c4-4644-ac42-9b9e81296550">

    If all goes well you should see this:

    <img width="60%" alt="image" src="https://github.com/user-attachments/assets/8e863aa9-e2b1-4387-ad0b-872ef44c270e">

    Next it will ask you to set up ESPHome:

    <img width="60%" alt="image" src="https://github.com/user-attachments/assets/b6b144b2-ca96-4729-8a7c-2fa860470265">

    <!-- TODO: Finish these steps -->

??? abstract "I want to set up via my computer & USB-C cable. (Advanced)"

    Click the "Connect" button below and select the JTAG device in the browser's notification.

    <div id="firmware-installer" markdown="1">
      <esp-web-install-button id="install-button" manifest="https://raw.githubusercontent.com/FutureProofHomes/Documentation/refs/heads/main/manifest.json" install-supported></esp-web-install-button>
    </div>

    <img width="60%" alt="image" src="/assets/ESPHome-SerialConn.png">

    Click Install.

    <img width="60%" alt="image" src="/assets/ESPHome-Install.png">

    Optionally erase the device, then click "Next" and then "Install".

    <img width="60%" alt="image" src="/assets/ESPHome-Erase.png">

    <img width="60%" alt="image" src="/assets/ESPHome-ConfirmInstall.png">

    After about 2 minutes:

    <img width="60%" alt="image" src="/assets/ESPHome-InstallationComplete.png">

    Now connect to your 2.4ghz WiFi network and click "Connect".  Eventually your device will begin sparkling blue.  (**NOTE:** ESP32 devices cannot connect to 5ghz networks.)  

    <img width="60%" alt="image" src="/assets/ConfigureWifi.png">

    Congrats you're now connected to your Wifi.  Your device will now begin sparkling red.  This means it needs to be connected to ESPHome in your Home Assistant instance.

    <img width="60%" alt="image" src="/assets/ESPHome-WiFiConnected.png">

    Inside Home Assistant, go to `Settings` -> `Devices & Services` and notice you have a Discovered `Satellite1 xxxxxx' device.  Click add and follow the onboarding steps.

    <img width="60%" alt="image" src="/assets/discovered_sat1.png">

    Welcome to your Sat1!

[Back to Top](/#introduction)

## Comparing Sat1 to Voice PE

The following table compares the main features of the Sat1 and Home Assistant Voice PE products.  Both products run the same ESP32-S3 and XMOS chip.  Our firmwares are also very similar.  In general, the Sat1 is more feature rich, but lacks the enclosure (hence why we're a Dev Kit).

Enclosure is coming in Q1'25 so feel free to get your Dev Kit now!

| Feature               | Satellite1                                                                                          | Home Assistant Voice PE                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| **Microphones**       | Four high-performance microphones (XMOS firmware uses two microphones currently.  Future firmware upgrade will utalize all 4 microphones with beamforming). | Two microphones designed to hear voice commands in most environments.                 |
| **Speaker Output**    | 25W speaker amplifier capable of 48 kHz audio streaming. Also allows 3.5mm jack for external speakers. | Built-in 3W speaker for 48 kHz playback; includes a 3.5mm stereo jack for external speakers. |
| **Environmental Sensors** | Includes room temperature, humidity, and luminosity sensors; supports adding mmWave presence detection (LD2410 or LD2450). | Primarily focused on voice assistance; does not include additional environmental sensors. |
| **Bluetooth Presence** | Planned but currently non-functional due to firmware/memory challenges.                                       | Not supported.                                                                         |
| **Form Factor**       | Available as a development kit with 4 buit-in buttons and components for assembly; official enclosure planned for future release. | Comes in a ready-to-use injection-molded case with physical controls, including a mute switch and volume dial. |
| **Price**             | $69.99 for the development kit.                                                                     | $59 for the Preview Edition.                                                           |
| **Power**             | Powered by USB-C PD (Power Delivery), enabling the extra power needed for the 25W amplifier.       | Powered by USB-C.                                                                      |
| **Expansion**         | Includes two 40-pin expansion connectors for powerful future accessories.                                   | Grove port for limited expansion.                                                               |
| **LED Ring**          | 24 LEDs for visual feedback.                                                                       | 12 LEDs for visual feedback.                                                           |
| **Software**          | [ESPHome Firmware very similar to Home Assistnat Voice](https://github.com/FutureProofHomes/Satellite1-ESPHome)  | [ESPhome firmware for Home Assistnat Voice](https://github.com/esphome/home-assistant-voice-pe)                                                           |


