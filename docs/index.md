## Introduction

Congrats on your shiny new Satellite1 Voice Assistant & Multi-Sensor hardware!  In this opening section we will teach you how to assemble your Satellite1 and get it fully functional.

<figure markdown="span">
  <video width="100%" class="video-js" loop="" autoplay="" preload="none" muted="" playsinline="" poster="https://futureproofhomes.net/cdn/shop/files/0001.jpg?v=1732152100">
    <source src="https://cdn.shopify.com/videos/c/o/v/84cc43e4fb6a4d4bb303d9beab397b3f.mp4" type="video/mp4"></source>
  </video>
  <figcaption>Animation shows how to attach the rectangular Core Board to the round Hat Board, with an optional mmWave sensor.</figcaption>
</figure>

## Prerequisites

The Satellite1 has a few requirements to get up and running.

1. An active installation of [Home Assistant](https://www.home-assistant.io/installation/)
2. A 2.4ghz wifi network (internet is not required)
3. The recommended Satellite1 accessories (see [Recommended Accessories](recommended-accessories.md))

## Assembling the Satellite1

The Satellite1 comes in 2 pieces: 

- The "Hat" (round board) 
- The "Core" (rectangular board)

You'll notice a standard Raspberry Pi 40-pin connector on the Hat board (marked in red).  Carefully align the Core board's 2 rows of pins with the Hat's 40 pin connector and press them together.

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

    Open the Home Assistant Companion App on your Android or iPhone.  Make sure Bluetooth on your phone is on and that you're nearby the Sat1!  
    
    1. <b>Tap "Settings":</b>
    <br><img width="50%" alt="image" src="/assets/ble_improv/1_go_to_settings.png">

    2. <b>Tap "Devices & Services":</b>
    <br><img width="50%" alt="image" src="/assets/ble_improv/2_go_to_devices.png">

    3. <b>Tap "Add" next to your Sat1 device (contains last 6 of device MAC address):</b>
    <br><img width="50%" alt="image" src="/assets/ble_improv/3_improv_discovered_device.png">

    4. <b>Type in your 2.4ghz network credentials:</b>
    <br><img width="50%" alt="image" src="/assets/ble_improv/4_improv_add_wifi_credentials.png">

    5. <b>On the Sat1 HAT, press the right "Action button" to give authorization:</b>
    <br><img width="50%" alt="image" src="/assets/ble_improv/5_improv_press_authorization_button.png">
    <img width="50%" alt="image" src="/assets/ble_improv/6_click_action_button.png">

    6. <b>Tap "Continue" after successfull Wifi connection:</b>
    <br><img width="50%" alt="image" src="/assets/ble_improv/8_improv_successful_wifi_connection.png">

    7. <b>Tap "Ok" to begin setting up ESPHome:</b>
    <br><img width="50%" alt="image" src="/assets/ble_improv/9_esphome_setup_request.png">

    8. <b>Tap the name if your Sat1 device and then tap the "Submit" button:</b>
    <br><img width="50%" alt="image" src="/assets/ble_improv/10_esphome_select_device.png">

    9. <b>The Wizard will pull down the most recent Sat1 Firmware:</b>
    <br><img width="50%" alt="image" src="/assets/ble_improv/12_wizard_checking_for_updates.png">

    10. <b>The Wizard will ask you to say the Wake Word twice:</b>
    <br><img width="50%" alt="image" src="/assets/ble_improv/13_wizard_first_wake_word_test.png">

    11. <b>Type the Area this Sat1 falls in:</b>
    <br><img width="50%" alt="image" src="/assets/ble_improv/15_wizard_assign_area.png">

    12. <b>Stick with the default or change the wake word, conversation agent, and voice:</b>
    <br><img width="50%" alt="image" src="/assets/ble_improv/16_wizard_quick_pipeline_config.png">

    13. <b>After completing the Wizard, do NOT click to add the Sat1 to ESPHome again.  Simply refresh and this will go away.</b>
    <br><img width="50%" alt="image" src="/assets/ble_improv/17_ignore_device_discovered.png">

    Congrats.  You're done!

??? abstract "I want to set up via my computer & USB-C cable. (Advanced)"

    Plug your Sat1 directly into your computer with a USB-C cable that supports a data connection.

    1. <b>Click <esp-web-install-button id="install-button" manifest="https://raw.githubusercontent.com/FutureProofHomes/Documentation/refs/heads/main/manifest.json" install-supported></esp-web-install-button> and select the JTAG device in the browser's notification:</b>
    <br><img width="50%" alt="image" src="/assets/ESPHome-SerialConn.png">

    2. <b>Click "Install":</b>
    <br><img width="50%" alt="image" src="/assets/ESPHome-Install.png">
    
    3. <b>Optionally erase the device, then click "Next" and then "Install":</b>
    <br><img width="50%" alt="image" src="/assets/ESPHome-Erase.png">
    <br><img width="50%" alt="image" src="/assets/ESPHome-ConfirmInstall.png">

    4. <b>Installation will complete. Click "Next":</b>
    <br><img width="50%" alt="image" src="/assets/ESPHome-InstallationComplete.png">

    5. <b>Type in your2.4ghz WiFi network and click "Connect".  Your device will begin sparkling blue while attempting to connect.</b>
    <br><img width="50%" alt="image" src="/assets/ConfigureWifi.png">

    6. <b>Congrats you're now connected to your Wifi.  Your device will now begin sparkling red.  This means it needs to be connected to ESPHome in your Home Assistant instance.</b>
    <br><img width="50%" alt="image" src="/assets/ESPHome-WiFiConnected.png">

    7. <b>Inside Home Assistant, go to "Settings -> Devices & Services" and notice you have a Discovered `Satellite1 xxxxxx' device.  Click add and follow the onboarding steps.</b>
    <br><img width="50%" alt="image" src="/assets/discovered_sat1.png">

    Congrats.  You're done!

## User Interface Control
Once your Sat1 is connected to Home Assistnat you should familiarize yourself with all the server-side settings you may want to change:

  1. <b>Inside your Home Assistnat, head over to "Settings -> Devices & Services -> ESPHome" and click on your Sat1 device:</b>
  <br><img width="100%" alt="image" src="/assets/esphome/1_esphome_device_list.png">

  2. <b>Understand all the features of your Sat1 device:</b>
  <br><img width="100%" alt="image" src="/assets/esphome/2_esphome_top_page.png">
  <br><img width="100%" alt="image" src="/assets/esphome/3_esphome_bottom_page.png">



## Comparing Sat1 to Voice PE

The following table compares the main features of the Sat1 and Home Assistant Voice PE products.  Both products run the same ESP32-S3 and XMOS chip.  Our firmwares are also very similar. In general, the Sat1 is more feature rich, but lacks the enclosure (hence why we're a Dev Kit).  Our enclosure is coming in Q1'25 so feel free to get your Dev Kit now!

| Feature               | Satellite1                                                                                          | Home Assistant Voice PE                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| **Microphones**       | Four high-performance microphones (XMOS firmware uses two microphones currently.  Future firmware upgrade will utalize all 4 microphones with beamforming). | Two microphones designed to hear voice commands in most environments.                 |
| **Speaker Output**    | 25W speaker amplifier capable of 48 kHz audio streaming. Also allows 3.5mm jack for external speakers. | Built-in 3W speaker for 48 kHz playback; includes a 3.5mm stereo jack for external speakers. |
| **Environmental Sensors** | Includes room temperature, humidity, and luminosity sensors; supports adding mmWave presence detection (LD2410 or LD2450). | Primarily focused on voice assistance; does not include additional environmental sensors. |
| **Form Factor**       | Available as a development kit with 4 buit-in buttons and components for assembly; official enclosure planned for future release. | Comes in a ready-to-use injection-molded case with physical controls, including a mute switch and volume dial. |
| **Price**             | $69.99 for the development kit.                                                                     | $59 for the Preview Edition.                                                           |
| **Power**             | Powered by USB-C PD (Power Delivery), enabling the extra power needed for the 25W amplifier.       | Powered by USB-C.                                                                      |
| **Expansion**         | Includes two 40-pin expansion connectors for powerful future accessories.                                   | Grove port for limited expansion.                                                               |
| **LED Ring**          | 24 LEDs for visual feedback.                                                                       | 12 LEDs for visual feedback.                                                           |
| **Software**          | [ESPHome Firmware very similar to Home Assistant Voice](https://github.com/FutureProofHomes/Satellite1-ESPHome)  | [ESPhome firmware for Home Assistant Voice](https://github.com/esphome/home-assistant-voice-pe)                                                           |

[Back to Top](/#introduction)