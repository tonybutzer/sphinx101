# Elastic Search

## Overview

- near real time
- distributed
- clusters and nodes
- index
    - collection of docs with similar characteristics
    - has a name
    - can have multiple indexes
        - ex. movies, earthquakes
- type - category inside index
- internet friendly format
- document = basic unit which can be indexed - expressed in JSON
- shards - break the problem across nodes
- replicas - copies of index for performance and reliability
- operations
    - search
- REST api - JSON/http
- conventions
    - multiple indices
        - comma seperated or wildcarding - url query string params
            - ignore unavailable, allow_no_indices, expand_wildcards
    - date math support in index name
        - need to create a jupyter example of date range searches
    - common options
        - Pretty Result, No Values, Human Readable Output, etc - need link here
        - Fuzziness, Enable Stack Traces
    - URL based Access Control
        - can make use of a proxy for access control
        - tony will probably ignore this initially

**APIs**

1. Document API
   - operation at the document level - huh?
   - CRUD operations via http PUT/GET
   - can use the kibana interface to test
   - music library example
2. Search API
    - search accross multiple indices
3. Aggregation API
    - sum, count, avg etc
4. Index APIs
5. Cluster APIs



## Prerequisites
**Tutorials**

[Getting started with Elasticsearch in Python](https://towardsdatascience.com/getting-started-with-elasticsearch-in-python-c3598e718380)

[Elasticsearch Tutorial | Getting Started with Elasticsearch](https://www.youtube.com/watch?v=1EnvkPf7t6Y)

[understanding-bulk-indexing-in-elasticsearch](https://qbox.io/blog/understanding-bulk-indexing-in-elasticsearch)

[down and dirty searching](https://www.youtube.com/watch?v=7FLXjgB0PQI)

[cheat sheet elastic](http://elasticsearch-cheatsheet.jolicode.com/)

[ElasticSearch Toolbox](https://chrome.google.com/webstore/detail/elasticsearch-toolbox/focdbmjgdonlpdknobfghplhmafpgfbp)


## Not totally schemaless

GET /music/_mapping/


## JSON

**Tutorials**


[Working With JSON Data in Python](https://realpython.com/python-json/)

## GeoJSON

## STAC

see odc-lcmap stac in depth

place practical cookbook stac here

## Labs

### Music Mp3s

[mp3-tagger](- https://pypi.org/project/mp3-tagger/)

- anotebooks/elastic/mp3-json.ipynb


### EarthQuake JSON

**fetching the data**

**pushing the json docs to elastic search**
