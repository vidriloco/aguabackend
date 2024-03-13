from django.contrib import admin
from django.urls import path
from world import api
from world.views import sources_map_view
from world.views import disrupted_areas_view
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda req: redirect('/colonias-afectadas')),
    path('admin/', admin.site.urls),
    path('settlements', api.settlements),
    path('fuentes-de-abastecimiento', sources_map_view, name='sources_map'),
    path('colonias-afectadas', disrupted_areas_view, name='disrupted_areas')
]