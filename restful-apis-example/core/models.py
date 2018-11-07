from django.db import models

class Api(models.Model):
    status = models.BooleanField(default=True)