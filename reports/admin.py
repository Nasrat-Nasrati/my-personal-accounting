# reports/admin.py

from django.contrib import admin
from .models import SavedReport


@admin.register(SavedReport)
class SavedReportAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "user", "created_at")
    list_filter = ("type", "user", "created_at")
    search_fields = ("name", "type", "user__username", "user__email")
    autocomplete_fields = ("user",)

    readonly_fields = ("created_at",)

    fieldsets = (
        (None, {
            "fields": ("user", "name", "type", "filters", "created_at")
        }),
    )
