from django.db import models
from django.db.models import (
    DO_NOTHING,
    CharField,
    DecimalField,
    ForeignKey,
    DateField,
)
from django.contrib.auth.models import User

# Create your models here.


class Stock(models.Model):
    name = CharField(max_length=500)
    current_price = DecimalField(max_digits=30, decimal_places=5)
    open_price = DecimalField(max_digits=30, decimal_places=5)
    min_price = DecimalField(max_digits=30, decimal_places=5)
    max_price = DecimalField(max_digits=30, decimal_places=5)

    def __str__(self):  # Вид
        return f"{self.name}: {self.current_price}"

class Transactions (models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE)
    quantity = DecimalField(max_digits=30, decimal_places=5)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    no_clicks = models.IntegerField()
