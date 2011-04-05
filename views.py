import json

from django.http import Http404, HttpResponse

from .models import District
from .models import HOUSE, SENATE

def lookup(request):
    """
    Returns a JSON-encoded view of the districts for the given lat/long
    """
    data = {}
    try:
        lat = float(request.GET.get('lat'))
        lng = float(request.GET.get('lng'))
    except (TypeError, ValueError):
        return HttpResponse(json.dumps(data), mimetype='application/json')

    districts = District.objects.filter_by_lat_lng(lat, lng)
    for type in (HOUSE, SENATE):
        try:
            district = districts.get(type=type)
            data[type.lower()] = {
                    'number': district.number, 
                    'geometry': district.geometry.json }
        except District.DoesNotExist:
            pass
    
    return HttpResponse(json.dumps(data), mimetype='application/json')
