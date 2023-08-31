### CALCULATE THE PET: 
If you have reached this point, you must be very familiar with all the different tools and codes we have used so far. You surely have collected several values in your ModelBuilder. Just to be sure you are in the right path, double check you have obtained the following:

*	Bowen Ratio
*	Sky View Factor
*	Solar Angle
*	Wet Bulb

If you have, then you are ready for the last steps towards building your own PET calculation tool. For this part we will need to add some values directly to the ModelBuilder and use them to calculate directly in the PET equation as follows:

##### Step 1. Add a Solar Irradiation value in W/m2: 
We could easily add this value directly into the equation of the PET analysis but that wouldn’t let us change it if we want to check a different city, day or year. Therefore if we want that value to be editable later on it is better for us to add the value in the following way:

Go to the “insert” ribbon in the ModelBuilder tab, select the variable button. You will see a small window appear called Variable Data Type, that will let you choose from different preestablished data representations, be sure to look for the “Double” type in the dropdown list and press ok when you are fine with your selection. Be sure to make it a parameter.

##### Step 2. Add the default value to Solar Irradiation: 
If you want the PET tool to always load the same value as default you can easily stablish this by double clicking the recently added Solar Irradiation variable and typing the Solar Irradiation value that you found when you investigated the warmest day in your study area. Ours was 211.5072. 

##### Step 3. Add the Wind Speed raster:  
You can drag the Wind Speed raster that we obtained at the beginning of the guide and drop it in the ModelBuilder work area. Be sure to make it a parameter.

##### Step 4. Calculate the PET: 
Here is where all resultant rasters come together, with this we will Finally calculate our goal values in a raster that we can later use in analyses and understand which changes can affect the most a certain area in the city. In order to achieve this we need to use the Raster Calculator tool: 

1)	In the Model Builder window, locate the Toolbox pane on the left side. Scroll down and find the "Spatial Analyst Tools" toolbox.

2)	Expand the "Spatial Analyst Tools" toolbox and locate the "Map Algebra" toolset. Within this toolset, you'll find the "Raster Calculator" tool. 

3)	Drag and drop the "Raster Calculator" tool onto the canvas. It will appear as an icon representing the tool. 

4)	Connect Bowen Ratio, Sky View Factor, Solar Angle, Wet Bulb, Solar Irradiation, Wind Speed, the Temperature in C and the extent as inputs in the "Raster Calculator" tool. In this case our output will create a final PET.tif raster and will be the final result in our tool. This should be a parameter too.


5)	Double-click on the "Raster Calculator" tool to open its parameters. In the expression field, try to replicate the following code with the name of your input files: 

```
-13.26+(1.25*float('%Temperature in C%'))+(0.011*float('%Solar Irradiation in W/m2%'))-(3.37* Ln("%Wind Speed at 1.2m%"))+(0.078* float('%WB%'))+(0.0055* float('%Solar Irradiation in W/m2%')*Ln("%Wind Speed at 1.2m%"))+(5.56*Sin(float('%Solar Angle%')))-(0.0103*float('%Solar Irradiation in W/m2%')*Ln("%Wind Speed at 1.2m%")*Sin(float('%Solar Angle%')))+(0.0546* "%BowenRatio%")+(1.94* "%SVF%")
```

The code calculates a value based on various input variables, remember the PET equation that we showed you at the beginning of the guide? We are replicating that one in this code. If you don’t remember the equation you can always find it in Section 2: Understanding the Science Behind PET It involves multiplication, addition, subtraction, and trigonometric functions. The input variables used in the expression include temperature, solar irradiation, wind speed, WB, solar angle, Bowen ratio, and SVF. Each variable is multiplied by a specific coefficient and combined with other terms to obtain the final result. The expression represents a mathematical model or formula that combines these variables to derive a calculated value.

**Note**: If the name of your files don’t match ours or you are scared of making a typo mistake, don’t worry you can also double click the raster you want to add in the “Rasters” window in the top left part of the Raster Calculator tool.

6)	Configure any additional parameters, such as the output raster name and the analysis extent should be applied to the tool as we did before.  

7)	Save your model and test it by pressing “Run” to execute the Raster Calculator tool. It will apply the provided code to perform the specified calculations on the input rasters.


#### [![Next]](Section%202-7.md)

<!---------------------------------------------------------------------------->

[Next]: https://img.shields.io/badge/Next-37a779?style=for-the-badge