from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import TimeStampedModel
from django.urls import reverse

from core import models as core_models

class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True
        db_table = ""

    def __str__(self):
        return self.name


class Mind(models.Model):

    """ RoomType Model Definition """
    
    name = models.CharField(max_length=80)

    class Meta:
        db_table = "mind"

    def __str__(self):
        return self.name
    
class Shape(models.Model):

    """ RoomType Model Definition """
    
    name = models.CharField(max_length=80)

    class Meta:
        db_table = "shape"

    def __str__(self):
        return self.name
    

class Color(models.Model):

    """ RoomType Model Definition """
    
    name = models.CharField(max_length=80)

    class Meta:
        db_table = "color"

    def __str__(self):
        return self.name


class Picture(TimeStampedModel):
    번호 = models.IntegerField()  # 숫자 형식으로 변경
    제목 = models.CharField(max_length=200)
    작품번호 = models.IntegerField()  # 숫자 형식으로 변경
    이미지 = models.URLField()  # 이미지 URL 형식으로 변경
    보관위치 = models.CharField(max_length=200)
    호수 = models.CharField(max_length=200)
    연속번호 = models.IntegerField()  # 숫자 형식으로 변경
    창작날짜 = models.DateField()  # 날짜 형식으로 변경
    일차 = models.IntegerField()  # 숫자 형식으로 변경
    재료 = models.CharField(max_length=200)
    세로X가로 = models.CharField(max_length=200)
    판매가격 = models.CharField(max_length=200)
    구매자 = models.CharField(max_length=200)
    상세설명 = models.TextField()  # 텍스트 형식으로 변경
    마음 = models.ManyToManyField("Mind", related_name="pictures", blank=True)  # 외래 키 필드 추가
    형태 = models.ManyToManyField("Shape", related_name="pictures", blank=True)  # 외래 키 필드 추가
    색 = models.ManyToManyField("Color", related_name="pictures", blank=True)  # 외래 키 필드 추가


    