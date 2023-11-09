from django.shortcuts import render,redirect
from items.models import Items
from .models import Bookorders
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.

def bookings(request):
    data=Bookorders.objects.filter(booking_status=False)
    return render(request , 'bookings/bookings.html',{'orders':data})

def order_history(request):
    data=Bookorders.objects.filter(booking_status=True)
    return render(request , 'bookings/history.html',{'orders':data})

def createbooking(request,id):
    quantity=request.POST.get('quantity')
    total_cost=request.POST.get('final_cal')
    item_id=Items.objects.get(id=id)
    user=User.objects.get(id=request.user.id)
    booking_status=False
    booking_date=datetime.now()
    bookorder=Bookorders(booking_status=booking_status,bookingdate=booking_date,item_id=item_id,user_id=user,quantity=quantity,total_cost=total_cost)
    bookorder.save()
    return redirect('bookings')

def delbooking(request,id):
    data=Bookorders.objects.get(id=id)
    data.delete()
    return redirect('bookings')

def updatebooking(request,id):
    data=Bookorders.objects.get(id=id)
    data.booking_status=True
    data.save()
    return redirect('bookings')

def makeorder(request, id):
    data=Items.objects.get(id=id)
    return render(request,'bookings/makeorder.html',{'items':data})

