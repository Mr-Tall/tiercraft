from django.shortcuts import get_object_or_404, render
from .models import Anime

def home(request):
    anime_list = Anime.objects.order_by("title")
    return render(request, "catalog/home.html", {"anime_list": anime_list})


def anime_detail(request, slug):
    anime = get_object_or_404(Anime, slug=slug)
    characters = anime.characters.order_by("name")
    return render(request, "catalog/anime_detail.html", {"anime": anime, "characters": characters})
