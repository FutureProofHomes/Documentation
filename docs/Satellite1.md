# Satellite1

## Assembly & Set Up

Congrats on your shiny new voice assistnat hardware!  In this opening section we will teach you how to assemble your Satellite1:

<iframe width="560" height="315" src="https://www.youtube.com/embed/yqWX86uT5jM?si=qK_A1XmaSsqYQ9js" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


## Installing the Firmware

<div id="firmware-installer" markdown="1">
  <!-- <p><strong>Select Revision:</strong></p> -->
  <label style="display: none"><input type="radio" name="revision" value="rev1"> Revision 1</label>
  <label style="display: none"><input type="radio" name="revision" value="rev2" checked> Revision 2</label>

  <p><strong>Select Version:</strong></p>
  <!-- <p id="warning" style="display: none" ><b>Warning:</b> <br> You have selected a development version. <br> Expect 🪲🪲🪲.</p> -->

  <select id="version-select"></select>
  
  <div id="warning" style="display: none" markdown="1">
!!! warning "Firmware Under Development"

    You have chosen a version of the firmware that is still under active development.  If you're not a developer we recommend running the stable firmware version.
  </div>

  <esp-web-install-button id="install-button" manifest="" install-supported></esp-web-install-button>
</div>

