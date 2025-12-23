from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ("user__username", "user__email")
    list_display = ("user", "favorite_anime", "created_at")
