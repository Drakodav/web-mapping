#### Dockerfile to generate a Docker image for nginx ­ to be used in a GeoDjango project
### Start from the official Nginx image
FROM nginx

WORKDIR '/nginx/'


RUN apt-get -y update && apt-get -y upgrade \
    && apt-get -y install software-properties-common certbot python-certbot-nginx
# Get rid of old default file and copy our config so that nginx can pick it up
RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.old

# COPY nginx.conf /etc/nginx/conf.d/
COPY headers.conf /etc/nginx/conf.d/
COPY server.conf /etc/nginx/conf.d/

# COPY ./static/ /usr/share/nginx/html/static/

EXPOSE 8080