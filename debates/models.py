

# Create your models here.
from django.conf import settings
from django.db import models
from catalog.models import Anime, Character

AGENDA_CHOICES = [
    ("powerscaling", "Powerscaling"),
    ("writing", "Writing / Themes"),
    ("matchups", "Matchups"),
    ("hot_takes", "Hot Takes"),
    ("meta", "Meta / Community"),
]

class DebateThread(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name="debate_threads")
    agenda = models.CharField(max_length=30, choices=AGENDA_CHOICES)
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.anime.title} [{self.agenda}] {self.title}"

class DebatePost(models.Model):
    thread = models.ForeignKey(DebateThread, on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    claim = models.CharField(max_length=240)
    evidence = models.CharField(max_length=240)
    counterpoint = models.CharField(max_length=240, blank=True)
    related_character = models.ForeignKey(Character, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.author} on {self.thread}"
