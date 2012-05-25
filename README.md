# Texas Legislative Districts

A reusable Django app for working with Texas legislative districts.


### Usage

Add `tx_lege_districts` to your `INSTALLED_APPS`. Then configure a GIS-enabled database and load the districts you want from a fixture:

    python manage.py loaddata districts_2012
    python manage.py loaddata districts_2006
