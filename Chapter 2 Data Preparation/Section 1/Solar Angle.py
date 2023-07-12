from math import degrees, cos, sin, radians, asin, pi
from math import acos, atan, asin, atan2, exp, e
 
current_mod = 'math'
 
import arcpy
from datetime import datetime
 
earth_radius = 6378140.0  # meters
earth_axis_inclination = 23.45  # degrees
seconds_per_day = 86400
 
when_full = arcpy.GetParameterAsText(0)
latitude = float(arcpy.GetParameterAsText(1))
longitude = float(arcpy.GetParameterAsText(2))
solar_angle = arcpy.GetParameterAsText(3)
 
date_obj = datetime.strptime(when_full, "%d/%m/%Y %H:%M:%S")  # Convert string to datetime object
 
tm_yday = date_obj.timetuple().tm_yday  # Get the day of year from th datetime object
tm_hour = date_obj.timetuple().tm_hour
tm_min = date_obj.timetuple().tm_min


 
def equation_of_time(day):
    "returns the number of minutes to add to mean solar time to get actual solar time."
    b = 2 * pi / 364.0 * (day - 81)
    return 9.87 * sin(2 * b) - 7.53 * cos(b) - 1.5 * sin(b)
 
def get_solar_time(longitude_deg):
    "returns solar time in hours for the specified longitude and time," \
    " accurate only to the nearest minute."
    return \
        (
            (tm_hour * 60 + tm_min + 4 * longitude_deg + equation_of_time(tm_yday))
        /
            60
        )
 
def get_hour_angle(longitude_deg):
    solar_time = get_solar_time(longitude_deg)
    return 15.0 * (solar_time - 12.0)
 
def get_declination(day):
    '''The declination of the sun is the angle between
    Earth's equatorial plane and a line between the Earth and the sun.
    The declination of the sun varies between 23.45 degrees and -23.45 degrees,
    hitting zero on the equinoxes and peaking on the solstices.
    '''
    return earth_axis_inclination * sin((2 * pi / 365.0) * (day - 81))
 
def get_altitude_fast(latitude_deg, longitude_deg, when):
# expect 19 degrees for solar.get_altitude(42.364908,-71.112828,datetime.datetime(2007, 2, 18, 20, 13, 1, 130320))
    day = tm_yday
    declination_rad = radians(get_declination(day))
    latitude_rad = radians(latitude_deg)
    hour_angle = get_hour_angle(longitude_deg)
    first_term = cos(latitude_rad) * cos(declination_rad) * cos(radians(hour_angle))
    second_term = sin(latitude_rad) * sin(declination_rad)
  
    return degrees(asin(first_term + second_term))
 
altitude = get_altitude_fast(latitude,longitude,when_full)
 
arcpy.SetParameter(3, altitude)
