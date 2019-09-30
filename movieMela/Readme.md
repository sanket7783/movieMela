### Django Rest API ###

1. To make get call to get the list of movies using curl
curl -X GET --user username:password http://endpoint_url

2. To make get call to get details of a movie

curl -X GET --user username:password http://endpoint_url/pk_id

3. To search a movie based on its name or genre using curl

curl -X GET --user username:password http://endpoint_url/?search=name_of _movie

4. To post a movie data

curl -X POST --user username:password -d {payload} http://endpoint_url



