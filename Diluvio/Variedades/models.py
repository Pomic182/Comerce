from django.db import models

class Variety(models.Model):
    name = models.CharField(max_length=20)
    appearance = models.CharField(max_length=200)
    smell = models.CharField(max_length=200)
    taste = models.CharField(max_length=200)
    marriage = models.CharField(max_length=200)
    ibu = models.FloatField()

