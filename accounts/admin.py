from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "nickname",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("nickname",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("nickname",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
