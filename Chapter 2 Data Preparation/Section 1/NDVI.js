var City = ee.FeatureCollection("path to asset");

/**
* Function to mask clouds using the Sentinel-2 QA band
* @param {ee.Image} image Sentinel-2 image
* @return {ee.Image} cloud masked Sentinel-2 image
*/
function maskS2clouds(image) {
 var qa = image.select('QA60');

 // Bits 10 and 11 are clouds and cirrus, respectively.
 var cloudBitMask = 1 << 10;
 var cirrusBitMask = 1 << 11;

 // Both flags should be set to zero, indicating clear conditions.
 var mask = qa.bitwiseAnd(cloudBitMask).eq(0)
     .and(qa.bitwiseAnd(cirrusBitMask).eq(0));

 return image.updateMask(mask).divide(10000);
}

var dataset = ee.ImageCollection('COPERNICUS/S2_SR')
                 .filterBounds(City)
                 //.filter(ee.Filter.contains('.geo', geometry))
                 .filterDate('2019-07-01', '2019-08-31')
                 // Pre-filter to get less cloudy granules.
                 .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',10))
                 .map(maskS2clouds)
                 //.sort('CLOUD_COVER')
                 //.first();
                 

print (dataset)
var median = dataset.median().clip(City)

var nir = median.select('B8');
var red = median.select('B4');
//var ndvi = nir.subtract(red).divide(nir.add(red)).rename('NDVI');
var ndvi = median.normalizedDifference(['B8' , 'B4']);

var projection = median.select('B2').projection().getInfo()
print(projection)

Map.centerObject("path to asset", 12);

var ndviParams = {min: -1, max: 1, palette: ['Darkblue', 'white', 'Darkgreen']};
Map.addLayer(ndvi, ndviParams, "NDVI layer");

//Change Projection


Export.image.toDrive({
 image: ndvi,
 description: 'NDVI',
 crs: 'EPSG:28992',
 scale: 10,
 region: City,
 fileFormat: 'GeoTIFF',
 formatOptions: {
   cloudOptimized: true
 }
});
