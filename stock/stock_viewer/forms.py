from django.db.transaction import atomic
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import Stock, Profile


class StockForm(ModelForm):
    class Meta:
        model = Stock
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
