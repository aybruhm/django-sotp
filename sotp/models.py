from django.db import models
from django.contrib.auth.models import get_user_model


User = get_user_model()


class UserSOTP(User):
    """Inherits the user model class to extend functionalities"""
    totp = models.CharField(unique=True, editable=False, null=True, blank=True)
    otp = models.IntegerField(max_length=6, editable=False, null=True, blank=True)
    
    def __str__(self):
        return "totp: {}, otp: {}".format(self.totp, self.otp)
    
    class Meta:
        abstract = True
        verbose_name_plural = "User SOTPs"
        db_table = "user_sotps"