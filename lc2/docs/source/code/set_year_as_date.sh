#! /bin/bash

curl -XPUT -H "Content-Type: application/json" "http://elastic:9200/music" -d'
{
   "mappings": {
      "_doc": {
         "properties": {
             "year": {
                 "type": "date",
                 "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd||yyyy"
             }
         }
      }
   }
}'

