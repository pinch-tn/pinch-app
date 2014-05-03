from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, View
from models import Project


class RootProjectView(View):

    def get(self, request, *args, **kwargs):
        project_name = kwargs["name"]
        project = Project.objects.get(name=project_name)
        if not project.idea:
            return redirect("big_idea", name=project_name)
        elif not (project.validate_customer and project.validate_offering and project.validate_value_prop):
            return redirect("validate", name=project_name)
        else:
            # Do more ifs once the data model is more complete
            return redirect("create_mvp", name=project_name)



class CreateProjectView(TemplateView):
    template_name = "create_project.html"

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

    def post(self, request, *args, **kwargs):
        project_name = kwargs["name"]
        project = Project.objects.get(name=project_name)
        project.idea = request.POST.get("bigIdea", "")
        project.save()
        return redirect("validate", name=project_name)


class CreateMvpView(TemplateView):
    template_name = "create_mvp.html"


class GravityBoardView(TemplateView):
    template_name = "gravity_board.html"


class MinifyMvpView(TemplateView):
    template_name = "minify_mvp.html"


class ValidateView(TemplateView):
    template_name = "validate.html"

