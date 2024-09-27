# Installer

## Initial Setup

Open the box. Magic!

## Install the Firmware

<div id="firmware-installer">
  <!-- <p><strong>Select Revision:</strong></p> -->
  <label style="display: none"><input type="radio" name="revision" value="rev1"> Revision 1</label>
  <label style="display: none"><input type="radio" name="revision" value="rev2" checked> Revision 2</label>

  <p><strong>Select Version:</strong></p>
  <p id="warning" style="display: none" ><b>Warning:</b> <br> You have selected a development version. <br> Expect 🪲🪲🪲.</p>
  <select id="version-select"></select>
  <br><br>

  <esp-web-install-button id="install-button" manifest="" install-supported></esp-web-install-button>
</div>
