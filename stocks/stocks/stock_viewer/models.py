from django.db import models
from django.db.models import Model, CharField, DecimalField

# Create your models here.


class Stock(Model):
    nazwa = CharField(max_length=500)
    kurs_obecny = DecimalField(decimal_places=2, max_digits=20)
    otawarcie = DecimalField(decimal_places=2, max_digits=20)
    min = DecimalField(decimal_places=2, max_digits=20)
    max = DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return f"{self.nazwa}"
