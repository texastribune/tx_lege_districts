import glob
import os
import sys

from django.contrib.gis.utils import LayerMapping

from tx_lege_districts.models import District
from tx_lege_districts.constants import PLAN_TYPES


class DistrictMapping(LayerMapping):
    mapping = {
        'number' : 'District',
        'geometry' : 'POLYGON',
    }

    def __init__(self, shp, year, **kwargs):
        base_name = os.path.basename(shp)
        assert base_name.startswith('PLAN')
        type_code = base_name[4]
        self.year = year
        self.type = PLAN_TYPES[type_code]
        super(DistrictMapping, self).__init__(
            District, shp, self.mapping, **kwargs)

    def feature_kwargs(self, feat):
        kwargs = super(DistrictMapping, self).feature_kwargs(feat)
        kwargs.update(year=self.year, type=self.type)
        return kwargs


def main(script, root, year, using=None):
    root = os.path.abspath(root)
    year = int(year)
    for shp in glob.glob(os.path.join(root, "*.shp")):
        lm = DistrictMapping(shp, year, transform=False, encoding='iso-8859-1',
                             using=using)
        lm.save(strict=True, verbose=True)


if __name__ == '__main__':
    if '--help' in sys.argv:
        print 'usage: python load_shapes.py <root> <year> [using]'
        exit()

    main(*sys.argv)
