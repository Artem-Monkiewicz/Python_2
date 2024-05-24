from typing import Any
from django.forms import ModelForm, CharField, IntegerField, DecimalField, ChoiceField
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from .models import Country, Profile


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError("Value must be capitalized")


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = "__all__"

    name = CharField(max_length=128, validators=[capitalized_validator])
    region = ChoiceField(choices=Country.region_choices)
    population = IntegerField()
    population_density = DecimalField(max_digits=20, decimal_places=2)
    gdp = DecimalField(max_digits=20, decimal_places=2)

    def clean(self):
        result = super().clean()
        result["gdp_per_capita"] = result["gdp"] / result["population"]
        return result


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["username", "email"]

    def save(self, commit=True):
        self.instance.is_active = False
        user = super().save(commit)
        profile = Profile(user=user, no_click=0)
        if commit:
            profile.save()
        return user
