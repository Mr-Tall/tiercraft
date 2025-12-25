from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.home, name="home"),
    path("anime/<slug:slug>/", views.anime_detail, name="anime_detail"),
]
