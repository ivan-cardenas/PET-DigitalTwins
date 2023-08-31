## 11. Wind Speed

In order to obtain this value, the preferred way would be to have some sensors around the city that are located at a proper height (the wind speed on top of buildings is not the same as the one at street level). As this data was not available neither in raster nor shapefile format at the moment we worked in the project, we had to use a simulation software in order to obtain an approximation on how the wind was behaving on the day of the warmest temperature in our study area. If you happen to have access this data from measuring sensors you can also opt to generate a raster through the interpolation of the sensors data (the interpolation process will be also shown in these steps).

WindNinja is a reliable simulation tool for wind that uses computational fluid dynamics (CFD) to model and predict wind flow patterns. It was developed by the Missoula Fire Sciences Laboratory, which is part of the Rocky Mountain Research Station, U.S. Forest Service.

WindNinja is trusted by researchers, scientists, and professionals in various fields, including wildfire management, emergency response planning, and wind energy assessment. It incorporates high-resolution terrain data, atmospheric boundary layer physics, and meteorological input to generate accurate wind simulations.

By considering factors such as topography, land cover, and weather conditions, WindNinja can estimate wind speed, direction, and turbulence at different heights above the ground. This information is valuable for assessing wind patterns, understanding airflow behaviour, and making informed decisions related to fire behaviour, smoke dispersion, air quality, and wind energy site selection.

WindNinja's credibility comes from its continuous development, rigorous testing, and validation against field measurements and other established wind models. Its open-source nature allows for community contributions and ongoing improvement, making it a trusted tool for wind modelling and analysis
Based on the values we got from the meteorological station for wind on the warmest day in Enschede,  we calculated the wind speed at 1.2m from the ground using a 100 azimuthal angle on a specific date (July 27, 2019), if you want to obtain your own value you can try the following steps:
	
### Step 1. Wind Speed (Point Shapefile):

1.	Download and install WindNinja:  This is a standalone open-source software that can be downloaded from the following website (https://www.firelab.org/project/windninja).

2.	Launch WindNinja: Launch the application after installing it.

3.	Import terrain data: You need to provide terrain data for the specific location you are interested in. You can import the terrain data in one of the following ways:

*	Load a digital elevation model (DEM) file: You can import a DEM file (e.g., in GeoTIFF format) that covers your study area. (This is the method we used).
*	Use online data sources: WindNinja allows you to fetch terrain data from online sources such as the National Elevation Dataset (NED) or the Shuttle Radar Topography Mission (SRTM).

4.	Set the date: In the WindNinja interface, navigate to the "Weather" or "Initialization" tab (depending on the version) and specify the desired date (July 27, 2019) as the simulation date.

5.	Define the desired output height: In WindNinja, you can set the output height to 1.2m to obtain the wind speed at that specific height and the speed should be set to m/s. This option is typically found in the “Wind Input" tab.


6.	Set the azimuthal angle: you can (and should) also define the azimuthal angle to simulate wind from a specific direction. In this case, set the azimuthal angle to the angle obtained from the meteorological station (for us it was 100 degrees angle) to obtain wind information from that direction. This is also done in the Wind Input tab.

7.	Configure the Output parameters: You can turn on the checkbox for the shapefile result. This will allow you to export the result as a .SHP file that you can load in any GIS software. You can use the mesh resolution to try to keep the data as compatible as possible. 


8.	Run the simulation: Once you have set all the desired parameters, you can go to the “Solve” tab, where you can indicate the folder where you want to save the resulting point feature (.SHP) and the amount of cores you want to use from your computer to process this task (more cores translate into faster calculation times, but this is limited to the hardware of your computer).

9.	In the same tab, initiate the simulation by clicking the "Solve" button. WindNinja will perform the calculations and generate the wind results for the specified date, output height, and azimuthal angle. (This could take a long time to process depending on your computer specs and the resolution of the DEM you used as an input. If it takes to long to process you can try generating a DEM with a resolution of 5m instead of 0.5m).

10.	Analyse the results: After the simulation completes, WindNinja will generate wind output files containing information such as wind speed, direction, and turbulence. We will use the wind speed attribute to generate our own interpolated wind speed raster.

### Step 2. Wind Speed (Raster):
In order to be able to use the wind speed properly in the PET calculation, we will need to convert the point shapefile to a raster. Here are the steps on how you can manage to achieve this:
		
a.	Loading Point Shapefile in ArcGIS:
*	Open ArcGIS and create a new project or open an existing one.

*	In the Catalog pane, navigate to the location where you have the output point shapefile.

*	Right-click on the folder where you want to add the shapefile and select "Import" -> "Feature Class (single)".

*	In the "Import Feature Class" dialog box, browse and select the point shapefile (.shp) generated by WindNinja.

*	Specify a name and location for the imported feature class, and click "OK" to import the shapefile.

b.	Performing Interpolation in ArcGIS:

*	With the point shapefile loaded, open the Geoprocessing pane by clicking on the "Analysis" tab and selecting "Tools".

*	In the Geoprocessing pane, search for the "IDW" (Inverse Distance Weighted) tool.

*	Double-click on the "IDW" tool to open the tool dialog.

*	Select the point shapefile you imported as the input feature class.

*	Choose an appropriate output raster location and specify the desired cell size, power, and search radius parameters according to your requirements.

*	Click "Run" to perform the IDW interpolation.

*	Once the interpolation is complete, ArcGIS will generate a raster layer with wind speed values based on the input points.

*	You can customize the symbology and further analyze the interpolated raster layer in ArcGIS as per your project needs.

---
Please note that the exact steps may vary slightly depending on the version of WindNinja and ArcGIS you are using. It's recommended to refer to the documentation or user guides of the respective software versions for more detailed instructions.

#### [![Next]](InputTree.md)

<!---------------------------------------------------------------------------->

[Next]: https://img.shields.io/badge/Next-37a779?style=for-the-badge