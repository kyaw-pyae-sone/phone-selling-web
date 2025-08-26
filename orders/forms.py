from django import forms 
from .models import Order

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        exclude = ("order_status","user_name", "grand_total")