HOUSE = 'HOUSE'
SENATE = 'SENATE'
CONGRESS = 'CONGRESS'
SBOE = 'SBOE'

TYPE_CHOICES = (
    (HOUSE, 'Texas House'),
    (SENATE, 'Texas Senate'),
    (CONGRESS, 'Congressional'),
    (SBOE, 'State Board of Education'),
)

PLAN_TYPES = {
    'H': HOUSE,
    'S': SENATE,
    'C': CONGRESS,
    'E': SBOE,
}

REMEDIAL = 'REMEDIAL'
INTERIM = 'INTERIM'
FINAL = 'FINAL'
STATUS_CHOICES = (
    (REMEDIAL, 'Remedial'),
    (INTERIM, 'Interim'),
    (FINAL, 'Final')
)
