from django.db import models
from django.utils import timezone
# Create your models here.
class SensorData(models.Model):
    soil_moisture = models.FloatField()
    temperature = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Soil Moisture: {self.soil_moisture}, Temperature: {self.temperature}"

class IrrigationSchedule(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    water_amount = models.FloatField()  # Amount of water in liters

    def __str__(self):
        return f"Irrigation from {self.start_time} to {self.end_time}, Water: {self.water_amount}L"