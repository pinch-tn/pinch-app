from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    started = models.DateTimeField(blank=True, null=True, editable=False)
    ended = models.DateTimeField(blank=True, null=True, editable=False)

    idea = models.TextField(blank=True)
    validate_customer = models.TextField(blank=True)
    validate_offering = models.TextField(blank=True)
    validate_value_prop = models.TextField(blank=True)

class Mvp(models.Model):
    project = models.OneToOneField(Project)
    statement_text = models.TextField()

class MvpRedaction(models.Model):
    mvp = models.ForeignKey(Mvp)
    start = models.IntegerField()
    end = models.IntegerField()

