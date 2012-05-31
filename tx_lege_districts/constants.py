HOUSE = 'HOUSE'
SENATE = 'SENATE'
SBOE = 'SBOE'

TYPE_CHOICES = (
    (HOUSE, 'House'),
    (SENATE, 'Senate'),
    (SBOE, 'State Board of Education'),
)

REMEDIAL = 'REMEDIAL'
INTERIM = 'INTERIM'
FINAL = 'FINAL'
STATUS_CHOICES = (
    (REMEDIAL, 'Remedial'),
    (INTERIM, 'Interim'),
    (FINAL, 'Final')
)
