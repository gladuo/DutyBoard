from __future__ import unicode_literals

from django.db import models


class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    date = models.DateField()
    category = models.ForeignKey(Project)

    def __unicode__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=32)
    slug = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name
