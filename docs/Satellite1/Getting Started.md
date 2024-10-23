Congrats on your shiny new voice assistnat hardware!  In this opening section we will teach you how to assemble your Satellite1:

## Assembling the Sat1 Module

<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Flashing the Firmware

To set up your Satellite1 HAT for the first time, follow these steps:

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
