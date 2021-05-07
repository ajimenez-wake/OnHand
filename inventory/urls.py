from django.urls import path
from . import views

urlpatterns = [
    path('', views.CameraListView.as_view(), name='camera_list_view'),
]