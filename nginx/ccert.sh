#!/bin/bash

#remove container
docker stop nginx_cert
docker rm nginx_cert

# remove image
docker image rm nginx_gis_cert

docker build -t nginx_gis_cert .
echo "done building image"

echo "creating container"
docker create --name nginx_cert --network geonet --network-alias wmap-nginx-certbot \
-p 20080:80 -p 20443:443 -t \
-v wmap_web_data:/usr/share/nginx/html \
-v $HOME/nginx_gis_cert/conf:/etc/nginx/conf.d \
-v /etc/letsencrypt:/etc/letsencrypt \
-v /var/www/certbot \
-v html_data:/usr/share/nginx/html/static \
nginx_gis_cert


echo "starting..."
docker start nginx
