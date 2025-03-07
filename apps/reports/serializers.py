# apps/reports/serializers.py
from rest_framework import serializers
from .models import Report
from apps.checkpoints.models import CheckpointLog
from apps.officer_auth.models import Officer


class ReportSerializer(serializers.ModelSerializer):
    checkpoint = serializers.PrimaryKeyRelatedField(queryset=CheckpointLog.objects.all())
    officer = serializers.PrimaryKeyRelatedField(queryset=Officer.objects.all())

    class Meta:
        model = Report
        fields = ['id', 'checkpoint', 'officer', 'findings', 'actions_taken', 'created_at', 'updated_at', 'status']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
