import json
from django.http.response import HttpResponse
from .models import UserLocation


def data(request):
    if request.method == 'POST':
        # get current user
        user = request.user

        # get json data from header
        jsonData = request.POST.get('data', None)
        data = json.loads(jsonData)
        lat = data['latitude']
        lng = data['longtitude']

        # add location to database
        userLocation = UserLocation()
        if lat and lng and user:
            userLocation.username = user
            userLocation.lat = lat
            userLocation.lng = lng
            userLocation.save()

        print(userLocation)

        return HttpResponse(200)
