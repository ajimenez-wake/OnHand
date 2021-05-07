from django.contrib import admin

from .models import Camera

# Modify the display of the models.
class ElectronicView_1(admin.ModelAdmin):
    list_display = ['manufacturer', 'model', 'serial_number']

admin.site.register(Camera, ElectronicView_1)
