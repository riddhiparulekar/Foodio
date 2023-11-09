from django.shortcuts import render,redirect
from django.contrib import auth,messages


# Create your views here.
def home(request):
    return render(request , 'home.html')

def about(request):
    return render(request , 'aboutus.html')

def login(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.error(request,'Invalid login details')
    return render(request,'home')
