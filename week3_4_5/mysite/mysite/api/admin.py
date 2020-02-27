from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from mysite.api.models import MyUser, Profile


@admin.register(MyUser)
class MyAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department')