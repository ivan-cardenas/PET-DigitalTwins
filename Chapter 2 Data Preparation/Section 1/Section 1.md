# Section 1: Exploring Data Sources

To calculate PET accurately, we need reliable data on temperature, humidity, and land cover. Luckily, there are various sources available that provide such information. According to the proposed method by (Koopmans et al.) the warmest day of the past five years should be considered to gather all the necessary data. 

After doing some research in the area of Enschede it was determined that the warmest day was July 27, 2019. Here's an overview of some commonly used data sources:
##	1. Meteorological Stations: 

Local weather stations provide temperature and humidity data. You can usually obtain this data from meteorological agencies or research institutions. Make sure to gather data for the desired study period and location.

 a.	In the Netherlands the Dutch Weather data from KNMI is available and accessible online as an open source data.

   b.	Knmy is a Python package for downloading and processing weather data from the automated weather stations of the Dutch Meteorological Institute (KNMI). Documentation of the used API can be found here (only in Dutch). https://knmy.readthedocs.io/en/latest/

   c.	For a list of the available selectable parameters and weather stations in the Netherlands to be used in the knmy wrapper you can also visit https://daggegevens.knmi.nl/.

d.	The closest Station in Enschede is the number 290: Twente.

e.	In order to find the warmest value of the day, we need to specify that we will obtain the values by hour (‘hourly’) and a range within the selected day. 

f.	Values like Temperature, Humidity, Solar Radiation were obtained using [this method](Meteorological.py).

## 2.	Remote Sensing Data: 
Satellite imagery can provide valuable information about land cover, including vegetation and impervious surfaces. Services like NASA Earth Observing System Data and Information System (EOSDIS) provide access to satellite data products.

a.	The NDVI raster was obtained using a google earth engine code for the area of the city of Enschede.

b.	After identifying the date with the highest temperature in the last 5 years, we will obtain the median NDVI values for the months where the highest temperature was recorded.

c.	In the website https://earthengine.google.com/ you can access the Google Earth Engine editor by clicking the Platform button on the top of the site and clicking on Code Editor.

d.	 Log-in with a compatible account (any google account can be used).

e.	Paste the [following code](NDVI.js) in the editor.

f.	Add a polygon geometry on the map that contains the area that you want to obtain the NDVI from by selecting the rectangular geometry tool .

![Alt text](image.png)

g.	The default name of this area will be called ‘geometry’, use this name and replace it instead of the text “path to asset” (the name geometry goes without any additional ‘ or “).

h.	Execute the code by clicking the ‘Run’ button on the top menu of the editor.

i.	This will generate a new tasks in the ‘Tasks’ tab beside the editor. This task will be named NDVI, when you press it, it will prompt you to provide basic information to generate the NDVI and the storage location.

j.	Fill in the CRS (Coordinate Reference System) in which you want the output to be generated (in our case as we were working in The Netherlands, we choose EPSG:28992).

k.	Save the file as a Geo_TIFF in order to retain the coordinate system data.

---
Now you have your own NDVI for your study area!

## 3.	Open Data Portals: 
Many governmental and environmental organizations offer open data portals with a wide range of spatial datasets. These portals often contain relevant data, such as land cover maps or climate information.

[![Continue]](Trees.md)

<!---------------------------------------------------------------------------->

[Continue]: https://img.shields.io/badge/Continue-37a779?style=for-the-badge