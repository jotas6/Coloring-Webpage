from django.urls import path
from . import views

app_name = "coloring"
urlpatterns = [path("color/", views.color, name = "color"),
               path("background/", views.background, name = "background"),
               path("black_white/", views.black_white, name = "black_white"),
               path("results/", views.results, name = "results"),
               path("home/", views.home, name = "home")]