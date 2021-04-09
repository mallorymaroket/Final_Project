from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.views import View

from .forms import *
from .models import *

def homepage_view(request):
		return render(request, "homepage.html")

def questboard_list(request):
	obj = CreateQuestboard.objects.all()
	return render(request, 'questboard_list.html', {'obj':obj})

def save_questboard_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            obj = CreateQuestboard.objects.all()
            data['html_list'] = render_to_string('questboard_partial.html', {
                'obj': obj
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def questboard_create(request):
    if request.method == 'POST':
        form = HomepageForm(request.POST)
    else:
        form = HomepageForm()
    return save_questboard_form(request, form, 'questboard_create.html')

def questboard_edit(request, pk):
    questboard = get_object_or_404(CreateQuestboard, pk=pk)
    if request.method == 'POST':
        form = HomepageForm(request.POST, instance=questboard)
    else:
        form = HomepageForm(instance=questboard)
    return save_questboard_form(request, form, 'questboard_edit.html')

def questboard_delete(request, pk):
    questboard = get_object_or_404(CreateQuestboard, pk=pk)
    data = dict()
    if request.method == 'POST':
        questboard.delete()
        data['form_is_valid'] = True
        obj = CreateQuestboard.objects.all()
        data['html_list'] = render_to_string('questboard_partial.html', {
            'obj': obj
        })
    else:
        context = {'questboard': questboard}
        data['html_form'] = render_to_string('questboard_delete.html', context, request=request)
    return JsonResponse(data)