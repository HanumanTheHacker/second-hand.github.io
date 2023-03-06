from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Profile)
class Admin(admin.ModelAdmin):
    list_display = ['name','email','item','Description','price','Mobile_no','image']