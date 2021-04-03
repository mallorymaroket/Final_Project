from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def homepage_view(request):
	return render(request, "homepage.html")