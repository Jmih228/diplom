from django.contrib import admin
from users.models import CustomUser, InviteCode


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_number', 'city', 'invite_code')
    list_filter = ('id', 'email', 'phone_number', 'city', 'invite_code')
    search_fields = ('id', 'email', 'phone_number', 'city', 'invite_code')


@admin.register(InviteCode)
class InviteCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'user')
    list_filter = ('id', 'value', 'user')
    search_fields = ('id', 'value', 'user')
