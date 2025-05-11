import uuid
# from django.contrib.gis.db import models as gis_models # REMOVED
from django.db import models

class Asset(models.Model):
    STATUS_CHOICES = [
        ('ok', 'OK'),
        ('issue', 'Issue'),
        ('unknown', 'Unknown'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True) # e.g., fire extinguisher, AED
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unknown')
    # location = gis_models.PointField(srid=4326) # SRID 4326 for WGS84 -- REPLACED
    latitude = models.FloatField(null=True, blank=True) # Added
    longitude = models.FloatField(null=True, blank=True) # Added
    owner = models.UUIDField(null=True, blank=True) # Assuming owner might be a user ID from another system or nullable

    def __str__(self):
        return f"{self.name} ({self.id})"

class Inspection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='inspections')
    status = models.CharField(max_length=10) # Could be 'ok', 'issue', or more detailed
    # For the 3-question checklist, we can store answers as JSON or individual fields
    # For simplicity, let's assume the overall status derived from checklist is stored in 'status'
    # question1_ok = models.BooleanField(default=True)
    # question2_ok = models.BooleanField(default=True)
    # question3_ok = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reporter = models.UUIDField(null=True, blank=True) # User ID of the reporter, optional

    def __str__(self):
        return f"Inspection for {self.asset.name} at {self.created_at}"

    class Meta:
        ordering = ['-created_at']