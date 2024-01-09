from django.db import models
from datetime import datetime

# Create your models here.
class Home(models.Model):
    name=models.CharField(max_length=50,)
    designation=models.CharField(max_length=100)
    short_about=models.TextField(max_length=500,blank=True)
    photo=models.ImageField(upload_to='images/')
    datetime=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.name