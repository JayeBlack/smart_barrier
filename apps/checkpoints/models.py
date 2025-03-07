# apps/checkpoints/models.py
from django.db import models
import uuid


class CheckpointLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plate_number = models.ForeignKey('vehicles.Vehicle', on_delete=models.CASCADE, related_name='checkpoints')
    officer = models.ForeignKey('officer_auth.Officer', on_delete=models.CASCADE, related_name='checkpoints')
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Checkpoint {self.id} - {self.plate_number}"
