from django.shortcuts import render

from django.views import generic
from .models import Camera

class CameraListView(generic.ListView):
    model = Camera
    template_name = 'cameras/camera_list.html'
    context_object_name = 'cameras'

class CameraDetailView(generic.DetailView):
    model = Camera
    template_name = 'cameras/camera_detail.html'
    
    # Override the get_context_data to return the context_object_name
    def get_context_data(self, **kwargs):

        # This is how to get the context dictionary
        context = super(CameraDetailView, self).get_context_data(**kwargs)

        # use the golfer object that was clicked by the user
        camera = self.get_object()

        # Use the golfer object to get the rest of the context
        context['camera'] = camera
        return context
