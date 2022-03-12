from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import color_form
import matplotlib.pyplot as plt
import os
from . import funcs
import numpy as np
from django.urls import reverse
from PIL import Image

path_to_images = os.path.realpath(os.path.join(os.path.dirname(__file__), "static", "coloring", "images", "im.jpg"))

# Create your views here.
def color(request):

    if request.method == 'POST':

        form = color_form(request.POST, request.FILES)

        if form.is_valid():

            c_hex = request.POST.get("color_value")
            color = np.array(funcs.hex_to_rgb(c_hex))/255

            image = form.cleaned_data["image"]
            nueva_imagen = funcs.cambia_color_base(image, color)

            plt.imsave(path_to_images, nueva_imagen)
            
            return HttpResponseRedirect(reverse("coloring:results"))

        else:
            
            return render(request, "coloring/color.html", {"page": "color", "form": form})
        
        
    return render(request, "coloring/color.html", {"page": "color", "form": color_form()})


def background(request):

    if request.method == "POST":

        form = color_form(request.POST, request.FILES)

        if form.is_valid():

            c_hex = request.POST.get("color_value")
            color = np.array(funcs.hex_to_rgb(c_hex))/255

            image = form.cleaned_data["image"]
            nueva_imagen = funcs.cambia_fondo(image, color)

            plt.imsave(path_to_images, nueva_imagen)
            
            return HttpResponseRedirect(reverse("coloring:results"))

        else: 
            
            return render(request, "coloring/background.html", {"page": "color", "form": form})

    return render(request, "coloring/background.html", {"page": "background", "form": color_form()})

def black_white(request):

    if request.method == "POST":

        form = color_form(request.POST, request.FILES)

        if form.is_valid():

            image = form.cleaned_data["image"]
            nueva_imagen = funcs.blanco_negro(image)

            plt.imsave(path_to_images, nueva_imagen)
            
            return HttpResponseRedirect(reverse("coloring:results"))

        else: 
            
            return render(request, "coloring/black_white.html", {"page": "blackwhite", "form": form})

    return render(request, "coloring/black_white.html", {"form": color_form()})

def results(request):

    return render(request, "coloring/color_results.html")

def home(request):

    return render(request, "coloring/home.html")