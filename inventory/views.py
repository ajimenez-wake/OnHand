from django.http import HttpResponse
from inventory.models import Camera

from django.views import generic

class CameraListView(generic.ListView):
    model = Camera
    template_name = 'camera/camera_list.html'
    context_object_name = 'cameras'
