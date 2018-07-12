from .views import *
from django.urls import path



urlpatterns = [
    path('view',view_cart, name="view_cart"),
    path('add',add_to_cart, name="add_to_cart"),
    path('delete',delete_item, name="delete_item"),
 
]

