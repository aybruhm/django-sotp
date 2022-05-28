# Django Imports
from django.contrib.auth import get_user_model

# SOTP Imports
from sotp.services import GenerateSOTP
from sotp.models import UserSOTP


User = get_user_model()
sotp = GenerateSOTP()


def remove_user_sotps(user:User):
    """
    It removes the user's SOTP.
    
    :param user: The user object
    :type user: User
    :return: True
    """
    user_sotp = UserSOTP.objects.get(id=user.id)
    user_sotp.totp = ""
    user_sotp.otp = ""
    user_sotp.save()
    return True


