from django.shortcuts import render
from .models import Settlement

def sources_map_view(request):
    settlements = Settlement.objects.all()
    return render(request, 'sources_map.html', {'settlements': settlements})

def disrupted_areas_view(request):
    settlements = Settlement.objects.all()
    return render(request, 'disrupted_areas.html', {'settlements': settlements})