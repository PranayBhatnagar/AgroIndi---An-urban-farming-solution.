from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    optimal_temperature = models.FloatField()
    optimal_humidity = models.FloatField()

    def __str__(self):
        return self.name
