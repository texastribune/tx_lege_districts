import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from .models import District


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

    for district in District.objects.filter_by_lat_lng(lat, lng):
        geojson = district.geometry.simplify(0.0001).geojson
        coordinates = json.loads(geojson)['coordinates']
        data[district.type.lower()] = {
            'name': unicode(district).encode('utf-8'),
            'number': district.number,
            'coordinates': coordinates,
            'year': district.year,
        }

    return HttpResponse(json.dumps(data), mimetype='application/json')


def by_number(request):
    """
    Returns a list of districts for the given type and numbers
    """
    district_type = request.GET.get('type')
    try:
        numbers = [int(n) for n in request.GET.getlist('number')]
    except ValueError:
        numbers = []
    if not (district_type and numbers):
        return HttpResponse('bad request', status=402)

    districts = District.objects.filter(type__iexact=district_type)
    if numbers:
        districts = districts.filter(number__in=numbers)

    data = []
    for district in districts:
        geojson = district.geometry.simplify(0.0001).geojson
        coordinates = json.loads(geojson)['coordinates']
        data.append({
            'name': unicode(district).encode('utf-8'),
            'type': district.type.lower(),
            'number': district.number,
            'coordinates': coordinates,
            'year': district.year,
        })

    return HttpResponse(json.dumps(data), mimetype='application/json')


def map(request):
    return render_to_response('districts/includes/map.html', {
            'lookup_url': reverse('tx_lege_districts:lookup')
        })


def district_detail(request, type, number):
    """
    Returns a geojson representation of a district.

    /house/15/
    /senate/3/

    TODO: support jsonp
    TODO: support year lookup

    If we do multi-district lookups (in a list view), it should return a feature
    object with meta in the "features" property.
    See: http://geojson.org/geojson-spec.html#feature-objects
    """
    simplify = 0.001  # WISHLIST make this a get parameter
    district = get_object_or_404(District,
        type__iexact=type,
        number=number,
    )
    data = district.geometry.simplify(simplify).geojson
    return HttpResponse(data, mimetype='application/json')
