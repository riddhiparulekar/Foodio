from django.shortcuts import render,redirect
from .models import Items
from .forms import ItemForm
# Create your views here.

def items(request):
    data=Items.objects.all() #ORM 
    return render(request , 'items/items.html',{'items':data})

def items_forms(request, id=0):
    if request.method == "GET":
        if id == 0:
            items_form=ItemForm()
        else:
            data = Items.objects.get(id=id)
            items_form=ItemForm(instance=data)
        return render(request,'items/items_form.html', {"i_items": items_form})
    if request.method == "POST":
        if id == 0:
            print('teat 1')
            items_form=ItemForm(request.POST,request.FILES)
        else:
            print('teat 2')
            data = Items.objects.get(id=id)
            items_form=ItemForm(request.POST,instance=data)
        if items_form.is_valid():
            print('teat 3')
            items_form.save()
        print('teat 4')
        print(items_form.errors)
        return redirect('items')
    return render(request,'items/items.html')

def delitems(request,id):
    data=Items.objects.get(id=id)
    data.delete()
    data=Items.objects.all() #ORM 
    return render(request , 'items/items.html',{'items':data})


