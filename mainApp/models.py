from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Photo(models.Model):
    image = CloudinaryField("image")
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name if self.name != "" else "No caption"
