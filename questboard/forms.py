from django import forms

from .models import *


class HomepageForm(forms.ModelForm):
	class Meta:
		model = CreateQuestboard
		fields = [
			'name',
			'description',
			'required_stars',
		]

class QuestboardPageForm(forms.ModelForm):
	class Meta:
		model = CreateQuest
		fields = [
			# 'user',
			'name',
			'description',
			'stars_given',
			'dropdown',
			'student1',
			'student2',
			'student3',
		]