from django.db import models
from django.db.models import (
    DO_NOTHING,
    CharField,
    DecimalField,
)

# Create your models here.

class Stock(models.Model):
    name = CharField(max_length=500)
    current_price = DecimalField(max_digits=30, decimal_places=5)
    open_price = DecimalField(max_digits=30, decimal_places=5)
    min_price = DecimalField(max_digits=30, decimal_places=5)
    max_price = DecimalField(max_digits=30, decimal_places=5)

    def __str__(self): #Вид
        return f'{self.name}: {self.current_price}'
