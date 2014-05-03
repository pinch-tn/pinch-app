from django.shortcuts import render

## Create your views here.
from django.http import HttpResponse


def create_project(request):
    return render(request, "create_project.html")

def big_idea(request):
    return render(request, "big_idea.html")

def create_mvp(request):
    return render(request, "create_mvp.html")

def gravity_board(request):
    return render(request, "gravity_board.html")

def minify_mvp(request):
    return render(request, "minify_mvp.html")

def validate(request):
    return render(request, "validate.html")
    