from django.urls import path
from . import views

urlpatterns = [
    path("add_review/<str:model>", views.add_review, name="add_review")
]
