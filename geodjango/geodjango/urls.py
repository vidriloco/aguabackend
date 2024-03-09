from django.contrib import admin
from django.urls import path
from world import api
from world.views import mapbox_map_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('settlements', api.settlements),
    path('mapbox-map', mapbox_map_view, name='mapbox_map_view')
]