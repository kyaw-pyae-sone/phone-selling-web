from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Phone

# Create your models here.

class ReviewModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.phone} - {self.created_at}"
