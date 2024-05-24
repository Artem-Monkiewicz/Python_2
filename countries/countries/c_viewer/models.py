from django.contrib.auth.models import User
from django.db.models import (
    Model,
    CharField,
    IntegerField,
    DecimalField,
    CASCADE,
    Model,
    OneToOneField,
    TextField,
)

# Create your models here.


class Country(Model):
    NA = "NORTHERN AMERICA"
    OC = "OCEANIA"
    EE = "EASTERN EUROPE"
    WE = "WESTERN EUROPE"
    LA = "LATIN AMER. & CARIB"
    BA = "BALTICS"
    AS = "ASIA (EX. NEAR EAST)"
    SA = "SUB-SAHARAN AFRICA"
    NE = "NEAR EAST"
    ID = "C.W. OF IND. STATES"
    NF = "NORTHERN AFRICA"
    region_choices = {
        (NA, "NORTHERN AMERICA"),
        (OC, "OCEANIA"),
        (EE, "EASTERN EUROPE"),
        (WE, "WESTERN EUROPE"),
        (LA, "LATIN AMER. & CARIB"),
        (BA, "BALTICS"),
        (AS, "ASIA (EX. NEAR EAST)"),
        (SA, "SUB-SAHARAN AFRICA"),
        (NE, "NEAR EAST"),
        (ID, "C.W. OF IND. STATES"),
        (NF, "NORTHERN AFRICA"),
    }
    name = CharField(max_length=500)
    region = CharField(max_length=500, choices=region_choices)
    population = IntegerField()
    population_density = DecimalField(decimal_places=2, max_digits=20)
    gdp = DecimalField(decimal_places=2, max_digits=20)
    gdp_per_capita = DecimalField(decimal_places=2, max_digits=20)


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    no_click = IntegerField()
