from django.db import models

class CDR(models.Model):

    from_number = models.CharField(max_length=12)
    to_number = models.CharField(max_length=12)
    status = models.CharField(max_length=20)
    start_time = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(max_length=5)

