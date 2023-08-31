## 5. Water Bodies
In our case, we got some water plains and water streams data from the Municipality of Enschede, if you don’t have access to these specific files don’t worry, you can also generate your own. 

For this you can use an [overpass-turbo code](WaterBodies.sql) to obtain the Water Bodies OSM polygon shapefile inside the city of Enschede. 

This code is written in Overpass QL, which is used with the Overpass API for querying OpenStreetMap data. To run this code and obtain the result, you can use the Overpass Turbo web application.

 a.	Visit the Overpass Turbo website: https://overpass-turbo.eu/ 

b.	Copy the code into the text editor on the left side of the Overpass Turbo interface.

c.	You can choose to edit the geocodeArea to the name of the city you are interested in getting the data from. (In other words, this is how you change the city you want to search inside of).

d.	Click the "Run" button (or press Ctrl+Enter) to execute the query.

e.	The results will be displayed on the map on the right side of the interface, and a list of elements will be shown below the text editor.

To use the result as a layer in ArcGIS Pro, you can export the data from Overpass Turbo and import it into ArcGIS Pro using one of the following methods:


### Export as GeoJSON:
a.	In Overpass Turbo, click the "Export" button located above the map.
b.	Select "GeoJSON" as the export format.
c.	Save the GeoJSON file to your local drive.

### In ArcGIS Pro:
a.	Open ArcGIS Pro and create a new project or open an existing one.
b.	In the Catalog pane, navigate to the location where you saved the exported GeoJSON file.
c.	Right-click on the folder or geodatabase where you want to import the data and select "Import" > "File Geodatabase" or "Feature Class."
d.	Follow the prompts to import the GeoJSON file into ArcGIS Pro. 

---
Note: You can also try to generate a code that will let you get the trees inside of your city of choice with this method, try changing some of the parameters and explore what options make your workflow easier!

[![Next]](Buildings_DSM.md)

<!---------------------------------------------------------------------------->

[Next]: https://img.shields.io/badge/Next-37a779?style=for-the-badge