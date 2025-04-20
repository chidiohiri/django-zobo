from django import forms 
from .models import Product, Checkout

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'price', 'description', 'status'
        ]

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'price', 'description', 'status'
        ]

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        exclude = ('product', 'is_verified', 'total_amount')