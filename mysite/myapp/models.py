from django.db import models

# Create your models here.
class SensorData(models.Model):
    timestamp = models.DateTimeField()
    waterlevel = models.FloatField()
    
    # Add more fields as needed