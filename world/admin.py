from django.contrib.gis import admin
from .models import WorldBorder, UserLocation

admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(UserLocation)
