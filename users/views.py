from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User


@require_http_methods(["GET"])
def pagenotfound(request, exception):
    return render(request,'pnf.html', status=404)
 
 
@require_http_methods(["GET"])
def servernotfound(request):
    return render(request,'snf.html', status=500)

# Create your views here.
@require_http_methods(["GET"])
def home(request):
    return render(request , 'home.html')

@require_http_methods(["GET"])
def about(request):
    return render(request , 'aboutus.html')


@require_http_methods(["GET","POST"])
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
@require_http_methods(["GET"])
def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required
@require_http_methods(["GET","POST"])
def signup(request):
    print('signup')
    if request.method =="POST":
        print('post')
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        emailid=request.POST.get('emailid')
        password=request.POST.get('password1')
        conf_password=request.POST.get('password2')
        if password != conf_password:
            messages.error(request,'Both Passwords do not match')
            return redirect('signup')

        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=emailid, password=password)
        user.save()
        print('saved')
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print('logged in')
            return redirect('home')
        else:
            messages.error(request,'Invalid login details')
    return redirect('login')
