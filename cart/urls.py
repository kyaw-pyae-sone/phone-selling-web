from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.view_cart, name="view_cart"),
    path("add_to_cart/<str:model>", login_required(views.add_to_cart) , name="add_to_cart"),
]
