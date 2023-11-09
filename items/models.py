from django.db import models

# Create your models here.
class Items(models.Model):
    item_name= models.CharField(max_length=100)
    item_price= models.IntegerField()
    item_description= models.CharField(max_length=100)
    item_isveg= models.BooleanField()
    item_img = models.ImageField(upload_to='static/photos/',default=None)

    def __str__(self):
        return self.item_name