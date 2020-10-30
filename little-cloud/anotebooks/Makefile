jup:
	(export CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; jupyter notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='yaml')

pipstuff:
	pip3 install osgeo
	# pip3 install cachetools
	# pip3 install xarray
	# pip3 install rasterio
	# pip3 install geojson
	# pip3 install elasticsearch
	# pip3 install folium
	# pip3 install geopandas
	# pip3 install scikit-image
	# pip3 install scikit-learn
	# pip3 install pandas

clear_db:
	(PGPASSWORD=localuser1234 psql -U dc_user datacube <dropTable.sql)

pandasfix:
	sudo pip3 install Cython 
	sudo apt-get update
	# sudo apt-get -y install gcc, g++
	sudo pip3 uninstall pandas
	sudo pip3 install pandas

netcdffix:
	sudo pip3 uninstall netCDF4
	sudo pip3 install netCDF4

numpyfix:
	sudo pip3 install --upgrade numpy

