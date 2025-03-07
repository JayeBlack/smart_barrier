# apps/reports/models.py
from django.db import models
import uuid


class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    checkpoint = models.ForeignKey(
        'checkpoints.CheckpointLog',
        on_delete=models.CASCADE,
        related_name='reports'
    )
    officer = models.ForeignKey(
        'officer_auth.Officer',
        on_delete=models.CASCADE,
        related_name='reports'
    )
    findings = models.TextField(blank=True, null=True)  # e.g., "Driver warned for speeding"
    actions_taken = models.CharField(
        max_length=100,
        choices=[
            ('warning', 'Warning Issued'),
            ('arrest', 'Arrest Made'),
            ('ticket', 'Ticket Issued'),
            ('none', 'No Action Taken'),
        ],
        default='none'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'Draft'),
            ('submitted', 'Submitted'),
            ('reviewed', 'Reviewed'),
        ],
        default='draft'
    )

    def __str__(self):
        return f"Report {self.id} for Checkpoint {self.checkpoint_id}"
