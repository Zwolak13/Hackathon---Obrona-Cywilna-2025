from django.contrib.gis import admin # Use GeoAdmin for PointField
from .models import Asset, Inspection

@admin.register(Asset)
class AssetAdmin(admin.OSMGeoAdmin): # OSMGeoAdmin provides a map widget
    list_display = ('name', 'category', 'status', 'location')
    list_filter = ('status', 'category')
    search_fields = ('name', 'id')

@admin.register(Inspection)
class InspectionAdmin(admin.ModelAdmin):
    list_display = ('asset', 'status', 'created_at', 'reporter')
    list_filter = ('status', 'created_at')
    search_fields = ('asset__name', 'reporter')
    autocomplete_fields = ['asset']