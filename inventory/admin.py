from django.contrib import admin

from .models import Camera
from .models import CameraLens


admin.site.register(Camera)
admin.site.register(CameraLens)
