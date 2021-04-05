from django.db import models


class QuestBoard(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    required_stars = models.PositiveIntegerField()