from django.db import models

class Camera(models.Model):
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    sensor = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.manufacturer + " " + self.model

    class Meta:
        verbose_name = "Camera"

class CameraLens(models.Model):
    manufacturer = models.CharField(max_length=50)
    minimum_focal_length = models.PositiveSmallIntegerField()
    maximum_focal_length = models.PositiveSmallIntegerField()
    model = models.CharField(max_length=50)
    mount = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)

    def __str__(self):
        return self.manufacturer + " " + self.model

    class Meta:
        verbose_name = "Camera Lens"
        verbose_name_plural = "Camera Lenses"
