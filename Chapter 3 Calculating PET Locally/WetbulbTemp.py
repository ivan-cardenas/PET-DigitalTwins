import arcpy
from math import atan

# Get input parameters
HR = float(arcpy.GetParameterAsText(0))  # Heat Index Relative Humidity
Temp = float(arcpy.GetParameterAsText(1))  # Temperature
out = arcpy.GetParameterAsText(2)  # Output parameter

# Calculate Wet Bulb Temperature (WB)
WB = Temp * (atan(0.151977 * ((HR + 8.313659) ** 0.5))) + (atan(Temp + HR) - atan(HR - 1.676331)) + (0.00391838 * (HR ** (3 / 2)) * atan(0.023101 * HR)) - 4.686035

# Set the output parameter
arcpy.SetParameter(2, WB)
