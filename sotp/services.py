# Native Imports Imports
import pyotp

# Django Imports
from django.conf import settings
from django.contrib.auth import get_user_model

# Apps Imports
from sotp.helpers.schedulers import run_scheduler
from sotp.models import UserSOTP


class GenerateSOTP:
    """
    This class generates a random base32 string 
    and uses it to generate a one time password
    """
    
    @classmethod
    def generate_otp(self, user_email:str):
        # Generate a random string of 32 characters
        secret = pyotp.random_base32()    
        
        # Parse the secret to an OTP and set an interval of 900 seconds 
        totp = pyotp.TOTP(secret, interval=settings.SOTP_TIME_EXPIRATION * 60)
        
        # Generate the OTP
        OTP = totp.now()
        
        # Secure TOTP and OTP payload
        payload = {
            "totp": secret,
            "OTP": OTP
        }
        
        # Add generated TOTP and OTP to user and save to database
        user_sotp, _ = UserSOTP.objects.get_or_create(
            user=get_user_model().objects.get(email=user_email)
        )
        user_sotp.totp = payload.get("totp")
        user_sotp.otp = payload.get("OTP")
        user_sotp.save(update_fields=["totp", "otp"])
        
        # Run scheduler to clear user *OTP after interval has elapsed
        run_scheduler(user_email=user_email)
        
        return payload
    
