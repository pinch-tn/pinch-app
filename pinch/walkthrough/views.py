from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView
from models import Project


class CreateProjectView(TemplateView):
    template_name = "create_project.html"


class BigIdeaView(TemplateView):
    template_name = "big_idea.html"

    def get_context_data(self, **kwargs):
        return {
            "project": Project.objects.get(name=kwargs["name"])
        }


class CreateMvpView(TemplateView):
    template_name = "create_mvp.html"


class GravityBoardView(TemplateView):
    template_name = "gravity_board.html"


class MinifyMvpView(TemplateView):
    template_name = "minify_mvp.html"


class ValidateView(TemplateView):
    template_name = "validate.html"

