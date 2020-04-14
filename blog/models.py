from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)
    thumbnails = models.ImageField(upload_to='images', blank=True,)
