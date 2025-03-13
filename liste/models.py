from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.quantity})"
