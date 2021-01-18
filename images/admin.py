from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Car


class CarAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = ('image_tag', 'photo')
    readonly_fields = ('image_tag',)


# Register your models here.
admin.site.register(Car, CarAdmin)
