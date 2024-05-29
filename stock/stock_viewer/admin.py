from django.contrib import admin
from stock_viewer.models import Stock, Profile, Transactions

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "no_clicks"]


class StockAdmin(admin.ModelAdmin):
    list_display = ["name", "current_price"]


class TransactionAdmin(admin.ModelAdmin):
    list_display = ["stock", "quantity", "timestamp"]


admin.site.register(Stock, StockAdmin)
admin.site.register(Transactions, TransactionAdmin)
admin.site.register(Profile, ProfileAdmin)
