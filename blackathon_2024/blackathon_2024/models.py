from django.db import models

class Perspectives(models.models):

    description = models.TextField
    endorsment = models.IntegerField
    title = models.TextField
    tags = models.ManyToManyField('Tags', through="tag_")

class Events(models.models):

    title = models.TextField
    date = models.IntegerField
    time = models.IntegerField
    description = models.TextField
    tags = models.ManyToManyField('Tags', through="tag_")

class Tags(models.models):

    name = models.TextField