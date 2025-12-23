from django.contrib import admin
from .models import Anime, Character

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "anime")
    list_filter = ("anime",)
    search_fields = ("name", "anime__title")
