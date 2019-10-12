from django.db import models
from django.urls import reverse
# Create your models here.
# class Topic(models.Model):
#     top_name = models.CharField(max_length = 264,unique = True)
#
#     def __str__(self):
#         return self.top_name
#
# class Webpage(models.Model):
#     topic = models.ForeignKey(Topic,on_delete=models.PROTECT)
#     name = models.CharField(max_length = 264,unique = True)
#     url = models.URLField(unique = True)
#
#     def __str__(self):
#         return self.name
#
# class AccessRecord(models.Model):
#     name = models.ForeignKey(Webpage,on_delete=models.PROTECT)
#     date = models.DateField()
#     def __str__(self):
#         return str(self.date)

class School(models.Model):
    name = models.CharField(max_length = 264)
    principal = models.CharField(max_length = 264)
    location = models.CharField(max_length = 264)
    def get_absolute_url(self):
        return reverse("first_app:detail",kwargs={'pk':self.pk})
    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length = 264)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,on_delete=models.PROTECT,related_name='students')
    def __str__(self):
        return self.name
