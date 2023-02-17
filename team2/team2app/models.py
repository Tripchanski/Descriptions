from django.db import models

class Item(models.Model):
    title= models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)

class Description(models.Model):
    author = models.CharField(max_length=255, default = "User")
    description = models.TextField()


