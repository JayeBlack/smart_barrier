# apps/checkpoints/serializers.py
from rest_framework import serializers
from .models import CheckpointLog
from apps.vehicles.models import Vehicle
from apps.officer_auth.models import Officer


class CheckpointLogSerializer(serializers.ModelSerializer):
    plate_number = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())
    officer = serializers.PrimaryKeyRelatedField(queryset=Officer.objects.all())

    class Meta:
        model = CheckpointLog
        fields = ['id', 'plate_number', 'officer', 'location', 'timestamp']
        extra_kwargs = {
            'id': {'read_only': True},
            'timestamp': {'read_only': True},
        }
