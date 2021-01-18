
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


def car_image_view(request):

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CarForm()
    return render(request, 'images/form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def display_car_images(request):

    if request.method == 'GET':

        # getting all the objects of car.
        # TO DO: answer why is the car Model not imported?
        Cars = Car.objects.all()
        return render(request, 'images/display_car_images.html',
                      {'car_images': Cars})
