from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required


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
            return redirect('home')
        else:
            messages.error(request,'Invalid login details')
    return render(request,'home.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')
