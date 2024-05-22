from django.shortcuts import render
from django.views.generic import FormView
from .forms import CountryForm


class CountriesCreateView(FormView):
    template_name = "form.html"
    form_class = CountryForm
