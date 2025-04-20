from django.db import models
from django.contrib.auth import get_user_model

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    reference = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    