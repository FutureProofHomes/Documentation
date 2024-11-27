<video width="250" height="250"class="video-js" loop="" autoplay="" preload="none" muted="" playsinline="" poster="https://futureproofhomes.net/cdn/shop/files/0001.jpg?v=1732152100"> <source src="https://cdn.shopify.com/videos/c/o/v/84cc43e4fb6a4d4bb303d9beab397b3f.mp4" type="video/mp4" >
</video>>

Congrats on your shiny new voice assistant hardware!  In this opening section we will teach you how to assemble your Satellite1 and get it fully functional

## Assembling the Satellite1 Module (Hat board+ Core Board):
Watch this video to see how easy it is to assemble your Satellite1 boards.

<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Configuring your Satellite1
Your Satellite1 arrives pre-configured with all the necessary firmware to get you up and running quickly. Now you have 2 choices,  Install and configure it with the easy method, or install it with the more complicated method (advanced users).

To set up your Satellite1 HAT for the first time, follow these steps:
## Easy Method
This is the method we recommend for most users. Watch this video to see how easy it is to get your Satellite1 operational right away.

<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Advanced Method

NOTE: You **MUST** use a browser that supports serial communications such as Chrome, Microsoft Edge, Firefox, Opera, and Safari.

1.  Connect the Satellite1 HAT to your computer using a USB-C cable.
2.  Select your desired firmware version from the dropdown below and then click the "Connect" button.
    1.  Follow through the steps to connect your Satellite1 to your local network.
    1.  When the ESP32 has booted for the first time it will flash the XMOS chip.

Once these steps are complete, you can then update your Satellite1 HAT wirelessly (over-the-air) without needing a physical connection to your computer.

<div id="firmware-installer" markdown="1">
  <!-- <p><strong>Select Revision:</strong></p> -->
  <label style="display: none"><input type="radio" name="revision" value="rev1"> Revision 1</label>
    <label style="display: none"><input type="radio" name="revision" value="rev2"> Revision 1</label>
  <label style="display: none"><input type="radio" name="revision" value="rev3" checked> Revision 2</label>

  <p><strong>Select the ESPHome Firmware Version:</strong></p>
  <!-- <p id="warning" style="display: none" ><b>Warning:</b> <br> You have selected a development version. <br> Expect 🪲🪲🪲.</p> -->

  <select id="version-select"></select>
  
  <div id="warning" style="display: none" markdown="1">
!!! warning "Firmware Under Development"

    You have chosen a version of the firmware that is still under active development.  If you're not a developer we recommend running the stable firmware version.
  </div>

  <esp-web-install-button id="install-button" manifest="" install-supported></esp-web-install-button>
</div>

## Home Assistant Voice Integration

Your Satellite1 should be autodetected in your Home Assistant.  Watch the video below to see how initialize your Satellite1 with Home Assistant:

<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Bluetooth Room Presence Detection

If you have multiple Satellite1's in each room of your home you can track your smart watch or phone to determine what room you're in:

<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Helpful Blueprint Automations

Here are a handful of very popular automations and use cases for your new voice assistant and multi-sensor:

<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
