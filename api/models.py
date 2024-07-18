from django.db import models

# Create your models here
class Statistic(models.Model):
    city = models.CharField(max_length=100)
    count = models.IntegerField()

