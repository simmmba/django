from django.db import models
from django.urls import reverse
# from imagekit.models import ImageSpecField, ProcessedImageField
# from imagekit.processors import Thumbnail


STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)
