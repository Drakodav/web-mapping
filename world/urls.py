
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from django.conf.urls import url
from django.urls import path, include
from . import views

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='GeoLad API')


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('data/', views.data, name='data'),

    # swagger
    url(r'^$', schema_view),

    #  rest urls
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
