from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, View
from models import Project, Mvp


class RootProjectView(View):

    def get(self, request, *args, **kwargs):
        project_slug = kwargs["slug"]
        project = Project.objects.get(slug=project_slug)
        if not project.idea:
            return redirect("big_idea", slug=project_slug)
        elif not (project.validate_customer and project.validate_offering and project.validate_value_prop):
            return redirect("validate", slug=project_slug)
        elif (not project.has_mvp) or not project.mvp.original_statement:
            # Do more ifs once the data model is more complete
            return redirect("create_mvp", slug=project_slug)
        else:
            return redirect("minify_mvp", slug=project_slug)


class CreateProjectView(TemplateView):
    template_name = "create_project.html"

    def post(self, request, *args, **kwargs):
        project = Project.objects.create(name=request.POST.get("projectName", ""))
        project.started = project.created
        project.save()
        return redirect("big_idea", slug=project.slug)


class BigIdeaView(TemplateView):
    template_name = "big_idea.html"

    def get_context_data(self, **kwargs):
        return {
            "project": Project.objects.get(slug=kwargs["slug"])
        }

    def post(self, request, *args, **kwargs):
        project_slug = kwargs["slug"]
        project = Project.objects.get(slug=project_slug)
        project.idea = request.POST.get("bigIdea", "")
        project.save()
        return redirect("validate", slug=project_slug)


class SelectToolsView(TemplateView):
    template_name = "select_tools.html"

    def get_context_data(self, **kwargs):
        return {
            "project": Project.objects.get(slug=kwargs["slug"])
        }

    def post(self, request, *args, **kwargs):
        project_slug = kwargs["slug"]
        project = Project.objects.get(slug=project_slug)
        project.tools = request.POST.get("tools", "")
        project.save()
        return redirect("gravity_board", slug=project_slug)


class ValidateView(TemplateView):
    template_name = "validate.html"

    def get_context_data(self, **kwargs):
        return {
            "project": Project.objects.get(slug=kwargs["slug"])
        }

    def post(self, request, *args, **kwargs):
        project_slug = kwargs["slug"]
        project = Project.objects.get(slug=project_slug)
        project.validate_offering = request.POST.get("offering", "")
        project.validate_customer = request.POST.get("customer", "")
        project.validate_value_prop = request.POST.get("valueProp", "")
        project.save()
        return redirect("create_mvp", slug=project_slug)


class CreateMvpView(TemplateView):
    template_name = "create_mvp.html"

    def get_context_data(self, **kwargs):
        project = Project.objects.get(slug=kwargs["slug"])
        return {
            "project": project,
        }

    def post(self, request, *args, **kwargs):
        project_slug = kwargs["slug"]
        project = Project.objects.get(slug=project_slug)
        if project.has_mvp:
            mvp = project.mvp
        else:
            mvp = Mvp.objects.create(project=project)
        mvp.original_statement = request.POST.get("original_statement", "")
        mvp.save()
        return redirect("minify_mvp", slug=project_slug)


class GravityBoardView(TemplateView):
    template_name = "gravity_board.html"


class MinifyMvpView(TemplateView):
    template_name = "minify_mvp.html"

    def get_context_data(self, **kwargs):
        project = Project.objects.get(slug=kwargs["slug"])
        return {
            "project": project,
            }

