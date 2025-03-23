# apps/vehicles/admin.py
from django.contrib import admin
from .models import CriminalRecord

admin.site.register(CriminalRecord)