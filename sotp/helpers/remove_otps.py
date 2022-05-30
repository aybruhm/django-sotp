# Django Imports
from django.contrib.auth import get_user_model
from django.http import HttpRequest

# SOTP Imports
from sotp.models import UserSOTP


User = get_user_model()


def remove_user_otp(request:HttpRequest):
    """
    It removes the user's SOTP.
    
    :param user: The user object
    :param user_id: The HttpRequest object
    :type user: User
    :return: True
    """
    user_sotp = UserSOTP.objects.get(id=request.user.id)
    user_sotp.totp = 0
    user_sotp.otp = 0
    user_sotp.save()
    return True


