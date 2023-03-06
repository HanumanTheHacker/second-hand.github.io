from django.shortcuts import render,HttpResponse
from re import template
from django.views.generic import DetailView
from .models import Profile

def home(request):
        return render(request,"upload.html")
# Create your views here.
def ImageView(request):
    if request.method=='POST':
      name=request.POST.get('name')
      email=request.POST.get('email')
      item=request.POST.get('item')
      Description=request.POST.get('Description')
      price=request.POST.get('price')
      Mobile_no=request.POST.get('Mobile_no')
      image=request.FILES.get('image')
      my_user=Profile(name=name,email=email,item=item,Description=Description,price=price,Mobile_no=Mobile_no,image=image)
      my_user.save()
      print(my_user)
      
      # return HttpResponse("Done")
      return render(request,"upload.html")

      
    else:
        return HttpResponse("ERROR OCCURED")



def Display(request):
    if request.method == "GET":
        img = Profile.objects.all()
        return render(request,'display.html', {'profile_img':img})