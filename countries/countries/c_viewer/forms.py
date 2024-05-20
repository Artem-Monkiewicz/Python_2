from django.forms import Form, CharField, IntegerField, DecimalField, ChoiceField

from c_viewer.models import Country


class Country(Form):
    name = CharField(max_length=500)
    region = ChoiceField(choices=Country.region_choices)
    population = IntegerField()
    population_density = DecimalField(decimal_places=2, max_digits=20)
    gdp = DecimalField(decimal_places=2, max_digits=20)
    gdp_per_capita = DecimalField(decimal_places=2, max_digits=20)
