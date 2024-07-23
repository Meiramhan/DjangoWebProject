from django.urls import path
from . import views
from .views import send_order

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about', views.about, name='about'),
    path('add', views.add_shop, name='add'),
    path('send_order/<int:order_id>/', send_order, name='send_order')
]