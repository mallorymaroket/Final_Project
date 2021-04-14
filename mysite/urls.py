"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include

from questboard.views import *

urlpatterns = [
	path('', homepage_view),
	path('home/', homepage_view),
    path('admin/', admin.site.urls),
    path('questboard/', questboard_list, name='questboard_list'),
    path(r'^questboard/create/$', questboard_create, name='questboard_create'),
    path(r'^questboard/(?P<pk>\d+)/edit/$', questboard_edit, name='questboard_edit'),
    path(r'^questboard/(?P<pk>\d+)/delete/$', questboard_delete, name='questboard_delete'),

    path('quests/<str:pk>/', quest_list, name='quest_list'),
    path('create_quest/', quest_create, name='quest_create'),
    path('delete_quest/<str:pk>/', quest_delete, name='quest_delete'),
    path('edit_quest/<str:pk>/', quest_edit, name="quest_edit"),
    path('dibs_quest/<str:pk>/', quest_dibs, name="quest_dibs"),
]