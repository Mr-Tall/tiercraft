from django.contrib import admin
from .models import DebateThread, DebatePost

@admin.register(DebateThread)
class DebateThreadAdmin(admin.ModelAdmin):
    list_display = ("title", "anime", "agenda", "created_by", "created_at")
    list_filter = ("agenda", "anime")
    search_fields = ("title", "anime__title", "created_by__username")

@admin.register(DebatePost)
class DebatePostAdmin(admin.ModelAdmin):
    list_display = ("thread", "author", "related_character", "created_at")
    search_fields = ("claim", "evidence", "author__username")
