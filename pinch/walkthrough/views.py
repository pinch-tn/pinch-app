from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView


class CreateProjectView(TemplateView):
    template_name = "create_project.html"

class BigIdeaView(TemplateView):
    template_name = "big_idea.html"

def create_mvp(request):
    return render(request, "create_mvp.html")

def gravity_board(request):
    return render(request, "gravity_board.html")

def minify_mvp(request):
    return render(request, "minify_mvp.html")

def validate(request):
    return render(request, "validate.html")
    
