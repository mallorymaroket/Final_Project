import django_filters
from .models import *


class QuestFilter(django_filters.FilterSet):
	class Meta:
		model = CreateQuest
		fields = '__all__'
		exclude = ['questboard']