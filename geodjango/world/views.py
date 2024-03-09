from django.shortcuts import render
from .models import Settlement

def mapbox_map_view(request):
    settlements = Settlement.objects.all()
    return render(request, 'mapbox_map.html', {'settlements': settlements})