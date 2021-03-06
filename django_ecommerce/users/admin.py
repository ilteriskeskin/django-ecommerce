from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "is_staff",
    ]

    add_fieldsets = (
        (
            "Username and Email",
            {
                "fields": (
                    "username",
                    "email",
                ),
            },
        ),
        (
            "Password",
            {
                "fields": ("password1", "password2"),
            },
        ),
        (
            "Contact Information",
            {"fields": ("phone_number",)},
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
