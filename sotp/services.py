import pyotp

# Django Imports
from django.conf import settings
from sotp.models import UserSOTP


class GenerateSOTP:
    """
    This class generates a random base32 string and uses it to generate a one time password
    """
    
    @staticmethod
    def generate_otp(request):
        # Generate a random string of 32 characters
        secret = pyotp.random_base32()    
        
        # Parse the secret to an OTP and set an interval of 86400 ms 
        totp = pyotp.TOTP(secret, interval=settings.SOTP_MILLI_SECONDS)
        
        # Generate the OTP
        OTP = totp.now()
        
        # Secure TOTP and OTP payload
        payload = {
            "totp": secret,
            "OTP": OTP
        }
        
        # Add generated TOTP and OTP to user and save to database
        user_sotp = UserSOTP.objects.get(id=request.user.id)
        user_sotp.totp = payload["totp"]
        user_sotp.otp = payload["OTP"]
        user_sotp.save()
        
        return payload