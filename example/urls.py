from django.urls import path
from example.views import redirect_to_register_page, register_page, \
    login_page, confirm_otp_page, welcome_page, logout_user


app_name = "example"


urlpatterns = [
    path("", redirect_to_register_page, name="redirect_to_register_page"),
    path("register/", register_page, name="register-page"),
    path("login/", login_page, name="login-page"),
    path("confirm-otp/", confirm_otp_page, name="confirm-otp-page"),
    path("welcome/", welcome_page, name="welcome-page"),
    path("logout/", logout_user, name="logout_user")
]