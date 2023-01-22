from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'site_vacancy/base.html')


def page_vacancy(request):
    return render(request, 'site_vacancy/index.html')

