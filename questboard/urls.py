from django.urls import path

from .views import *

urlpatterns = [
	path('', homepage_view, name='home'),
	path('', questboard_list, name='questboard_list'),
	path('', questboard_create, name='questboard_create'),
    path('', questboard_edit, name='questboard_edit'),
    path('', questboard_delete, name='questboard_delete'),
    path('', quest_list, name='quest_list'),
]