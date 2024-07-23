from django.contrib.auth.context_processors import auth
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Order, Shop
from .forms import ShopForm
import requests

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def add_shop(request):
    error = ''
    if request.method == 'POST':
         form = ShopForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('homepage')
         else:
             error = 'Ошибка'


    form = ShopForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add.html', data)


def send_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    if order.status == 'F':
        print(f"Order id: {order.id} Shop id: {order.shop.id}, Amount: {order.amount}")
        return JsonResponse({"message": "Orders details sent successfully"})
    else:
        return JsonResponse({"error": "Orders details sent are not successfully"}, status=400)


