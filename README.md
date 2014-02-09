# Texas Legislative Districts

A reusable Django app for working with Texas legislative districts.


### Usage

Add `tx_lege_districts` to your `INSTALLED_APPS`. Then configure a GIS-enabled
database and load the districts you want from a fixture:

    python manage.py loaddata districts_2006

Hookup the urls in the `tx_lege_districts` [namespace]:

    urlpatterns = patterns('',
        url('^lege\-districts/', include('tx_lege_districts.urls',
                namespace='tx_lege_districts')),
    )

[namespace]: https://docs.djangoproject.com/en/dev/topics/http/urls/#url-namespaces-and-included-urlconfs


### Representatives

Districts provide a `representative` property that is `None` by default.

The representative can be handled in your own project using a a configurable backend:

    # myapp/backends.py
    class MyBackend(object):
        def get_representative(self, district):
            return MyRepresentativeModel.objects.get_for_district(district)

    # settings.py
    TX_REPRESENTATIVE_BACKENDS = ['myapp.backends.MyBackend']


## Testing

Set the DATABASE_URL environment variable. Example:

    export DATABASE_URL=postgis:///tx_lege_districts

### Change template1 to be postgis enabled:

    psql template1

    CREATE EXTENSION postgis;
    CREATE EXTENSION postgis_topology;

Just use `DROP EXTENSION` if you want to go back.

### Run the test runner:

    python runtests.py
