from django.contrib import admin
from django.urls import path
from world import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('settlements', api.settlements)
]