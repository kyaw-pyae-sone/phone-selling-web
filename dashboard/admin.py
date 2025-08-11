from django.contrib import admin
from .models import Phone

# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("brand", "model_name", "instock", "ram", "storage", "price")
    list_filter = ("ram", "storage", "brand")
    search_fields = ("brand", "model_name")