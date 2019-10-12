from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=264)
    length = models.PositiveIntegerField()
    release = models.PositiveIntegerField()
    def __str__(self):
        return self.title

class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone_no = models.PositiveIntegerField()
    def __str__(self):
        return self.first_name+' '+self.last_name
