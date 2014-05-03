from django.shortcuts import render

## Create your views here.
from django.http import HttpResponse


def poll(request):
    return HttpResponse("Hello, world. You're at the poll index.")


# def create_project(request):

