from django.urls import path
from .views import get_products,get_mens

urlpatterns = [
    path('', get_products, name="get_products"),
    path('mens/', get_mens, name="get_mens"),

]