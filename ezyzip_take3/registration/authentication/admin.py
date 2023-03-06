from django.contrib import admin
from .models import studentinfo

class Adminstudentinfo(admin.ModelAdmin):
    list_display= ['name','rollno','email','pass1']
# Register your models here.
admin.site.register(studentinfo,Adminstudentinfo)
# Register your models here.
