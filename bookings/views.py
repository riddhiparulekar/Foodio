from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.conf.urls import handler500
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from items.models import Items
from .models import Bookorders

# Create your views here.

@login_required
@require_http_methods(["GET"])
def bookings(request):
    try:
        if request.user.username == 'admin':
            data=Bookorders.objects.filter(booking_status=False)
        else:
            data=Bookorders.objects.filter(booking_status=False, user_id=request.user.id)
        return render(request , 'bookings/bookings.html',{'orders':data})
    except Exception:
        return redirect(handler500)

@login_required
@require_http_methods(["GET"])
def order_history(request):
    try:
        if request.user.username == 'admin':
            data=Bookorders.objects.filter(booking_status=True)
        else:
            data=Bookorders.objects.filter(booking_status=True, user_id=request.user.id)

        return render(request , 'bookings/history.html',{'orders':data})
    except Exception:
        return redirect(handler500)

@login_required
@require_http_methods(["GET", "POST"])
def createbooking(request,id):
    try:
        quantity=request.POST.get('quantity')
        total_cost=request.POST.get('final_cal')
        item_id=Items.objects.get(id=id)
        user=User.objects.get(id=request.user.id)
        booking_status=False
        booking_date=datetime.now()
        bookorder=Bookorders(booking_status=booking_status,bookingdate=booking_date,item_id=item_id,user_id=user,quantity=quantity,total_cost=total_cost)
        bookorder.save()
        return redirect('bookings')
    except Exception:
        return redirect(handler500)


@login_required
@require_http_methods(["GET"])
def delbooking(request,id):
    try:
        data=Bookorders.objects.get(id=id)
        data.delete()
        return redirect('bookings')
    except Exception:
        return redirect(handler500)

@login_required
@require_http_methods(["GET"])
def updatebooking(request,id):
    try:
        data=Bookorders.objects.get(id=id)
        data.booking_status=True
        data.save()
        return redirect('bookings')
    except Exception:
        return redirect(handler500)

@login_required
@require_http_methods(["GET"])
def makeorder(request, id):
    try:
        data=Items.objects.get(id=id)
        return render(request,'bookings/makeorder.html',{'items':data})
    except Exception:
        return redirect(handler500)

