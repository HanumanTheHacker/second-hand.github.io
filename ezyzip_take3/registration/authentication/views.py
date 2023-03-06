from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
# from .models import studentinfo
from django.contrib import messages
from django.contrib.auth import authenticate, login
#chandu ka import
from django.views.decorators.csrf import csrf_exempt
from authentication.models import studentinfo
# chandu ka import ends

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        rollno = request.POST['rollno']
        pass1 = request.POST['pass1']
        # print(name,email,rollno,pass1)
        
        # chandu ka code
        my_user=studentinfo(name=name,rollno=rollno,email=email,pass1=pass1)
        my_user.save()
        # return redirect('/index')
        #chandu ka code ends
        
        # my code
        # myuser = User.objects.create_user(name,email,rollno,pass1)
        # myuser.save()
        return HttpResponse("YOUR LOGGED IN")
        # my code ends
    
    
def signin(request):
    
    if request.method == "POST":
        username = request.POST['logname']
        pass1 = request.POST['logpass1']
        
        user = authenticate(request,username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            return HttpResponse("TRUE")
             
        else:
           return HttpResponse("FAKE")
    
    else:
        return render(request, 'index.html')
            
    # return render(request, "authentication/signin.html")