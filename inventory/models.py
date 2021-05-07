from django.db import models

class Camera(models.Model):
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    sensor = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

class CameraLens(models.Model):
    manufacturer = models.CharField(max_length=50)
    minimum_focal_length = models.PositiveSmallIntegerField()
    maximum_focal_length = models.PositiveSmallIntegerField()
    model = models.CharField(max_length=50)
    mount = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
