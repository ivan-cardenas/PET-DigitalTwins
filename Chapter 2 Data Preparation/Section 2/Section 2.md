# Section 2: Setting Up Your Project

To begin the PET calculation process in ArcGIS Pro, we need to set up our project properly. Here are the essential steps:
## 1.	Create a New Project: 
Open ArcGIS Pro and create a new project. Give it a meaningful name and specify the desired location to save your project files. This ensures that all your work is organized and easily accessible.

## 2.	Set the Coordinate System: 
A coordinate system defines the spatial reference of your data. It ensures that the different layers align correctly in your project. If you're unsure about the coordinate system to use, check the metadata of your data sources or consult any guidelines provided by the data provider. In our case with the information from The Netherlands we used the Amersfoort / RD New (EPSG:28992) Coordinate System.

To set the coordinate system to Amersfoort / RD New (EPSG:28992) in ArcGIS Pro, follow these steps:

a.	Open your ArcGIS Pro project or create a new one.

b.	In the Catalog pane, navigate to the desired map or dataset that you want to assign the coordinate system to.

c.	Right-click on the map or dataset and select "Properties" from the context menu.

d.	In the "Layer Properties" dialog box, go to the "Coordinate System" tab.

e.	Click on the "Select" button next to the "Spatial Reference" field.

f.	In the "Spatial Reference Properties" dialog box, select "Projected Coordinate Systems" from the left panel.

g.	Expand the "National Grids" folder.

h.	Within the "National Grids" folder, scroll down and locate "RD New (EPSG:28992)".

i.	Select "RD New (EPSG:28992)" and click "OK".

j.	Back in the "Layer Properties" dialog box, you should see "Amersfoort / RD New" selected as the coordinate system.

k.	Click "OK" to apply the changes and close the dialog box.

The coordinate system of the selected map or dataset should now be set to Amersfoort / RD New (EPSG:28992) in your ArcGIS Pro project.

## 3.	Add Data: 
Add the necessary data layers to your project. This includes temperature and humidity data, as well as any DSM, DTM files you have obtained. To add data, click on the "Add Data" button in the ArcGIS Pro ribbon and navigate to the location where your data is stored.

## 4.	Examine Data Attributes: 
Once you've added the data, it's essential to examine the attribute tables associated with each layer. These tables contain valuable information about the variables and their corresponding values. Understanding the data's attributes helps you ensure the accuracy of your calculations.

---

With your project set-up and data in place, you're now ready to embark on the exciting journey of PET calculation. In Chapter 3, we'll delve into the specifics of using geoprocessing tools to calculate PET in ArcGIS Pro. Buckle up and get ready to unleash the power of spatial analysis in the realm of thermal comfort!
 
#### [Next Chapter](/Chapter%203%20Calculating%20PET%20Locally/Section%201.md)