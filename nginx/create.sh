#!/bin/bash

#remove container
docker stop nginx 
docker rm nginx

# remove image
docker image rm nginx_gis

docker build -t nginx_gis .
echo "done building image"

echo "creating container"
docker volume rm v_nginx
docker create --name nginx \
--network geonet -t -p 8080:80 \
-v v_nginx:/usr/share/nginx/html nginx_gis

echo "starting..."
docker start nginx
