from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    img =CloudinaryField('images')
    ima =CloudinaryField('images')
    ime =CloudinaryField('images')
    ig =CloudinaryField('images')
    im =CloudinaryField('images')
    
    def __str__(self):
        return self.title
    

    

