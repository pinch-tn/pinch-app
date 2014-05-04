from django.contrib import admin
from models import Project, MvpRedaction, Workstream
from models import Mvp
from models import Ticket


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created', 'started', 'ended')

class MvpAdmin(admin.ModelAdmin):
    list_display = ("project", "original_statement")

admin.site.register(Project, ProjectAdmin)
admin.site.register(Mvp, MvpAdmin)
admin.site.register(Ticket)
admin.site.register(MvpRedaction)
admin.site.register(Workstream)
