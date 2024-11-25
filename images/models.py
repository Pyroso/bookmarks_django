from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='images')

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    
