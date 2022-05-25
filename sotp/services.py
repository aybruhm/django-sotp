import pyotp

# Django Imports
from django.conf import settings


class GenerateSOTP:
    """
    This class generates a random base32 string and uses it to generate a one time password
    """
    
    @staticmethod
    def generate_otp():
        # Generate a random string of 32 characters
        secret = pyotp.random_base32(length=6)    
        
        # Parse the secret to an OTP and set an interval of 86400 ms 
        totp = pyotp.TOTP(secret, interval=settings.SOTP_MILLI_SECONDS)
        
        # Generate the OTP
        OTP = totp.now()
        
        # Secure TOTP and OTP payload
        payload = {
            "totp": secret,
            "OTP": OTP
        }
        
        return payload