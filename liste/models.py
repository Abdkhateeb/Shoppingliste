from django.db import models
from django.contrib.auth.models import User

class ShoppingItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Authentifizierung
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.name} ({self.quantity})"
