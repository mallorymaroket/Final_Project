from django.db import models


class CreateQuestboard(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    required_stars = models.PositiveIntegerField()

class CreateQuest(models.Model):
	# user = models.ForeignKey(to=CreateQuestboard, on_delete=models.CASCADE)
	name = models.CharField(max_length=40)
	description = models.TextField()
	stars_given = models.PositiveIntegerField()
	Yes = 'Yes'
	No = 'No'
	everyone_dropdown_choices = [
		(Yes, 'Yes'), (No, 'No'),
	]
	dropdown = models.CharField(max_length=3, choices=everyone_dropdown_choices)