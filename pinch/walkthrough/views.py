from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from models import Project


class CreateProjectView(TemplateView):
    template_name = "create_project.html"

    def get(self, request, *args, **kwargs):
        return super(CreateProjectView, self).get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        project = Project.objects.create(name=request.POST.get("projectName", ""))
        project.started = project.created
        project.save()
        return redirect("big_idea", name=project.name)



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

