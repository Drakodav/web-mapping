FROM python:3.8

# update and install gdal
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install libgdal-dev

# Make a working directory in the image and set it as working dir
RUN mkdir -p /user/src/app
WORKDIR /usr/src/app
# make sure that pip is installed and to date
RUN pip install --upgrade pip setuptools wheel

# Get the following libraries. We can install them "globally" on 
# the image as it will contain only our project
RUN apt-get -y install build-essential python-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

# Now copy this to the image and install everything in it.
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy this directory into image
COPY . /usr/src/app

# make sure static files are up to date and available 
RUN python manage.py collectstatic --no-input --link

# expose localhost 8001 on the image
EXPOSE 8001

# run uwsgi 
CMD [ "uwsgi", "--ini", "uwsgi.ini" ]
