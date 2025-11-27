# accounting/admin.py

from django.contrib import admin
from .models import Account, Customer, Supplier, Product, Transaction, TransactionLine


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "user", "parent")
    list_filter = ("type", "user")
    search_fields = ("name", "user__email", "user__username")
    autocomplete_fields = ("user", "parent")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "phone", "province")
    list_filter = ("province", "user")
    search_fields = ("name", "phone", "province", "user__email", "user__username")
    autocomplete_fields = ("user",)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "contact_info")
    list_filter = ("user",)
    search_fields = ("name", "contact_info", "user__email", "user__username")
    autocomplete_fields = ("user",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "unit", "default_price")
    list_filter = ("unit", "user")
    search_fields = ("name", "unit", "user__email", "user__username")
    autocomplete_fields = ("user",)


class TransactionLineInline(admin.TabularInline):
    model = TransactionLine
    extra = 1
    autocomplete_fields = ("account", "customer", "supplier", "product")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "description", "reference", "created_at")
    list_filter = ("date", "user")
    search_fields = ("description", "reference", "user__email", "user__username")
    date_hierarchy = "date"
    autocomplete_fields = ("user",)
    inlines = [TransactionLineInline]


@admin.register(TransactionLine)
class TransactionLineAdmin(admin.ModelAdmin):
    list_display = (
        "transaction",
        "account",
        "debit",
        "credit",
        "customer",
        "supplier",
        "product",
        "quantity",
    )
    list_filter = ("account", "customer", "supplier", "product")
    search_fields = (
        "transaction__description",
        "account__name",
        "customer__name",
        "supplier__name",
        "product__name",
    )
    autocomplete_fields = ("transaction", "account", "customer", "supplier", "product")
