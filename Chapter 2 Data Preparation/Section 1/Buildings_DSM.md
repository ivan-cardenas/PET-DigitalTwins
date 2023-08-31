## 6. Building Footprints

a.	Through the National Provision for Key Register Addresses and Buildings. You can obtain the building footprints for all of The Netherlands. The BAG 2.0 Extract contains the Basisregistratie Adressen en Gebouwen (BAG) data that is available free of charge. On the 8th day of every month, a new Extract with the current data is created

b.	You can download the files from the open website https://www.kadaster.nl/-/kosteloze-download-bag-2.0-extract  these are way easier to download. 

## 7. Digital Surface Model (DSM)

The DSM represents the Earth's surface including all above-ground features like buildings, trees, and other structures. It captures the elevations of these features, resulting in a surface that includes both the bare ground and the objects on it.

The AHN4 0.5 meter raw grid (DSM) is intended as a raw file, where both ground level and non-ground level objects (trees, buildings, bridges and other objects) have been resampled from the point cloud into a 0.5 meter grid. No further edits have been made. For the Netherlands access the  Actueel Hoogtebestand Nederland 4  (AHN 4) data repository where the Digital Surface Model (DSM) and Digital Terrain Model (DTM)  files for your study area are available: 
https://www.arcgis.com/apps/Embed/index.html?appid=73433bc06f7640949f32e4f8e3842e7a 

Locate and download the DSM files for your desired study area in a suitable format. The DSM is available at a scale resolution of 0.5m and 5m. Be careful, as the lower the number in the resolution the bigger the file will be when you download it, and the longer it will take to process once you use it later on. If you consider you computer is not fast enough try downloading the 5m resolution instead.  Make sure the files cover the same spatial extent as the DTM.

## 8. Digital Terrain Model (DTM):

The DTM represents the bare ground surface without any above-ground features. It eliminates the heights of objects like buildings and trees, focusing solely on the natural topography of the terrain.

The AHN4 0.5 meter ground level grid (DTM) is intended as a ground level file, with all non-ground level objects (trees, buildings, bridges and other objects) removed from the point cloud. For the Netherlands, access the  Actueel Hoogtebestand Nederland 4  (AHN 4) data repository where the Digital Terrain Model (DTM)  files for your study area are available: 
https://www.arcgis.com/apps/Embed/index.html?appid=73433bc06f7640949f32e4f8e3842e7a 

Locate and download the DTM files for your desired study area in a suitable format. DTM is available at a scale resolution of 0.5m and 5m. Be careful, as the lower the number in the resolution the bigger the file will be when you download it, and the longer it will take to process once you use it later on. If you consider you computer is not fast enough try downloading the 5m resolution instead. Make sure the files you download cover the same spatial extent as the DSM .

## 9. Digital Elevation Model (DEM):

A Digital Elevation Model (DEM) is a digital representation of the Earth's surface, which provides information about the elevation or height of the terrain at different locations. It is a widely used dataset in various fields, including geospatial analysis, hydrology, and terrain visualization. By subtracting the DTM from the DSM, we obtain the DEM, which represents the bare ground elevation at each location. This process helps in removing the influence of above-ground features and isolating the terrain's natural elevation. 
So, now that you have collected the DSM and the DTM raster files, you will be able to use them pretty early in the data collecting phase. Here is a step-by-step guide on how to obtain a Digital Elevation Model (DEM) using the Digital Surface Model (DSM) and the Digital Terrain Model (DTM) in ArcGIS Pro using the Raster Calculator:

a.	Start ArcGIS Pro and open your project.

b.	If you haven’t done it already, add both the DSM and DTM rasters to your project by navigating to the "Catalog" pane, locating the folder containing the rasters, and dragging them into your map or right-clicking and selecting "Add to Current Map."

c.	Once the DSM and DTM rasters are added, navigate to the "Analysis" tab in the top menu and click on "Tools" to open the Geoprocessing pane.

d.	In the Geoprocessing pane, type "Raster Calculator" in the search box to locate the "Raster Calculator" tool. Click on it to open the tool.

e.	In the Raster Calculator tool, you'll see two input boxes. In the first input box, enter the DSM raster name or drag and drop it from the "Catalog" pane. 

f.	In the second input box, enter the DTM raster name or drag and drop it from the "Catalog" pane.

g.	To perform the calculation, subtract the DTM from the DSM. You can do this by typing the following expression in the Raster Calculator tool:  DSM - DTM

h.	Choose a destination folder and specify a name for the output raster. You can do this by clicking on the "Browse" button next to the "Output raster" parameter and navigating to the desired location.

i.	Click on the "Run" button to execute the Raster Calculator tool.

j.	Once the tool completes, the resulting DEM raster will be saved in the specified output location. You can add this DEM raster to your map by dragging and dropping it from the "Catalog" pane or by right-clicking on the map and selecting "Add Data."

### [![Next]](SolarAngle.md)

<!---------------------------------------------------------------------------->

[Next]: https://img.shields.io/badge/Next-37a779?style=for-the-badge