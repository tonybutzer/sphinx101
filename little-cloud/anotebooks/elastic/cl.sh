#! /bin/bash -x
echo hello
echo hi there
curl --header "Content-Type: application/json" -X$1 elastic:9200$2 | python -m json.tool
