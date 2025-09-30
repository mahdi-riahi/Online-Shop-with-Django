from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # add_fieldsets = None
    # fieldsets = None
    list_display = ('username', 'email',)
    ordering = ('email', )


admin.site.register(CustomUser, CustomUserAdmin)
