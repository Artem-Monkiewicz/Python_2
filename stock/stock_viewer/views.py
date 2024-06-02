from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.shortcuts import render

from .forms import SignUpForm, StockForm, TransactionForm
from .models import Stock, Profile, Transactions

# Create your views here.


def hello(request):
    return HttpResponse("<h1>Hello, World!</h1>")


class SignUpView(CreateView):
    template_name = "form.html"
    form_class = SignUpForm
    success_url = reverse_lazy("hello")


class StocksView(PermissionRequiredMixin, ListView):
    template_name = "list.html"
    model = Stock
    permission_required = "stock_viewer.view_stock"

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        profile.no_clicks += 1
        profile.save()
        return super().get(request, args, kwargs)


class StockAddView(PermissionRequiredMixin, CreateView):
    form_class = StockForm
    template_name = "form.html"
    success_url = reverse_lazy("index")
    permission_required = "stock_viewer.add_stock"


class StockUpdateView(PermissionRequiredMixin, UpdateView):
    model = Stock
    template_name = "form.html"
    form_class = StockForm
    success_url = reverse_lazy("index")
    permission_required = "stock_viewer.update_stock"


class IsSuperUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class StockDeleteView(IsSuperUserMixin, DeleteView):
    model = Stock
    template_name = "delete.html"
    success_url = reverse_lazy("index")

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super().post(request, *args, **kwargs)


def cust_403(request, exception):
    return render(request, "403.html")


class TransactionsView(PermissionRequiredMixin, ListView):
    template_name = "list_transaction.html"
    model = Transactions
    permission_required = "stock_viewer.view_transactions"


class TransactionAddView(PermissionRequiredMixin, CreateView):
    form_class = TransactionForm
    template_name = "form.html"
    success_url = reverse_lazy("t_list")
    permission_required = "stock_viewer.add_transactions"


class TransactionsUpdateView(PermissionRequiredMixin, UpdateView):
    model = Transactions
    template_name = "form.html"
    form_class = TransactionForm
    success_url = reverse_lazy("t_list")
    permission_required = "stock_viewer.update_transaction"

class TransactionDeleteView(IsSuperUserMixin, DeleteView):
    model = Transactions
    template_name = "delete.html"
    success_url = reverse_lazy("t_list")