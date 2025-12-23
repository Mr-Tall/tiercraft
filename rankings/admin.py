
# Register your models here.
from django.contrib import admin
from .models import TierList, TierListEntry, Justification, JustificationVote

@admin.register(TierList)
class TierListAdmin(admin.ModelAdmin):
    list_display = ("title", "anime", "owner", "is_public", "updated_at")
    list_filter = ("is_public", "anime")
    search_fields = ("title", "owner__username", "anime__title")

@admin.register(TierListEntry)
class TierListEntryAdmin(admin.ModelAdmin):
    list_display = ("tier_list", "character", "tier", "created_at")
    list_filter = ("tier", "tier_list__anime")

@admin.register(Justification)
class JustificationAdmin(admin.ModelAdmin):
    list_display = ("entry", "updated_at")

@admin.register(JustificationVote)
class JustificationVoteAdmin(admin.ModelAdmin):
    list_display = ("user", "justification", "value", "created_at")
