from django.db import models


class CreateQuestboard(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    required_stars = models.PositiveIntegerField()