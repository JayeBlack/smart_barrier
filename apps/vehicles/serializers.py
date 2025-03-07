# apps/vehicles/serializers.py
from rest_framework import serializers
from .models import Vehicle
from apps.drivers.models import Driver  # Adjust if Driver model differs


class VehicleSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=Driver.objects.all())

    class Meta:
        model = Vehicle
        fields = ['plate_number', 'owner', 'make', 'model', 'year', 'color']
