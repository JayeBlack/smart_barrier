# apps/vehicles/models.py
from django.db import models
import uuid


class Vehicle(models.Model):
    plate_number = models.CharField(max_length=20, primary_key=True)
    owner = models.ForeignKey('drivers.Driver', on_delete=models.CASCADE, related_name='vehicles')
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.plate_number} - {self.make} {self.model}"
