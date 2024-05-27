from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Dataset

def index(request):
    datasets_list = Dataset.objects.order_by("title")
    context = { 'datasets_list': datasets_list, }
    return render(request, 'datasets/index.html', context)

def detail(request, dataset_id):
    response = "You're looking at data set %s."
    return HttpResponse(response % dataset_id)

def analysis(request, dataset_id):
    response = "You're looking at the analysis path for data set %s."
    return HttpResponse(response % dataset_id)