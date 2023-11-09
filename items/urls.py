from django.urls import path
from . import views


urlpatterns = [
    path('', views.items, name='items' ),
    path('createitems/', views.items_forms, name='items_forms_create_update'),
    path('createitems/<int:id>', views.items_forms, name='items_forms_load'),
    path('deleteitems/<int:id>', views.delitems, name='deleteitems'),    
  
]
