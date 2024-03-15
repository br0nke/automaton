from django.contrib import admin
from . import models


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('picture')


admin.site.register(models.Profile)