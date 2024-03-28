from django import forms
from dz6app.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product', 'description', 'price', 'quantity', 'photo']