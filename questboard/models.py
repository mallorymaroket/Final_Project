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


	dropdown_choices = [
		('Everyone', 'Yes'), ('Student/s', 'No'),
	]
	dropdown = models.CharField(max_length=9, choices=dropdown_choices, verbose_name="For everyone?")
	student1 = models.CharField(max_length=50, blank=True, verbose_name="Student 1:")
	student2 = models.CharField(max_length=50, blank=True, verbose_name="Student 2:")
	student3 = models.CharField(max_length=50, blank=True, verbose_name="Student 3:")