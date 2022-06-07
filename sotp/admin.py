from django.contrib import admin
from sotp.models import UserSOTP


@admin.register(UserSOTP)
class UserSOTPAdmin(admin.ModelAdmin):
    list_display = ("user", "totp", "otp",)
    
    