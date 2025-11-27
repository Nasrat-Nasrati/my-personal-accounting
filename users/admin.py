# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, OTPCode


# ==========================
# Custom User Admin
# ==========================
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ("email", "username", "is_email_verified", "is_staff", "is_superuser")
    list_filter = ("is_email_verified", "is_staff", "is_superuser")

    search_fields = ("email", "username")
    ordering = ("email",)

    # Fields displayed when editing a User
    fieldsets = (
        ("Login Info", {
            "fields": ("email", "password"),
        }),
        ("Personal Info", {
            "fields": ("username", "google_id"),
        }),
        ("Permissions", {
            "fields": ("is_active", "is_email_verified", "is_staff", "is_superuser", "groups", "user_permissions"),
        }),
        ("Important Dates", {
            "fields": ("last_login", "date_joined"),
        }),
    )

    # Fields displayed when creating a User
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "is_email_verified", "is_staff", "is_superuser"),
        }),
    )


# ==========================
# OTPCode Admin
# ==========================
@admin.register(OTPCode)
class OTPCodeAdmin(admin.ModelAdmin):
    list_display = ("user", "code", "created_at", "is_used")
    list_filter = ("is_used", "created_at")
    search_fields = ("user__email", "code")

    readonly_fields = ("created_at",)

    fieldsets = (
        (None, {
            "fields": ("user", "code", "is_used", "created_at")
        }),
    )
