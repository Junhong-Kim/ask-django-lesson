import re

from django.db import models
from django.forms import ValidationError


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    author = models.CharField(max_length=20)
    # 길이 제한이 있는 문자열
    title = models.CharField(max_length=100,
                             verbose_name='제목',
                             help_text='포스팅 제목을 입력해주세요 (최대 100자)')
    # 길이 제한이 없는 문자열
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50,
                              blank=True,
                              validators=[lnglat_validator],
                              help_text='위도/경도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
