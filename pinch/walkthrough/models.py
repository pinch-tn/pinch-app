from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    started = models.DateTimeField()
    ended = models.DateTimeField()

    idea = models.TextField()
    validate_customer = models.TextField()
    validate_offering = models.TextField()
    validate_value_prop = models.TextField()
