from django.contrib import admin
from .models import Country


class CountryAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ['id', 'name', 'region', ]


# Register your models here.

admin.site.register(Country, CountryAdmin)
