from django.contrib import admin
from . import models



@admin.register(models.IpData)
class IpData(admin.ModelAdmin):
    pass
