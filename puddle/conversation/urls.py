from django.urls import path

from . import views

app_name='conversation'

urlpatterns = [
    path('new/<int:id>/', views.new_conversation, name='new_conversation'),
    path('',views.inbox,name="inbox"),
    path('<int:id>/', views.detail,name='detail'),
]