from django.db import models
from django.urls import reverse
# from imagekit.models import ImageSpecField, ProcessedImageField
# from imagekit.processors import Thumbnail


STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:detail', args=[self.id])
