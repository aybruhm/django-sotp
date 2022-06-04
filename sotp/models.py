from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    totp = models.CharField(max_length=18, unique=True, null=True, blank=True)
    otp = models.IntegerField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=False, null=True, blank=True)
    
    def __str__(self):
        return "User: {} -> TOTP: {}, OTP: {}".format(self.user.username, self.totp, self.otp)
    
    class Meta:
        verbose_name_plural = "User SOTPs"
        db_table = "user_sotps"