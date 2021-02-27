from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("meme/", views.meme, name="meme")
]