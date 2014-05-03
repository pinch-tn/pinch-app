from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView


class CreateProjectView(TemplateView):
    template_name = "create_project.html"

class BigIdeaView(TemplateView):
    template_name = "big_idea.html"


