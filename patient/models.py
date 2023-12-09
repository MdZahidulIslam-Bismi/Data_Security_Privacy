from django.db import models

# Create your models here.


class Patient(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    health_history = models.CharField(max_length=100)
