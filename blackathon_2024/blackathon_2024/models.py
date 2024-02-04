import datetime
from django.db import models

class Tag(models.models):
    title = models.TextField()

    def __str__(self):
        return self.title

class Perspectives(models.models):

    title = models.TextField()
    description = models.TextField()
    upboat = models.IntegerField()
    downboat = models.IntegerField()
    tags = models.ManyToManyField(Tag, through="tag_p")

    def __str__(self):
        return self.title

class Events(models.models):

    title = models.TextField()
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField()
    description = models.TextField()
    tags = models.ManyToManyField(Tag, through="tag_e")

    def __str__(self):
        return self.title
