import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from .models import District
from .constants import HOUSE, SENATE


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
            coordinates = json.loads(district.geometry.geojson)['coordinates']
            data[type.lower()] = {
                    'name': unicode(district).encode('utf-8'),
                    'number': district.number,
                    'coordinates': coordinates
                }
        except District.DoesNotExist:
            pass

    return HttpResponse(json.dumps(data), mimetype='application/json')


def map(request):
    return render_to_response('districts/includes/map.html', {
            'lookup_url': reverse('districts_lookup')
        })
