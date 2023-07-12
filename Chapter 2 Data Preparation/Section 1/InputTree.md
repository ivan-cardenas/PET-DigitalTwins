## 12. Input Tree (for the “Stamp Trees tool”):

We will need to use a polygon that represents a single tree later in our PET calculation, this tree will be “cloned” or “stamped” whenever the user chooses to add new trees to the simulation of the study area. In order to prepare this shapefile before we start you can do the following:

a.	Open the Tree Point Layer: Start by opening the tree point layer that contains the tree locations in ArcGIS Pro. You can do this by adding the layer to your map document.

b.	Select a Tree Point: Using the selection tools in ArcGIS Pro, select the specific tree point that you want to work with. You can click on the tree point to select it


c.	Create a Buffer: Once the tree point is selected, you can create a buffer around it to represent the tree crown. To do this, go to the Geoprocessing pane and search for the "Buffer" tool. Select the tool and provide the tree point layer as the input. Set the buffer distance to half the diameter of the tree crown you want to represent (e.g., 4.5 meters for a 9-meter diameter). Run the tool to create the buffer.

d.	Clip the DSM Raster: With the buffer created, you can now clip the DEM (Digital Elevation Model) raster to extract the portion that corresponds to the tree crown. In the Geoprocessing pane, search for the "Clip Raster" tool. Provide the DSM raster as the input and the buffer as the clip feature. Run the tool to obtain the clipped raster.

e.	Convert Pixel Values to Polygon: Now that you have the clipped raster, you can convert the pixel values (which represent height) to a polygon. In the Geoprocessing pane, search for the "Raster to Polygon" tool. Provide the clipped raster as the input and specify the field that contains the pixel values representing height. Run the tool to convert the raster to a polygon.


f.	Save the Polygon: After converting the raster to a polygon, you can save the resulting polygon feature class to a desired location. Specify the name and location for the output feature class, and save it.

By following these steps, you selected a tree point, created a buffer to represent the tree crown, clipped a DEM raster using the buffer, and converted the pixel values to a polygon feature class. This process allows you to obtain a polygon representing the tree crown based on the selected tree point.

Note: Remember, data availability may vary depending on your study area and the specific requirements of your project. Now that we know where to find data, let's move on to project preparation.
