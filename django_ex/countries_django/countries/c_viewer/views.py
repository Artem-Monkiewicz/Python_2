from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)

from .forms import CountryForm, SignUpForm
from .models import Country, Profile


class CountriesList(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    template_name = "list.html"
    model = Country
    permission_required = "c_viewer.view_country"

    # def get(self, request, *args, **kwargs):
    #     profile = Profile.objects.get(user=request.user)
    #     profile.no_click += 1
    #     profile.save()
    #     return super().get(request, args, kwargs)


class UserClicksView(ListView):
    template_name = "List_usr.html"
    model = Profile


class CountriesCreateView(PermissionRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = CountryForm
    success_url = reverse_lazy("form")
    permission_required = "c_viewer.add_country"


class StuffRequaredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class CountriesUpdateView(StuffRequaredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "form.html"
    form_class = CountryForm
    model = Country
    success_url = reverse_lazy("index")
    permission_required = "c_viewer.change_country"


class CountryDeleteView(StuffRequaredMixin, PermissionRequiredMixin, DeleteView):
    template_name = "delete.html"
    model = Country
    success_url = reverse_lazy("index")
    permission_required = "c_viewer.delete_country"

    def test_func(self):
        return super().test_func() and self.request.user.is_superuser


class SignUpView(CreateView):
    template_name = "form.html"
    form_class = SignUpForm
    success_url = reverse_lazy("index")
