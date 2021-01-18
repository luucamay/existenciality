
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


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
