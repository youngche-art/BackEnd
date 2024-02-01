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


# Create your models here.
class Picture(TimeStampedModel): 

    마음 = models.ManyToManyField("Mind", related_name="mind", blank=True, null=True)  

    