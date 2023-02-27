from django.shortcuts import render, get_object_or_404, redirect
from item.models import Category, Item, Cart
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm,EditItemForm
# Create your views here.
def items(request):
    items = Item.objects.filter(is_sold = False)
    query = request.GET.get('query','')
    category_id= request.GET.get('catagory',0)
    categories = Category.objects.all()
    if query:
        items = items.filter(name__icontains=query)
    
    if category_id:
        items = items.filter(catagory_id=category_id)

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'catagory_id': int(category_id),
    } )

def detail(request, id):
    item= get_object_or_404(Item, id=id)
    related_item=Item.objects.filter(category=item.category,is_sold=False).exclude(id=id)[0:3]
    context={
        'item':item,
        'related_item':related_item
    }
    return render(request, 'item/detail.html',context)

@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit = False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', id=item.id)
    else:
        form = NewItemForm()
    context = {
        'form' : form,
        'title': 'New Item'
    }
    return render(request, 'item/form.html',context)

@login_required
def delete(request, id):
    item = get_object_or_404(Item, id=id, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

@login_required
def edit(request, id):
    item = get_object_or_404(Item, id=id, created_by=request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            
            form.save()

            return redirect('item:detail', id=item.id)
    else:
        form = EditItemForm(instance=item)
    
    context = {
        'form' : form,
        'title': 'Edit Item'
    }
    return render(request, 'item/form.html',context)

from django.shortcuts import get_object_or_404, redirect

def add_to_cart(request, id):
    item = get_object_or_404(Item, id=id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, item=item, defaults={'quantity': 1})
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('item:view_cart')

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    context = {'cart_items': cart_items}
    return render(request, 'item/cart.html', context)
