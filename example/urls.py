from django.urls import path
from example.views import register_page, login_page, confirm_otp_page, welcome_page


app_name = "example"


urlpatterns = [
    path("register/", register_page, name="register-page"),
    path("login/", login_page, name="login-page"),
    path("confirm-otp/", confirm_otp_page, name="confirm-otp-page"),
    path("welcome/", welcome_page, name="welcome-page")
]