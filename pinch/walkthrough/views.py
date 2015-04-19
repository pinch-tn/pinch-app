import datetime
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, RedirectView, View
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from models import Project, ProjectMember, Mvp, MvpRedaction, Workstream, Ticket
import json

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

    def get_context_data(self, **kwargs):
        return {
            "event_default": "Hack Tennessee 7"
        }

    def post(self, request, *args, **kwargs):
        project = Project.objects.create(name=request.POST.get("projectName", ""))
        project.started = project.created
        project.ended = project.started + datetime.timedelta(days=14)
        event = request.POST.get("event")
        if event:
            project.event = event
        project.save()
        owner = ProjectMember.objects.create(project=project,
                                             name=request.POST.get("ownerName", ""),
                                             email=request.POST.get("ownerEmail", ""),
                                             owner=True)
        owner.save()

        memberNames = request.POST.getlist("memberName")
        memberEmails = request.POST.getlist("memberEmail")
        for name, email in zip(memberNames, memberEmails):
            if name:
                member = ProjectMember.objects.create(project=project,
                                                      name=name,
                                                      email=email,
                                                      owner=False)
                member.save()
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


class MinifyMvpView(TemplateView):
    template_name = "minify_mvp.html"

    def get_context_data(self, **kwargs):
        project = Project.objects.get(slug=kwargs["slug"])
        if project.has_mvp:
            current_selection = [{"line": r.line, "statement_start": r.statement_start, "statement_end": r.statement_end} for r in project.mvp.mvpredaction_set.all()]
        else:
            current_selection = []
        return {
            "project": project,
            "selectionJson": json.dumps(current_selection)
        }

    def post(self, request, *args, **kwargs):
        project_slug = kwargs["slug"]
        project = Project.objects.get(slug=project_slug)

        if project.has_mvp:
            mvp = project.mvp
        else:
            mvp = Mvp.objects.create(project=project)

        for redaction in mvp.mvpredaction_set.all():
            redaction.delete()

        raw_redactions = json.loads(request.POST.get("redactions", "[]"))
        # deduplicate
        redactions = [dict(t) for t in set([tuple(d.items()) for d in raw_redactions])]
        for add_redaction in redactions:
            line = add_redaction["line"]
            redaction = MvpRedaction.objects.create(mvp=mvp, line=line, statement_start=add_redaction["statement_start"],statement_end=add_redaction["statement_end"])
            redaction.save()
        return redirect("breakdown_mvp", slug=project_slug)


class BreakdownMvpView(TemplateView):
    template_name = "breakdown_mvp.html"

    def get_context_data(self, **kwargs):
        project = Project.objects.get(slug=kwargs["slug"])
        if project.has_mvp:
            current_selection = [{"line": w.line, "statement_start": w.statement_start, "statement_end": w.statement_end} for w in project.mvp.workstream_set.all()]
        else:
            current_selection = []
        return {
            "project": project,
            "selectionJson": json.dumps(current_selection)
        }

    def post(self, request, **kwargs):
        project_slug = kwargs["slug"]
        project = Project.objects.get(slug=project_slug)
        if project.has_mvp:
            mvp = project.mvp
        else:
            mvp = Mvp.objects.create(project=project)

        for workstream in mvp.workstream_set.all():
            workstream.delete()

        raw_workstreams = json.loads(request.POST.get("workstreams", "[]"))
        workstreams = [dict(t) for t in set([tuple(d.items()) for d in raw_workstreams])]

        for add_workstream in workstreams:
            line = add_workstream["line"]
            start = add_workstream["statement_start"]
            end = add_workstream["statement_end"]
            name = mvp.statement.split("\n")[line][start:end]
            workstream = Workstream.objects.create(mvp=mvp, name=name, line=line, statement_start=start, statement_end=end,)
            workstream.save()

        # add "select tech" workstream
        tech_ws = Workstream.objects.create(mvp=mvp,name="Tools & Technology", line=0, statement_start=0, statement_end=0)
        tech_ws.save()
        return redirect("gravity_board", slug=project_slug)


class GravityBoardView(TemplateView):
    template_name = "gravity_board.html"

    def get_context_data(self, **kwargs):
        project = Project.objects.get(slug=kwargs["slug"])
        return {
            "project": project,
        }

class TicketView(View):
    def get_context_data(self, **kwargs):
        project = Project.objects.get(slug=kwargs["slug"])
        return {
            "project": project,
        }

    def get(self, request, **kwargs):
        project_slug = kwargs["slug"]
        project = Project.objects.get(slug=project_slug)
        if project.has_mvp:
            mvp = project.mvp
        else:
            mvp = Mvp.objects.create(project=project)
        workstreams = mvp.workstream_set.all()
        return HttpResponse(json.dumps(self._convert_workstreams_to_json(workstreams)),mimetype='application/json')

    def _convert_ticket_to_json(self, t):
        t_out = {"id": t.id, "text": t.content}
        return t_out

    def _convert_workstreams_to_json(self, workstreams):
        all = []
        for w in workstreams:
            w_out = { "name": w.name, "ready":[], "doing":[], "done":[] }
            for t in w.ticket_set.all():
                t_out = self._convert_ticket_to_json(t)
                w_out[t.status].append(t_out)
            all.append(w_out)

        return all


    def post(self, request, **kwargs):
        project_slug = kwargs["slug"]
        project = Project.objects.get(slug=project_slug)
        if project.has_mvp:
            mvp = project.mvp
        else:
            mvp = Mvp.objects.create(project=project)

        create_ticket = json.loads(request.body)
        workstream = mvp.workstream_set.filter(name=create_ticket['workstream'])[0]
        ticket = Ticket.objects.create(mvp=mvp,content=create_ticket['content'],status=create_ticket['status'],workstream=workstream)
        ticket.save()
        return HttpResponse(json.dumps(self._convert_ticket_to_json(ticket)), content_type='application/json')

    def patch(self, request, **kwargs):
        project_slug = kwargs["slug"]
        project = Project.objects.get(slug=project_slug)
        if project.has_mvp:
            mvp = project.mvp
        else:
            mvp = Mvp.objects.create(project=project)

        update_ticket = json.loads(request.body)
        workstream = mvp.workstream_set.filter(name=update_ticket['workstream'])[0]
        ticket = Ticket.objects.get(pk=update_ticket['id'])
        ticket.workstream=workstream
        ticket.content=update_ticket['content']
        ticket.status=update_ticket['status']
        ticket.save()
        return HttpResponse("ok")

    def delete(self, request, **kwargs):
        project_slug = kwargs["slug"]
        project = Project.objects.get(slug=project_slug)
        if project.has_mvp:
            mvp = project.mvp
        else:
            mvp = Mvp.objects.create(project=project)

        delete_ticket = json.loads(request.body)
        Ticket.objects.get(pk=delete_ticket['id']).delete()
        return HttpResponse("id")

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(TicketView, self).dispatch(*args, **kwargs)
