from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .forms import *

from .models import *

def homepage_view(request):
	form = QuestBoardForm(request.POST or None)
	qb_count = QuestBoard.objects.all().count()
	qb_id = list(QuestBoard.objects.values_list('name', flat=True).distinct())
	if request.method == 'POST':
		if form.is_valid():
			new_questboard = form.save()
			questboard_id = new_questboard.id
			obj = QuestBoard.objects.get(id=questboard_id)
			form = QuestBoardForm()
	context = {
			'form' : form,
			'object' : obj,
		}
	return render(request, "homepage.html", context)