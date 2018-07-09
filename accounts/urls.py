from django.urls import path
from .views import login,register_buyer,logout,profile

urlpatterns = [
    path('login/',login, name="login"),
    path('register_buyer',register_buyer, name="register_buyer"),
    path('logout/',logout, name="logout"),
    path('profile/',profile, name="profile")
]