from django.urls import path
from . import views


urlpatterns = [
    path('', views.bookings, name='bookings' ),
    path('createbookings/<int:id>', views.createbooking, name='createbookings'),
    path('deletebookings/<int:id>', views.delbooking, name='deletebookings'),
    path('makeorder/<int:id>', views.makeorder, name='makeorder'),
    path('updatebooking/<int:id>', views.updatebooking, name='updatebooking'),
    path('orderhistory', views.order_history, name='orderhistory'),


]
