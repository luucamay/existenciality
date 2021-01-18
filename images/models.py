from django.db import models
from django.utils.safestring import mark_safe


class Car(models.Model):
    photo = models.ImageField(upload_to='cars')

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.photo.url))
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.photo.url
