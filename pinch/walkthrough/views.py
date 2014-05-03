from django.shortcuts import render

## Create your views here.
from django.http import HttpResponse


def create_project(request):
    return render(request, "create_project.html")


