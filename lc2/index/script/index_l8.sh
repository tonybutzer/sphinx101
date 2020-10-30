#! /bin/bash

./dropDatabaseTables.sh

datacube product add ../product_definition/l8_rwanda.yaml  ## L8

datacube product list

echo "Now run the prepare script you have\'nt written yet"


