from django.shortcuts import render, get_object_or_404
from item.models import Category, Item
# Create your views here.
def detail(request, id):
    item= get_object_or_404(Item, id=id)
    related_item=Item.objects.filter(category=item.category,is_sold=False).exclude(id=id)[0:3]
    context={
        'item':item,
        'related_item':related_item
    }
    return render(request, 'item/detail.html',context)