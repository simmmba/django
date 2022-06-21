import re
from django.conf import settings
from django.db import models
from django.forms import ValidationError


def lnglat_validator(value):
    if not re.match(r'(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

REGION_CHOICE = (
    ('Africa', '아프리카'),
    ('Europe', '유럽'),
    ('Oceania', '오세아니아'),
    ('Asia', '아시아'),
    ('North America', '북아메리카'),
    ('South America', '남아메리카'),
)
