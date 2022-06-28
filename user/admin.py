from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User as UserModel
# Register your models here.


class UserAdmin(BaseUserAdmin):
    list_display = ("id", "username", "email",)
    list_display_links = ("username",)
    list_filter = ("username",)
    search_fields = ("username", "email",)

    fieldsets = (
        ("유저 정보", {"fields": ("username", "email", "password", "nickname", )}),
        ("권한", {"fields": ("is_active", "is_admin",)}),
        )

    filter_horizontal = []

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date',)
        else:
            return ('join_date', )

    inlines = [

        
    ]

admin.site.register(UserModel, UserAdmin)
