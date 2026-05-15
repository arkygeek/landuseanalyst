<!--
  catchment_mask.qml — default style for catchment-output binary mask
  rasters. One class (value 1) drawn semi-transparent in a saturated colour;
  null cells fully transparent.

  Loaded at runtime by la.gui.lacatchmenttask.LaCatchmentTask via
  QgsRasterLayer.loadNamedStyle().
-->
<qgis version="3.0" hasScaleBasedVisibilityFlag="0">
  <pipe>
    <rasterrenderer opacity="0.6" alphaBand="-1" classificationMin="1" classificationMax="1" band="1" type="singlebandpseudocolor">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader colorRampType="EXACT" clip="0">
          <item alpha="220" value="1" label="catchment" color="#3B5A8C"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeGreen="128" colorizeOn="0" colorizeRed="255" colorizeBlue="128" grayscaleMode="0" saturation="0" colorizeStrength="100"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
