from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    started = models.DateTimeField(blank=True, null=True, editable=False)
    ended = models.DateTimeField(blank=True, null=True, editable=False)

    idea = models.TextField(blank=True)
    validate_customer = models.TextField(blank=True)
    validate_offering = models.TextField(blank=True)
    validate_value_prop = models.TextField(blank=True)
