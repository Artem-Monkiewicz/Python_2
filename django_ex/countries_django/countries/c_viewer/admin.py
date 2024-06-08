from django.contrib import admin
from .models import Country


class CountryAdmin(admin.ModelAdmin):
    ordering = ["id"]
    list_display = [
        "id",
        "name",
        "region",
        "population",
        "population_density",
        "gdp",
        "gdp_per_capita"
    ]
    list_display_links = ["id", "name"]
    list_per_page = 20
    list_filter = ["region"]
    search_fields = ["name"]


admin.site.register(Country, CountryAdmin)
