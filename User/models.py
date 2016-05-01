from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    name = models.CharField(max_length=32, blank=True)
    class_id = models.CharField(max_length=32, blank=True)
    roll_id = models.CharField(max_length=32, blank=True)
    birthday = models.DateField(blank=True)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.name
