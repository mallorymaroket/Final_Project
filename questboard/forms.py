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