## 10. Solar Angle

[This code]() has to be added into ArcGIS PRO as a toolbox that will accept inputs. This inputs will let the code work and you will have a nice tool to load every time you need to obtain this value. This tool will also be useful later as it will be possible to add it into a model builder when we use all the values to calculate the PET.

Arcpy code to be loaded in a compatible environment like in an ArcGIS PRO toolbox. Here is how to add the code to a toolbox in ArcGIS Pro and configure the necessary parameters:

a.	Open ArcGIS Pro and create a new project or open an existing one.

b.	In the Catalog pane, right-click on "Toolboxes" and select "Add Toolbox". Give the toolbox a name and save it in a desired location.

c.	Right-click on the newly created toolbox and select "Add Script".

d.	In the "Add Script" window, provide a name for the script and select the Python script file containing the code you provided.

e.	Click "Next" to proceed to the "Script Properties" window.

f.	In the "Script Properties" window, you can configure various settings for the script:

*	**Label**: Provide a label for the script.
*	**Description**: Enter a description that explains the functionality of the script.
*	**Script File**: Specify the path to the Python script file containing the code.
*	**Toolbox Alias**: Optionally, you can provide an alias for the toolbox.

g.	In the "Parameters" tab, you can add the necessary input parameters:

*	Click on the "Add" button to add a new parameter.
*	Specify a name for the parameter.
*	Choose the appropriate data type for the parameter (e.g., Date, Double, String).
*	Optionally, you can provide a label, direction, and default value for the parameter.
*	Repeat these steps to add all the required parameters (`when_full`, `latitude`, `longitude`, `solar_angle`).

h.	After adding the parameters, you can configure additional settings as needed, such as parameter validation, dependency between parameters, and tooltips.

i.	Click "Finish" to add the script to the toolbox.

j.	You can now find the script tool under the toolbox in the Catalog pane. Double-click on the script tool to open the tool dialog.

k.	In the tool dialog, you can enter values for the input parameters (`when_full`, `latitude`, `longitude`, `solar_angle`).

l.	Click "Run" to execute the script with the provided input values.

[Next](Wind%20Speed.md)