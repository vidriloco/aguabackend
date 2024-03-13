from django.shortcuts import render
from .models import Settlement
import datetime
from datetime import timedelta

def sources_map_view(request):
    return render(request, 'sources_map.html', { 'settlements': settlements() })

def disrupted_areas_view(request):
    return render(request, 'disrupted_areas.html', { 'settlements': settlements() })

def settlements():
    today = datetime.date.today()
    settlements = Settlement.objects.filter(day_measured=today)

    if not settlements:
        yesterday = today - timedelta(days=1)
        settlements = Settlement.objects.filter(day_measured=yesterday)
    return settlements