# Section 1: Exploring Data Sources

To calculate PET accurately, we need reliable data on temperature, humidity, and land cover. Luckily, there are various sources available that provide such information. According to the proposed method by (Koopmans et al.) the warmest day of the past five years should be considered to gather all the necessary data. 

After doing some research in the area of Enschede it was determined that the warmest day was July 27, 2019. Here's an overview of some commonly used data sources:
##	Meteorological Stations: 

Local weather stations provide temperature and humidity data. You can usually obtain this data from meteorological agencies or research institutions. Make sure to gather data for the desired study period and location.

 a.	In the Netherlands the Dutch Weather data from KNMI is available and accessible online as an open source data.

   b.	Knmy is a Python package for downloading and processing weather data from the automated weather stations of the Dutch Meteorological Institute (KNMI). Documentation of the used API can be found here (only in Dutch). https://knmy.readthedocs.io/en/latest/

   c.	For a list of the available selectable parameters and weather stations in the Netherlands to be used in the knmy wrapper you can also visit https://daggegevens.knmi.nl/.

d.	The closest Station in Enschede is the number 290: Twente.

e.	In order to find the warmest value of the day, we need to specify that we will obtain the values by hour (‘hourly’) and a range within the selected day. 

f.	Values like Temperature, Humidity, Solar Radiation were obtained using [this method](Meteorological.py).


```
!pip install knmy

from datetime import datetime, timedelta
import pandas as pd
today = datetime.now()
yesterday = datetime.today() - timedelta(days=365)
today= today.strftime("%Y%m%d%H")
yesterday= yesterday.strftime("%Y%m%d%H")
print(yesterday)
print(today)

from knmy import knmy
disclaimer, stations, variables, data = knmy.get_knmi_data(type='hourly',stations=[290], start=2019072700, end= 2019072800,
                                                             inseason=False, variables=['SUNR'], parse=True)
print(stations)
print(variables)

pd.DataFrame(data)
