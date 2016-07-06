from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)
    def __unicode__(self):
        return self.name
