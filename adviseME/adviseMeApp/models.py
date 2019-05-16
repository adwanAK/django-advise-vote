from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text= models.CharField(max_length=500)


class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    vote = models.IntegerField(default=0)

    class Meta:
        ordering = ['-vote']
