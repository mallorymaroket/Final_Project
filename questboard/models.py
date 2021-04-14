from django.db import models


class CreateQuestboard(models.Model):
    name = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    required_stars = models.PositiveIntegerField()

    def __str__(self):
    	return self.name


class CreateQuest(models.Model):
	# user = models.ForeignKey(to=CreateQuestboard, on_delete=models.CASCADE)
	questboard = models.ForeignKey(CreateQuestboard, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=100, null=True)
	description = models.TextField(null=True)
	stars_given = models.PositiveIntegerField()


	dropdown_choices = [
		('Everyone', 'Yes'), ('Student/s', 'No'),
	]
	dropdown = models.CharField(max_length=9, choices=dropdown_choices, verbose_name="For everyone?")
	student1 = models.CharField(max_length=50, blank=True, verbose_name="Student 1:")
	student2 = models.CharField(max_length=50, blank=True, verbose_name="Student 2:")
	student3 = models.CharField(max_length=50, blank=True, verbose_name="Student 3:")
