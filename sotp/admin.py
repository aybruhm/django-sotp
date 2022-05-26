from django.contrib import admin
from sotp.models import UserSOTP


@admin.register(UserSOTP)
class UserSOTPAdmin(admin.ModelAdmin):
    fields = ("user", "totp", "otp",)