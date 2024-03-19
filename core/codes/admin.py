from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _


class CodeListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'link')
    list_filter = ['user', 'created_at', 'category']

    def total_listings(self, obj: models.CodeListing):
        return obj.listings.count()
    total_listings.short_description = _('total listings')

admin.site.register(models.CodeListing, CodeListingAdmin)