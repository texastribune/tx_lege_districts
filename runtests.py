import sys

from django.conf import settings

try:
    from local_settings import DATABASES
except ImportError:
    raise RuntimeError('You must provide a local_settings.py with a DATABASES '
                       'setting containing your GIS-capable database backend.')

settings.configure(
        DEBUG=False,
        DATABASES=DATABASES,
        INSTALLED_APPS=('lege_districts',),
        ROOT_URLCONF='lege_districts.urls',
        )

from django.test.utils import get_runner


def run_tests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['lege_districts'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    run_tests()
