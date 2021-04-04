from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .forms import *

def homepage_view(request):
	form = CreateForm()
	return render(request, "homepage.html", {"form":CreateForm})