# apps/criminals/models.py
from django.db import models
import uuid

class CriminalRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plate_number = models.ForeignKey('vehicles.Vehicle', on_delete=models.CASCADE, related_name='criminal_records')
    status = models.CharField(max_length=50)  # e.g., "stolen", "wanted"
    notes = models.TextField()

    def __str__(self):
        return f"{self.plate_number} - {self.status}"