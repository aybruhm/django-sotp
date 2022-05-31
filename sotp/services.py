from django.http import HttpRequest
import pyotp

# Django Imports
from django.conf import settings

# Apps Imports
from sotp.helpers.schedulers import run_scheduler
from sotp.models import UserSOTP


class GenerateSOTP:
    """
    This class generates a random base32 string 
    and uses it to generate a one time password
    """
    
    @staticmethod
    def generate_otp(user_id:int):
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
        user_sotp = UserSOTP.objects.get(id=user_id)
        user_sotp.totp = payload["totp"]
        user_sotp.otp = payload["OTP"]
        user_sotp.save()
        
        # Run scheduler to clear user *OTP after interval has elapsed
        run_scheduler(user_id=user_id)
        
        return payload
    