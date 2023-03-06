from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False,null=True)
    email=models.EmailField(unique=True,null=True)
    item = models.CharField(max_length=200, blank=False,null=True)
    Description=models.CharField(max_length=200, blank=False,null=True)
    price=models.IntegerField(blank=False,null=True)
    Mobile_no = models.CharField(max_length=10, unique=True, null=True)
    image = models.ImageField(upload_to='img/%Y/%m/%d', blank=False,null=True)