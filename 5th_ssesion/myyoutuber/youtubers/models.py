from django.db import models

class youtubers(models.Model):
    channelname = models.CharField(max_length=100)
    creatorname = models.CharField(max_length=100)
    preference = models.IntegerField()
    onair = models.BooleanField()
    subscribers = models.IntegerField()
    link1 = models.TextField()
    link2 = models.TextField()
    link3 = models.TextField()


# Create your models here.
