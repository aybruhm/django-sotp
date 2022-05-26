from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSOTP(User):
    """Inherits the user model class to extend functionalities"""
    totp = models.CharField(max_length=18, unique=True, null=True, blank=True)
    otp = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return "totp: {}, otp: {}".format(self.totp, self.otp)
    
    class Meta:
        verbose_name_plural = "User SOTPs"
        db_table = "user_sotps"