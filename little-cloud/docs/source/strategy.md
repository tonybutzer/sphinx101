# Strategy

## Strategy Items

### The Database Replace Problems

#### RUN Instructions

```bash

cd /opt/little-cloud/lib/dcindexLib/dcindexLib

python3 index_metadata_to_elastic_main.py


#verify with kibana - set the date range at least a year ago or you will get no records

kibana:5601

# run test queries

cd ./elasticQueries

grep creation_dt geoComboQuery.sh
./geoComboQuery.sh | python-m json.tool | grep red


```

#### Steps

1. Review ElasticSearch principles - and my examples - DONE!
2. in dcindex - send the jason docs to elastic elastic_index.py - DONE!
    - query the data from elastic and examine aggregates from pandas - DONE!
3. Look at GeoJson and Elastic synergies

[Getting Started with Geospatial Queries in Elasticsearch](https://blog.benjie.me/geospatial-queries-for-elasticsearch/)

#### Elastic Tasks

1. add scene_center as a point and then start to find ones near that center
    - add to mapping (schema)
    - add to flatten elastic

### Xarray

[XArray: the power of pandas for multidimensional arrays](https://www.youtube.com/watch?v=Dgr_d8iEWk4)


[MetPy Mondays #53 - XArray Basics](https://www.youtube.com/watch?v=_9j7Y1-lk-o)


### GeoJson

### Shapefiles and Heatmaps

#### shapely and geopandas

[Introduction to Geospatial Data Analysis with Python | SciPy 2018 Tutorial | Serge Rey](https://www.youtube.com/watch?v=kJXUUO5M4ok)

[Introduction to Geospatial Data Analysis with Python | SciPy 2018 Tutorial | Serge Rey](https://www.youtube.com/watch?v=kJXUUO5M4ok)

### ElasticSearch Geo

#### Queries are tough for me

[elasticsearch bodybuilder helper](https://github.com/danpaz/bodybuilder)

- several sample queries are documented in shell scripts in dcindexLib

## People

[developmentseed people link](https://github.com/orgs/sat-utils/people)

[every-programmer-should-know](https://github.com/scisco/every-programmer-should-know)

[stac spec fork](https://github.com/scisco/stac-spec)


## WBS

1. setup infrastructure
    - elastic virtual machine ubuntu
    - NFS for big data usb drive
2. Learn ElasticSearch
    - documented tutorial
3. Learn JSON - link here
4. Setup RWANDA data set
5. organize lib directory
    - COG and UNTAR software - document how to use
    - improve code base and test documentation
6. GDAL, rasterio, gippy library study
7. Development Seed Study
8. Radiant Earth Study

### The Footprint problem

1. practice displaying imagery overlayed on folium maps - done

2. write browse.py modeled after cog.py in noteLib


```bash
gdalwarp -of GTiff -t_srs EPSG:4326 LC08_L1TP_172061_20130410_20170505_01_T1.tif mercator.tif


gdal_translate mercator.tif mercator.jpg -of JPEG -outsize 10% 10% -scale

```

[get landsat contrast stretch dans here uses gdal](https://salsa.debian.org/debian-gis-team/dans-gdal-scripts)

#### Links

[est_image_overlay_gulf_stream](http://nbviewer.jupyter.org/github/ocefpaf/folium_notebooks/blob/master/test_image_overlay_gulf_stream.ipynb)

[/examples/ImageOverlay](http://nbviewer.jupyter.org/github/python-visualization/folium/blob/master/examples/ImageOverlay.ipynb)

[JuxtaposeJS two images with slider](https://juxtapose.knightlab.com/)

[animated python](https://www.youtube.com/watch?v=c7GoaIsPlLE)

2. 


## Research

1. gippy

[Getting Down and Dirty with ElasticSearch by Clinton Gormley](https://www.youtube.com/watch?v=7FLXjgB0PQI)


[Getting Started with Geospatial Queries in Elasticsearch](https://blog.benjie.me/geospatial-queries-for-elasticsearch/)
