# Django Imports
from django.contrib.auth import get_user_model

# SOTP Imports
from sotp.models import UserSOTP

# Third Party Imports
from django_apscheduler.models import DjangoJob


def remove_user_otp_and_job(**kwargs):
    """
    It removes the OTP from the database 
    for the user with the email address passed 
    in as a keyword argument
    
    :return: A boolean value.
    """
    user_sotp = UserSOTP.objects.get(
        user=get_user_model().objects.get(
            email=kwargs.get("email")
        )
    )
    user_sotp.totp = 0
    user_sotp.otp = 0
    user_sotp.save()
    
    # Removes user job from database
    DjangoJob.objects.get(id=kwargs.get("job_id")).delete()
    
    return True


