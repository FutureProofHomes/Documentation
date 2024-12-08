---
title: Start Here
description: Installation guide for Satellite1
---
<video width="250" height="250"class="video-js" loop="" autoplay="" preload="none" muted="" playsinline="" poster="https://futureproofhomes.net/cdn/shop/files/0001.jpg?v=1732152100"> <source src="https://cdn.shopify.com/videos/c/o/v/84cc43e4fb6a4d4bb303d9beab397b3f.mp4" type="video/mp4" >
</video>>

Congrats on your shiny new voice assistant hardware!  In this opening section we will teach you how to assemble your Satellite1 and get it fully functional

## Assembling the Satellite1 Module (Hat board+ Core Board):
Watch this video to see how easy it is to assemble your Satellite1 boards.

<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Configuring your Satellite1
Your Satellite1 arrives pre-configured with all the necessary firmware to get you up and running quickly. Now you have 2 choices,  Install and configure it with the easy method, or install it with the more complicated method (advanced users).

To set up your Satellite1 HAT for the first time, follow these steps:

![![easiest](assets/label-easiest.png)](../assets/label-easiest.png)

## <a name="EasyMode"></a> Easy Method
This is the method we recommend for most users. Watch this video to see how easy it is to get your Satellite1 operational right away.

<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Initial Set up steps
Unbox your new Satellite1.  You'll see it comes in 2 pieces, the "Hat" or round board and the "Core" the rectangular board.  Lay the Hat on a flat surface with the buttons facing down.  

<img width="271" alt="image" src="https://github.com/user-attachments/assets/ee2c9a4c-2ed6-48b1-87e0-aae0122690dd">

Next, take the Core board and face it down as follows:

<img width="300" alt="image" src="https://github.com/user-attachments/assets/b11b02a2-7041-4144-aacc-5d2ee322e320">

You'll notice 2 rows of pin sockets underneath the label "Expansion Module 1" on the Hat board. Carefully align the Core board's 2 rows of pins with the Hat's 2 rows of pin sockets and press them together. It will snap together.  Make sure the Core's pins have fully seated into the Hat.  It should look like this once you're done:

<img width="300" alt="image" src="https://github.com/user-attachments/assets/b844a350-4328-4cd3-9f52-10981c220fd8">

Next take a USB C cable and plug it into the USB socket labeled  CORE/ESP.
The LEDs will flash Blue & sparkly and then eventually a series of Blue LED's will count down clockwise as the device boots up.
Next open the Home Assistant Companion App on your Adroid or iPhone.  Make sure your BlueTooth on your phone is on!  Click on settings:

<img width="150" alt="image" src="https://github.com/user-attachments/assets/38cb8fb9-beae-42d5-8568-1eb682d93e41">

Then click on Devices & Services:

<img width="150" alt="image" src="https://github.com/user-attachments/assets/107a03d2-8dbe-4a9f-b05f-1f7a7fa6bfd0">

You should now see a new device has been discovered:

<img width="150" alt="image" src="https://github.com/user-attachments/assets/42fe24c6-bddf-431e-b993-9190de732bd5">

Follow the prompts to set up the new device:

<img width="150" alt="image" src="https://github.com/user-attachments/assets/22b8d9c9-f182-44c4-bea6-9e2b6a78e41b">

When you see the following screen, press the Action Button on the Hat labeled "RIGHT"

<img width="150" alt="image" src="https://github.com/user-attachments/assets/8ec83264-1fc1-447d-a571-3f22b8eb0e3a">

Next you'll enter your WiFi credentials to get the Sat1 connected to your network:

<img width="150" alt="image" src="https://github.com/user-attachments/assets/76800e3c-46c4-4644-ac42-9b9e81296550">

If all goes well you should see this:

<img width="150" alt="image" src="https://github.com/user-attachments/assets/8e863aa9-e2b1-4387-ad0b-872ef44c270e">

Next it will ask you to set up ESPHome:

<img width="150" alt="image" src="https://github.com/user-attachments/assets/b6b144b2-ca96-4729-8a7c-2fa860470265">

ADD ESPHOME CORRECTED STUFF HEFRE.

<img width="150" alt="image" src="https://github.com/user-attachments/assets/34c35699-f504-4a43-89f8-a28f3c946f60">

![Advanced](../assets/label-expert.png)

## <a name="ExpertMode"></a> Expert/Advanced Method

!!! note
    You **MUST** use a browser that supports serial communications such as Chrome, Microsoft Edge, Firefox, Opera, and Safari.

1.  Connect the Satellite1 HAT to your computer using a USB-C cable.
2.  Select your desired firmware version from the dropdown below and then click the "Connect" button.
    1.  Follow through the steps to connect your Satellite1 to your local network.
    1.  When the ESP32 has booted for the first time it will flash the XMOS chip.

Once these steps are complete, you can then update your Satellite1 HAT wirelessly (over-the-air) without needing a physical connection to your computer.

<div id="firmware-installer" markdown="1">
  <esp-web-install-button id="install-button" manifest="https://raw.githubusercontent.com/FutureProofHomes/Documentation/refs/heads/main/manifest.json" install-supported></esp-web-install-button>
</div>

<img width="350" alt="image" src="/assets/ESPHome-SerialConn.png">

And then:

<img width="350" alt="image" src="/assets/ESPHome-Install.png">

And then:

<img width="350" alt="image" src="/assets/ESPHome-Erase.png">

And then:

<img width="350" alt="image" src="/assets/ESPHome-ConfirmInstall.png">

And then after about 2 minutes:

<img width="350" alt="image" src="/assets/ESPHome-InstallationComplete.png">

Now connect to your WiFi network and Connect

<img width="350" alt="image" src="/assets/ConfigureWifi.png">

<img width="350" alt="image" src="/assets/ESPHome-WiFiConnected.png">

## Home Assistant Voice Integration

Your Satellite1 should be autodetected in your Home Assistant.  Watch the video below to see how initialize your Satellite1 with Home Assistant:

<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Bluetooth Room Presence Detection

If you have multiple Satellite1's in each room of your home you can track your smart watch or phone to determine what room you're in:

<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Helpful Blueprint Automations

Here are a handful of very popular automations and use cases for your new voice assistant and multi-sensor:

<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
