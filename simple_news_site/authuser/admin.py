from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

from .models import MyUser

# @admin.register(MyUser)
# class UserAdmin(BaseUserAdmin):
#     fieldsets = BaseUserAdmin.fieldsets + (
#         (None, {'fields': ('group', )}),
#     )
#     # fieldsets = BaseUserAdmin.fieldsets + (
#     #     (None, {'fields': ('group', 'password')}),
#     #     ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth')}),
#     #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#     #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     # )
#     filter_horizontal = ()
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
#     list_filter = ()
#     list_display = ('email', 'group', 'first_name', 'last_name', 'date_of_birth', 'is_staff')
#     search_fields = ('email', 'group', 'last_name', 'is_staff', 'is_active')
#     ordering = ('created',)

admin.site.register(MyUser)
