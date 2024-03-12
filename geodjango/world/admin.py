from django.contrib import admin
from .models import Settlement

@admin.register(Settlement)

class SettlementAdmin(admin.ModelAdmin):
   list_display=['day_measured', 'identifier', 'municipality', 'settlement', 'hours_of_service', 'supply_zone', 'is_atypical_condition']