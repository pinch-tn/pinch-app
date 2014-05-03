from django.contrib import admin
from models import Project
from models import Mvp


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created', 'started', 'ended')

class MvpAdmin(admin.ModelAdmin):
    list_display = ("project", "original_statement")

admin.site.register(Project, ProjectAdmin)
admin.site.register(Mvp, MvpAdmin)
