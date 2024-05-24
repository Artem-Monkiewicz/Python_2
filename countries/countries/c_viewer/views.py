from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import CountryForm, SignUpForm
from .models import Country, Profile


class CountriesList(LoginRequiredMixin, ListView):
    template_name = "list.html"
    model = Country

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        profile.no_click += 1
        profile.save()
        return super().get(request, args, kwargs)


class UserClicksView(ListView):
    template_name = "List_usr.html"
    model = Profile


class CountriesCreateView(PermissionRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = CountryForm
    success_url = reverse_lazy("form")
    # permission_required =


class CountriesUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "form.html"
    form_class = CountryForm
    model = Country
    success_url = reverse_lazy("index")


class CountryDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "delete.html"
    model = Country
    success_url = reverse_lazy("index")


class SignUpView(CreateView):
    template_name = "form.html"
    form_class = SignUpForm
    success_url = reverse_lazy("index")
