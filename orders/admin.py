from django.contrib import admin
from .models import Order, OrderDetail

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("transaction_id", "user_name", "order_status", "payment", "order_date")
    list_filter = ("order_status","payment")

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ("order_id", "phone_model", "quantity", "price")