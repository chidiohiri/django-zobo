from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, 
        choices=(
            ('In Stock', 'In Stock'), 
            ('Out of Stock', 'Out of Stock')
        ), 
        default='In Stock'
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name 

class Checkout(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    state = models.CharField(
        max_length=100, 
        choices=(
            ('Lagos', 'Lagos'), 
        )
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1) # amount of products cx is buying
    total_amount = models.PositiveIntegerField() # amount * product price 
    
    is_verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
