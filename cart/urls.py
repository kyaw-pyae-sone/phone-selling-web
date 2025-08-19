from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_cart, name="view_cart"),
    path("add_to_cart/<str:model>", views.add_to_cart, name="add_to_cart"),
]
