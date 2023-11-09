from django.db import models
from items.models import Items
from django.contrib.auth.models import User
# Create your models here.

class Bookorders(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    item_id=models.ForeignKey(Items,on_delete=models.CASCADE)
    bookingdate= models.DateTimeField()
    quantity=models.IntegerField()
    total_cost=models.FloatField(null=True,blank=True)
    booking_status= models.BooleanField()
    # delivery_datetime= models.DateTimeField()
    def __str__(self):
        return str(self.id)