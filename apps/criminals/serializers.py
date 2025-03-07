# apps/criminals/serializers.py
from rest_framework import serializers
from .models import CriminalRecord
from apps.vehicles.models import Vehicle


class CriminalRecordSerializer(serializers.ModelSerializer):
    plate_number = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())

    class Meta:
        model = CriminalRecord
        fields = ['id', 'plate_number', 'status', 'notes']
        extra_kwargs = {
            'id': {'read_only': True},
        }
