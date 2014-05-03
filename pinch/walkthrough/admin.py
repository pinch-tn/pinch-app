from django.contrib import admin
from models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'created', 'started', 'ended')

admin.site.register(Project, ProjectAdmin)
