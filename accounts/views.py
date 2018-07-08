from django.shortcuts import render


def get_home(request):
    return render(request,"index.html")
    
def login(request):
    return render(request, 'accounts/login.html')
    
def register(request):
    return render(request, 'accounts/register.html')