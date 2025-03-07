from django.db import models
import uuid


class Driver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name
