from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Media(models.Model):
    file_path = models.TextField(max_length=500)
    file_extension = models.TextField(max_length=200)
    territory = models.TextField(max_length=100, null=True)
