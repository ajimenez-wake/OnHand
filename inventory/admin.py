from django.contrib import admin

from .models import Camera
from .models import CameraLens


# Modify the display of the models.
class ElectronicView_1(admin.ModelAdmin):
    list_display = ['manufacturer', 'model', 'serial_number']

admin.site.register(Camera, ElectronicView_1)
admin.site.register(CameraLens, ElectronicView_1)
