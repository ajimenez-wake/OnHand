from django.db import models
from django.templatetags.static import static

class Camera(models.Model):
    id = models.IntegerField(primary_key=True)
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    sensor = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    picture_url = models.CharField(default=static('cameras/images/default.png'), max_length=100)

    def __str__(self):
        return self.manufacturer + " " + self.model

    class Meta:
        verbose_name = "Camera"
