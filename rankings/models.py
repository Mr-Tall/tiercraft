
# Create your models here.
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from catalog.models import Anime, Character

TIER_CHOICES = [
    ("S", "S"),
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("F", "F"),
]

TIER_TO_NUM = {"S": 6, "A": 5, "B": 4, "C": 3, "D": 2, "F": 1}

def score_validators():
    return [MinValueValidator(0), MaxValueValidator(5)]

class TierList(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tier_lists")
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name="tier_lists")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.anime.title})"


class TierListEntry(models.Model):
    tier_list = models.ForeignKey(TierList, on_delete=models.CASCADE, related_name="entries")
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="tier_entries")
    tier = models.CharField(max_length=1, choices=TIER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["tier_list", "character"], name="uniq_character_per_tierlist"),
        ]

    def __str__(self):
        return f"{self.character.name}: {self.tier}"


class Justification(models.Model):
    entry = models.OneToOneField(TierListEntry, on_delete=models.CASCADE, related_name="justification")

    writing_score = models.IntegerField(validators=score_validators())
    development_score = models.IntegerField(validators=score_validators())
    impact_score = models.IntegerField(validators=score_validators())
    consistency_score = models.IntegerField(validators=score_validators())
    enjoyment_score = models.IntegerField(validators=score_validators())

    evidence_1 = models.CharField(max_length=140)
    evidence_2 = models.CharField(max_length=140, blank=True)
    evidence_3 = models.CharField(max_length=140, blank=True)

    tags = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def evidence_list(self):
        return [e for e in [self.evidence_1, self.evidence_2, self.evidence_3] if e]

    def __str__(self):
        return f"Justification for {self.entry}"


class JustificationVote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    justification = models.ForeignKey(Justification, on_delete=models.CASCADE, related_name="votes")
    value = models.SmallIntegerField(choices=[(1, "Agree"), (-1, "Disagree")])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "justification"], name="uniq_vote_per_user_justification"),
        ]
