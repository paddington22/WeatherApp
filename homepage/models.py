from django.db import models

# Create your models here.
class Devices(models.Model):
    last_query = models.CharField(max_length=100, null=True, verbose_name='Введите название города')

    def __str__(self):
        return str(self.id)


class QueryHistory(models.Model):
    device_id = models.ForeignKey(Devices, on_delete=models.CASCADE)
    query = models.CharField(max_length=100)
