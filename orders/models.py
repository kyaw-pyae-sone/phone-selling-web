from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Phone

# Create your models here.

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.CharField(
        max_length=100,
        choices = [
            ("cancel", "Cancel"),
            ("pending", "Pending"),
            ("confirm", "Confirm")
        ]
    )
    grand_total = models.FloatField()
    transaction_id = models.IntegerField
    address = models.TextField
    payment = models.CharField(
        max_length=100,
        choices=[
            ("kbz", "KBZ Pay"),
            ("cb", "CB Pay"),
            ("wave", "Wave Pay"),
            ("aya", "Aya Pay")          
        ],
        default="kbz"
    )
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id)


class OrderDetail(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    phone_model = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.order_id)