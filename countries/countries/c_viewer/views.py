from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CountryForm, SingUpForm
from .models import Country

class CountriesList(LoginRequiredMixin, ListView):
    template_name = "list.html"
    model = Country

class CountriesCreateView(LoginRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = CountryForm
    success_url = reverse_lazy("form")

class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('form')

class CountriesUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "form.html"
    form_class = CountryForm
    model = Country
    success_url = reverse_lazy("index")


class CountryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "delete.html"
    model = Country
    success_url = reverse_lazy("index")




