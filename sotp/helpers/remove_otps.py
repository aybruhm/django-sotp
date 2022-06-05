# Django Imports
from django.contrib.auth import get_user_model

# SOTP Imports
from sotp.models import UserSOTP


User = get_user_model()


def remove_user_otp(**kwargs):
    """
    It removes the OTP from the database 
    for the user with the email address passed 
    in as a keyword argument
    
    :return: A boolean value.
    """
    user_sotp = UserSOTP.objects.get(
        user=User.objects.get(
            email=kwargs.get("email")
        )
    )
    user_sotp.totp = 0
    user_sotp.otp = 0
    user_sotp.save()
    
    return True


