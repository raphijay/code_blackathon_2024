import datetime
from django.db import models

class Tags(models.Model):
    title = models.TextField()
    in_use = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Perspectives(models.Model):

    title = models.TextField()
    description = models.TextField()
    upboat = models.IntegerField()
    downboat = models.IntegerField()
    year = models.IntegerField()
    tags = models.ManyToManyField(Tags, through="tag_p")

    def __str__(self):
        return self.title

class Events(models.Model):

    title = models.TextField()
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField()
    description = models.TextField()
    tags = models.ManyToManyField(Tags, through="tag_e")

    def __str__(self):
        return self.title

class Tag_P(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    perspective = models.ForeignKey(Perspectives, on_delete=models.CASCADE)

class Tag_E(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)