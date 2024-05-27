from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the datasets index.")

def detail(request, dataset_id):
    response = "You're looking at data set %s."
    return HttpResponse(response % dataset_id)

def analysis(request, dataset_id):
    response = "You're looking at the analysis path for data set %s."
    return HttpResponse(response % dataset_id)