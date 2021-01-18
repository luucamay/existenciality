from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Car


class CarAdmin(admin.ModelAdmin):

    readonly_fields = ["photo", "headshot_image"]

    def headshot_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.photo.url,
            width=obj.photo.width,
            height=obj.photo.height,
        )
        )


# Register your models here.
admin.site.register(Car, CarAdmin)
