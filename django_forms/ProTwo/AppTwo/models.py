from django.db import models

# Create your models here.
class User(models.Model):
    fName = models.CharField(max_length = 100)
    lName = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    def __str__(self):
        return self.email
