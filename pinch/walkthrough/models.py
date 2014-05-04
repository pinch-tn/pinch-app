import datetime
from django.db import models
from django_extensions.db.fields import AutoSlugField


class Project(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = AutoSlugField(populate_from="name")
    created = models.DateTimeField(auto_now_add=True)
    started = models.DateTimeField(blank=True, null=True, editable=False)
    ended = models.DateTimeField(blank=True, null=True, editable=False)

    idea = models.TextField(blank=True)
    tools = models.TextField(blank=True)
    validate_customer = models.TextField(blank=True)
    validate_offering = models.TextField(blank=True)
    validate_value_prop = models.TextField(blank=True)

    @property
    def has_mvp(self):
        try:
            return self.mvp is not None
        except Mvp.DoesNotExist:
            return False

    def __unicode__(self):
        return self.name

    def is_frozen(self):
        return datetime.datetime.now() > self.ended

    def is_workstream_frozen(self):
        return self.has_mvp and self.mvp.workstream_set


class Mvp(models.Model):
    project = models.OneToOneField(Project)
    original_statement = models.TextField(blank=True)

    @property
    def statement(self):
        original_statement = self.original_statement.split("\n")
        minified_statement = [""] * len(original_statement)
        redactions = MvpRedaction.objects.all().filter(mvp=self).order_by("statement_start")
        last_redaction_end = [0] * len(minified_statement)
        for redaction in redactions:
            line = redaction.line
            if redaction.statement_start > last_redaction_end[line]:
                minified_statement[line] = minified_statement[line] + original_statement[line][last_redaction_end[line]:redaction.statement_start]
            last_redaction_end[line] = redaction.statement_end
        for line in range(0, len(original_statement)):
            minified_statement[line] = minified_statement[line] + original_statement[line][last_redaction_end[line]:len(original_statement[line])]
        return "\n".join(minified_statement)


class MvpRedaction(models.Model):
    mvp = models.ForeignKey(Mvp)
    line = models.IntegerField()
    statement_start = models.IntegerField()
    statement_end = models.IntegerField()


class Workstream(models.Model):
    mvp = models.ForeignKey(Mvp)
    line = models.IntegerField()
    statement_start = models.IntegerField()
    statement_end = models.IntegerField()
    name = models.TextField()
    owner = models.TextField(blank=True)


class Ticket(models.Model):
    mvp = models.ForeignKey(Mvp)
    workstream = models.ForeignKey(Workstream)
    content = models.TextField(blank=True)
    status = models.CharField(max_length=20)

