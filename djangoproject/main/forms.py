from .models import Shop, Order
from django.forms import ModelForm


class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'open']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'amount', 'shop']