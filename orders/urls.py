from django.urls import path
from . import views

urlpatterns = [
    path("order_now/<str:model>", views.order_now, name="order_now"),
    path("order_cart", views.order_cart, name="order_cart")
]