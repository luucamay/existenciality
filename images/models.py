from django.db import models


class Car(models.Model):
    photo = models.ImageField(upload_to='cars')
