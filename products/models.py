from django.db import models
from django.db.models import Avg

 

class Product(models.Model):
    CATEGORY_CHOICES=(
        ("MENS_TSHIRTS","Mens T-Shirts"),
        ("MENS_JEANS","Mens Jeans"),
        ("MENS_SHOES","Mens Shoes"),
        )
    name = models.CharField(max_length=254, default='')
    description = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    brand = models.CharField(max_length=50, default='')
    category=models.CharField(max_length=30,choices=CATEGORY_CHOICES, default="MENS_TSHIRTS")
    
    
    
    def __str__(self):
        return self.name