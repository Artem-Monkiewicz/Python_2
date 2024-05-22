from django.forms import Form, CharField, IntegerField, DecimalField, ChoiceField

from django.core.exceptions import ValidationError
from c_viewer.models import Country


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError("Value must be capitalized")
    
# class PastDateField(DateField):
#     def validate(self, value):
#         super().validate(value)
#         if value >= date.today():
#             raise ValidationError('Only past dates allowed')


class CountryForm(Form):
    name = CharField(max_length=500, validators=[capitalized_validator])
    region = ChoiceField(choices=Country.region_choices)
    population = IntegerField()
    population_density = DecimalField(decimal_places=2, max_digits=20)
    gdp = DecimalField(decimal_places=2, max_digits=20)
    gdp_per_capita = DecimalField(decimal_places=2, max_digits=20)
