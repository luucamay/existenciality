
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('upload', car_image_view, name='upload'),
    path('success', success, name='success'),
]
