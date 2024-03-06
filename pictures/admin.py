from django.contrib import admin
from . import models

@admin.register(models.Mind, models.Color, models.Shape)
class ItemAdmin(admin.ModelAdmin):

    pass


# Register your models here.
@admin.register(models.Picture)
class PictureAdmin(admin.ModelAdmin):
        pass


