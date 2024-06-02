from django.db.transaction import atomic
from django.forms import ModelForm, CharField, DecimalField
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Stock, Profile, Transactions


def is_not_negative(value):
    if value < 0:
        raise ValidationError("Price cannot be negative")


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"

    current_price = DecimalField(
        max_digits=30, decimal_places=5, validators=[is_not_negative]
    )
    open_price = DecimalField(
        max_digits=30, decimal_places=5, validators=[is_not_negative]
    )
    min_price = DecimalField(
        max_digits=30, decimal_places=5, validators=[is_not_negative]
    )
    max_price = DecimalField(
        max_digits=30, decimal_places=5, validators=[is_not_negative]
    )


class TransactionForm(ModelForm):
    class Meta:
        model = Transactions
        fields = "__all__"


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        exclude = []

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)
        profile = Profile(user=user, no_clicks=0)
        if commit:
            profile.save()
        return super().save(commit)
