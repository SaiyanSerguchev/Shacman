from django.contrib import admin
from main.models import Truck
@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    pass
