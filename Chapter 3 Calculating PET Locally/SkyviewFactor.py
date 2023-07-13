import arcpy
import numpy as np

# Specify the path to the DEM raster
dem_raster = arcpy.GetParameterAsText(0)
output_path= arcpy.GetParameterAsText(1)



# Get input Raster properties
inRas = arcpy.Raster(dem_raster)
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth
crs= arcpy.Describe(inRas).spatialReference

arcpy.env.overwriteOutput=True

# Convert the DEM raster to a NumPy array
height_arr = arcpy.RasterToNumPyArray(dem_raster)

def horizon_shift_vector(num_directions=16,
                         radius_pixels=10,
                         min_radius=1
                         ):
    """
    Calculates Sky-View determination movements.

    Parameters
    ----------
    num_directions : int
        Number of directions as input.
    radius_pixels : int
        Radius to consider in pixels (not in meters).
    min_radius : int
        Radius to start searching for horizon in pixels (not in meters).

    Returns
    -------
    shift : dict
        Dict with keys corresponding to the directions of search azimuths rounded to 1 decimal number
            - for each key, a subdict contains a key "shift":
                values for this key is a list of tuples prepared for np.roll - shift along lines and columns
            - the second key is "distance":
                values for this key is a list of search radius used for the computation of the elevation angle 
    """

    # Initialize the output dict
    shift = {}

    # Generate angles and corresponding normal shifts in X (columns)
    # and Y (lines) direction
    angles = (2 * np.pi / num_directions) * np.arange(num_directions)
    x = np.cos(angles)
    y = np.sin(angles)
    angles = np.round(np.degrees(angles), decimals=1)

    # Generate a range of radius values in pixels.
    # Make it finer for the selcted scaling.
    # By adding the last constant we make sure that we do not start with
    # point (0,0).
    scale = 3.
    radii = np.arange((radius_pixels - min_radius) * scale + 1) / scale + min_radius

    # For each direction compute all possible horizont point position
    # and round them to integers
    for i in range(num_directions):
        x_int = np.round(x[i] * radii, decimals=0)
        y_int = np.round(y[i] * radii, decimals=0)
        # consider only the minimal number of points
        # use the trick with set and complex nuber as the input
        coord_complex = set(x_int + 1j * y_int)
        # to sort proportional with increasing radius, 
        # set has to be converted to numpy array
        shift_pairs = np.array([(k.real, k.imag) for k in coord_complex]).astype(int)
        distance = np.sqrt(np.sum(shift_pairs ** 2, axis=1))
        sort_index = np.argsort(distance)
        # write for each direction shifts and corresponding distances
        shift[angles[i]] = {
            "shift": [(k[0], k[1]) for k in shift_pairs[sort_index]],
            "distance": distance[sort_index],
        }

    return shift

def sky_view_factor_compute(height_arr,
                            radius_max=10,
                            radius_min=1,
                            num_directions=16,
                            compute_svf=True,
                            compute_opns=False,
                            compute_asvf=False,
                            a_main_direction=315.,
                            a_poly_level=4,
                            a_min_weight=0.4,
                            no_data=None
                            ):
    """
    Calculates horizon based visualizations: Sky-view factor, Anisotopic SVF and Openess.

    Parameters
    ----------
    height_arr : numpy.ndarray
        Elevation (DEM) as 2D numpy array.
    radius_max : int
        Maximal search radius in pixels/cells (not in meters).
    radius_min : int
        Minimal search radius in pixels/cells (not in meters), for noise reduction.
    num_directions : int
        Number of directions as input.
    compute_svf : bool
        If true it computes and outputs svf.
    compute_asvf : bool
        If true it computes and outputs asvf.
    compute_opns : bool
        If true it computes and outputs opns.
    a_main_direction : int or float
        Main direction of anisotropy.
    a_poly_level : int
        Level of polynomial that determines the anisotropy.
    a_min_weight : int
        Weight to consider anisotropy:
                 0 - low anisotropy, 
                 1 - high  anisotropy (no illumination from the direction opposite the main direction)
    no_data : int or float
        Value that represents no_data, all pixels with this value are changed to np.nan .

    Returns
    -------
    dict_out : dictionary
        Return {"svf": svf_out, "asvf": asvf_out, "opns": opns_out};
        svf_out, skyview factor : 2D numpy array (numpy.ndarray) of skyview factor;
        asvf_out, anisotropic skyview factor : 2D numpy array (numpy.ndarray) of anisotropic skyview factor;
        opns_out, openness : 2D numpy array (numpy.ndarray) openness (elevation angle of horizon).
    """
    # change no_data to np.nan
    if no_data is not None:
        height_arr[height_arr == no_data] = np.nan

    # pad the array for the radius_max on all 4 sides
    height = np.pad(height_arr, radius_max, mode='symmetric')

    # compute the vector of movement and corresponding distances
    move = horizon_shift_vector(num_directions=num_directions, radius_pixels=radius_max, min_radius=radius_min)

    # init the output for usual SVF
    if compute_svf:
        svf_out = np.zeros(height.shape, dtype=np.float32)
    else:
        svf_out = None
    # init the output for azimuth dependent SVF
    if compute_asvf:
        asvf_out = np.zeros(height.shape, dtype=np.float32)
        w_m = a_min_weight
        w_a = np.deg2rad(a_main_direction)
        weight = np.arange(num_directions) * (2 * np.pi / num_directions)
        weight = (1 - w_m) * (np.cos((weight - w_a) / 2)) ** a_poly_level + w_m
    else:
        asvf_out = None
    # init the output for Openess
    if compute_opns:
        opns_out = np.zeros(height.shape, dtype=np.float32)
    else:
        opns_out = None

        # search for horizon in each direction...
    for i_dir, direction in enumerate(move):
        # reset maximum at each iteration (direction)
        max_slope = np.zeros(height.shape, dtype=np.float32) - 1000

        # ... and to the search radius
        for i_rad, radius in enumerate(move[direction]["distance"]):
            # get shift index from move dictionary
            shift_indx = move[direction]["shift"][i_rad]
            # estimate the slope
            _ = (np.roll(height, shift_indx, axis=(0, 1)) - height) / radius
            # compare to the previus max slope and keep the larges
            max_slope = np.maximum(max_slope, _)

        # convert to angle in radians and compute directional output
        _ = np.arctan(max_slope)
        if compute_svf:
            svf_out = svf_out + (1 - np.sin(np.maximum(_, 0)))
        if compute_asvf:
            asvf_out = asvf_out + (1 - np.sin(np.maximum(_, 0))) * weight[i_dir]
        if compute_opns:
            opns_out = opns_out + _

    # cut to original extent and 
    # average the directional output over all directions
    if compute_svf:
        svf_out = svf_out[radius_max:-radius_max, radius_max:-radius_max] / num_directions
    if compute_asvf:
        asvf_out = asvf_out[radius_max:-radius_max, radius_max:-radius_max] / np.sum(weight)
    if compute_opns:
        opns_out = np.rad2deg(0.5 * np.pi - (opns_out[radius_max:-radius_max, radius_max:-radius_max] / num_directions))

    # return results within dict
    dict_svf_asvf_opns = {"svf": svf_out, "asvf": asvf_out, "opns": opns_out}
    dict_svf_asvf_opns = {k: v for k, v in dict_svf_asvf_opns.items() if v is not None}  # filter out none

    return dict_svf_asvf_opns["svf"]

svf=sky_view_factor_compute(height_arr,
                            radius_max=10,
                            radius_min=1,
                            num_directions=16,
                            compute_svf=True,
                            compute_opns=False,
                            compute_asvf=False,
                            a_main_direction=315.,
                            a_poly_level=4,
                            a_min_weight=0.4,
                            no_data=None
                            )

# Convert array to a geodatabase raster
myRaster = arcpy.NumPyArrayToRaster(svf,lowerLeft,cellSize)
myRaster= arcpy.Raster(arcpy.management.DefineProjection(myRaster, crs))
# Set the output parameter
myRaster.save(output_path)
#myRaster.save(outname)
arcpy.SetParameter(1, output_path)
