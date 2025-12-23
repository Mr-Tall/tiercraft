from django.db import models
from django.utils.text import slugify

class Anime(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True)
    cover_image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:220]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Character(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name="characters")
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, blank=True)
    image_url = models.URLField(blank=True)
    tags = models.JSONField(default=list, blank=True)  # e.g. ["villain", "goat", "wasted potential"]
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["anime", "name"], name="uniq_character_name_per_anime")
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.anime.title}-{self.name}")[:220]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.anime.title})"
