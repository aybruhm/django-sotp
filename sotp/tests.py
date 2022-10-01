# Native Imports 
from typing import Tuple
import pyotp

# Django Imports
from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model as User

# Own Imports
from sotp.models import UserSOTP


class GenerateSOTPTestCase(TestCase):
    """
    Test case to generate a secured one-time password
    """
    
    def setUp(self) -> None:
        self.user = User().objects.get_or_create(
            first_name="Abram",
            last_name="Israel",
            email="abram@email.com",
            username="abram",
            password="someawfully-strong_password2022"
        )[0]
        self.user_sotp =  UserSOTP.objects.get_or_create(
            user=self.user
        )[0]
        
    @property
    def generate_otp(self) -> Tuple[str, str]:
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
        return payload["totp"], payload["OTP"]
    
    def test_generate_sotp_for_user(self):
        """
        Test case to ensure that the generated
        TOTP and OTP matches with the user's.
        """
        
        totp, otp = self.generate_otp
        
        user = self.user_sotp
        user.otp = otp
        user.totp = totp
        user.save(update_fields=["otp", "totp"])
        
        self.assertEqual(user.otp, otp)
        self.assertEqual(user.totp, totp)