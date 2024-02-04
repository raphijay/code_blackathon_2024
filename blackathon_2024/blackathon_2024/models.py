from django.db import models

class Persepectives(models.models):

    description = models.TextField
    endorsment = models.IntegerField
    title = models.TextField
    data = models.IntegerField

    