from django.http import JsonResponse
from world.models import Settlement
from django.contrib.gis.db.models.functions import Centroid

def settlements(request):
    min_lon = request.GET.get('min_lon')
    min_lat = request.GET.get('min_lat')
    max_lon = request.GET.get('max_lon')
    max_lat = request.GET.get('max_lat')
    
    #agebs = Ageb.findAllAgebsWithinViewport(min_lon, min_lat, max_lon, max_lat)
    return JsonResponse({ 'agebs': serialize_ageb_records([]) }, status=200)

def serialize_ageb_records(records):
    return [{  } for record in records]