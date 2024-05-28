from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignUpForm, StockForm
from .models import Stock

# Create your views here.


def hello(request):
    return HttpResponse("<h1>Hello, World!</h1>")


class SignUpView(CreateView):
    template_name = "form.html"
    form_class = SignUpForm
    success_url = reverse_lazy("hello")


class StocksView(LoginRequiredMixin, ListView):
    template_name = "list.html"
    model = Stock


class StockAddView(LoginRequiredMixin, CreateView):
    form_class = StockForm
    template_name = "form.html"
    success_url = reverse_lazy("index")


class StockUpdateView(LoginRequiredMixin, UpdateView):
    model = Stock
    template_name = "form.html"
    form_class = StockForm
    success_url = reverse_lazy("index")


class StockDeleteView(LoginRequiredMixin, DeleteView):
    model = Stock
    template_name = "delete.html"
    success_url = reverse_lazy("index")

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super().post(request, *args, **kwargs)
