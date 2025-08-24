from django.urls import path
from . import views

urlpatterns = [
    path("", views.render_home, name="home"),
    path("detail/<str:model>", views.render_detail, name="detail"),
]