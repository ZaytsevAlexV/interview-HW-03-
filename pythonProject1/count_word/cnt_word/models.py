from django.db import models

class Result(models.Model):
    path_file = models.CharField(max_length=100)
    word = models.CharField(max_length=100)
    cnt = models.IntegerField()

