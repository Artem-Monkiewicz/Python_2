from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import Stock


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        exclude = []

    def save(self, commit=True):
        self.instance.is_active = True
        return super().save(commit)
