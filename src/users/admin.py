from django.contrib import admin
from .models import User, Role


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('last_login', 'date_joined',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass