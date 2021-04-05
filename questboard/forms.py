from django import forms


from .models import *


class QuestBoardForm(forms.ModelForm):
	class Meta:
		model = QuestBoard
		fields = [
			'name',
			'description',
			'required_stars',
		]