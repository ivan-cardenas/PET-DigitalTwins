import arcpy # necessary library to run all geoprocessing tools in ArcGIS

arcpy.env.overwriteOutput=True #When set to True tools will execute and overwrite any existing output
# Define input and output paths
input_point_fc = arcpy.GetParameterAsText(0) #Will obtain the first parameter as the point feature containing the new trees
input_poly_fc = arcpy.GetParameterAsText(1) #Will obtain the second parameter as the base polygon feature to stamp

output_file_name = arcpy.GetParameterAsText(2) #Will use this parameter as the name of the finalized stamped trees file

# Create output feature class with same CRS as input point layer
output_crs = arcpy.Describe(input_point_fc).spatialReference
output_fc = arcpy.management.CreateFeatureclass('in_memory', 'Stamped_Trees', "POLYGON", spatial_reference=output_crs)

# Add fields to the output feature class
arcpy.management.AddField(output_fc, "Height", "DOUBLE")

# Create an InsertCursor to insert polygons into the output feature class
with arcpy.da.InsertCursor(output_fc, ["SHAPE@", "Height"]) as cursor:

    # Loop through each point feature in the input point layer
    poly_count = 0
    with arcpy.da.SearchCursor(input_point_fc, ["SHAPE@XY"]) as point_cursor:
        for point_row in point_cursor:
            point_xy = point_row[0]

            # Get all polygons (representing the pixels) from the input polygon layer 
            polygons = []
            with arcpy.da.SearchCursor(input_poly_fc, ["SHAPE@", "Height"]) as poly_cursor:
                for poly_row in poly_cursor:
                    polygons.append(poly_row)

            # Combine the polygons into a single geometry object
            poly_array = arcpy.Array()
            for poly in polygons:
                poly_array.add(poly[0].getPart(0))
            combined_polygons = arcpy.Polygon(poly_array, output_crs)

            # Calculate the distance between the point and the centroid of the combined polygons
            centroid = combined_polygons.centroid
            distance_x = point_xy[0] - centroid.X
            distance_y = point_xy[1] - centroid.Y

            # Loop through each polygon and insert it into the output feature class (to combine all the polygons in a single layer)
            for poly in polygons:
                poly_geom = poly[0]
                height = poly[1]

                # Check if the height attribute is present in the input data (to avoid errors on some files not having it)
                if height is not None:
                    # Move the polygon based on the distance between the point and the centroid of the combined polygons
                    new_poly_geom = arcpy.Polygon(arcpy.Array([arcpy.Point(pt.X + distance_x, pt.Y + distance_y) for pt in poly_geom.getPart(0)]), output_crs)

                    # Insert the new polygon into the output feature class
                    cursor.insertRow([new_poly_geom, height])

                    # Increment the polygon count
                    poly_count += 1

                else:
                    # Skip this polygon if the height attribute is not present
                    continue

    # Print number of polygons created
    print("Created {} polygons".format(poly_count))

    # Clean up
    # arcpy.management.Delete("point_layer")
    Stamped = output_fc
    arcpy.SetParameter(2, Stamped) #returns the resulting Stamped as the resulting feature class
