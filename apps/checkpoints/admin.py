# apps/vehicles/admin.py
from django.contrib import admin
from .models import CheckpointLog

admin.site.register(CheckpointLog)