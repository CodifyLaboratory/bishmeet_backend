from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'last_name', 'first_name', 'age', 'gender', 'email', 'avatar',
    )