from django.urls import path
from . import views

urlpatterns = [
    path("phones/", views.get_phone, name = "get_phone"),
    path("phones/insert/", views.insert_phone, name="insert_phone"),
    path("phones/update/<str:model>", views.update_phone, name="update_phone"),
    path("phones/delete/<str:model>", views.delete_phone, name="delete_phone")
]