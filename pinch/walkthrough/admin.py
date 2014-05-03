from django.contrib import admin
from models import Project
from models import Mvp


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'created', 'started', 'ended')

class MvpAdmin(admin.ModelAdmin):
    list_display = ("project", "statement_text")

admin.site.register(Project, ProjectAdmin)
admin.site.register(Mvp, MvpAdmin)
