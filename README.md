# Texas Legislative Districts

A reusable Django app for working with Texas legislative districts.


### Usage

Add `tx_lege_districts` to your `INSTALLED_APPS`. Then configure a GIS-enabled database and load the districts you want from a fixture:

    python manage.py loaddata districts_2006


### Representatives

Districts provide a `representative` property that is `None` by default.

The representative can be handled in your own project using a a configurable backend:

    # myapp/backends.py
    class MyBackend(object):
        def get_representative(self, district):
            return MyRepresentativeModel.objects.get_for_district(district)

    # settings.py
    TX_REPRESENTATIVE_BACKENDS = ['myapp.backends.MyBackend']
