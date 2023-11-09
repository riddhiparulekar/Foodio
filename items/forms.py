from django import forms
from .models import Items

class ItemForm(forms.ModelForm):
    class Meta:
        model=Items
        fields=("item_name","item_price","item_description","item_isveg","item_img")
        labels={
            "item_name":"Item Name",
            "item_price":"Item Price",
            "item_description":"Item Description",
            "item_isveg":"veg/non-veg",
            "item_img":"Item image"
        }