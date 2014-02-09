import sys

from django.conf import settings
from django.conf.urls import patterns, url, include

import dj_database_url


# test url patterns
urlpatterns = patterns('',
    url('', include('tx_lege_districts.urls',
            namespace='tx_lege_districts')),
)


settings.configure(
        DEBUG=False,
        DATABASES={'default': dj_database_url.config()},
        INSTALLED_APPS=('tx_lege_districts',),
        ROOT_URLCONF=__name__,
        )

from django.test.utils import get_runner


def run_tests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['tx_lege_districts'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    run_tests()
