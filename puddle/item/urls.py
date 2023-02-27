from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('items/', views.items,name='items'),
    path("items/<int:id>", views.detail , name="detail"),
    path('new/',views.new,name='new'),
    path('<int:id>/delete/',views.delete,name='delete'),
    path('<int:id>/edit/',views.edit,name='edit'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:id>/', views.add_to_cart, name='add_to_cart'),
]