from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    started = models.DateTimeField(blank=True, null=True, editable=False)
    ended = models.DateTimeField(blank=True, null=True, editable=False)

    idea = models.TextField(blank=True)
    tools = models.TextField(blank=True)
    validate_customer = models.TextField(blank=True)
    validate_offering = models.TextField(blank=True)
    validate_value_prop = models.TextField(blank=True)

class Mvp(models.Model):
    project = models.OneToOneField(Project, primary_key=True)
    original_statement = models.TextField(blank=True)

class MvpRedaction(models.Model):
    mvp = models.ForeignKey(Mvp, primary_key=True)
    statement_start = models.IntegerField()
    statement_end = models.IntegerField()

class Workstream(models.Model):
    mvp = models.ForeignKey(Mvp, primary_key=True)
    statement_start = models.IntegerField()
    statement_end = models.IntegerField()
    name = models.TextField()
    owner = models.TextField()


class Ticket(models.Model):
    workstream = models.ForeignKey(Workstream, primary_key=True)
    content = models.TextField()
    status = models.CharField(max_length=20)

