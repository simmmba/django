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


class Post(models.Model):
    title = models.CharField(
        max_length=100, verbose_name='제목', help_text='포스팅 제목을 입력해주세요. 최대 100자 내외')
    content = models.TextField(verbose_name='내용')
    region = models.CharField(
        max_length=20, choices=REGION_CHOICE, default='Asia')
    tags = models.CharField(max_length=100, verbose_name='태그', blank=True)
    lnglat = models.CharField(
        max_length=50, verbose_name='위경도', blank=True, validators=[lnglat_validator], help_text='경도,위도 포맷으로 입력')
    create_at = models.DateField(auto_now_add=True)  # 수정불가
    updated_at = models.DateTimeField(auto_now=True)  # 수정가능
    tag_set = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
