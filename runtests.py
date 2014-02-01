import sys

from django.conf import settings

import dj_database_url


settings.configure(
        DEBUG=False,
        DATABASES={'default': dj_database_url.config()},
        INSTALLED_APPS=('tx_lege_districts',),
        ROOT_URLCONF='tx_lege_districts.urls',
        )

from django.test.utils import get_runner


def run_tests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['tx_lege_districts'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    run_tests()
