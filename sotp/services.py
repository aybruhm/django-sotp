# Library Imports
import pyotp

# Django Imports
from django.core.mail import send_mail
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
        user_sotp = UserSOTP.objects.get_or_create(
            user=get_user_model().objects.get(email=user_email),
            totp = payload.get("totp"), otp = payload.get("OTP")
        )
        
        # Send email to user
        self.send_otp_email(
            otp_code=user_sotp[0].otp,
            user_email=user_email
        )
        
        # Run scheduler to clear user *OTP after interval has elapsed
        run_scheduler(user_email=user_email)
        
        return payload
   
   
    @classmethod
    def send_otp_email(self, otp_code:int, user_email:str):
        """
        > Send an email to the user with the OTP code
        
        :param otp_code: The OTP code that was generated for the user
        :type otp_code: int
        :param user_email: The email address of the user
        :type user_email: str
        :return: True
        """
        
        send_mail(
            'Confirm OTP',
            'Use this secured OTP to authenticate your account\nOTP: {}'.format(otp_code),
            settings.SOTP_FROM_EMAIL,
            [user_email],
            fail_silently=False,
        )
        
        return True
    
