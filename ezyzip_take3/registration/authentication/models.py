from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.http import request
from django.db import models
from django.contrib import messages
# # Create your models here.
class studentinfo(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False,unique=True)
    rollno=models.IntegerField(unique=True,primary_key=True)
    email=models.EmailField(unique=True) 
    # Phone=models.CharField(max_length=10,unique=True)
    pass1=models.CharField(max_length=50, null=False, blank=False)
