from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate, login

# Sotp Imports
from sotp.models import UserSOTP
from sotp.services import GenerateSOTP


User = get_user_model()
generate_otp = GenerateSOTP()


def redirect_to_register_page(request):
    return redirect("example:register-page")


def register_page(request):
    
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Creates user and save to database
        user = User.objects.create(
            firstname=firstname, lastname=lastname,
            email=email, password=password
        )
        user.set_password(password)
        user.save()
        
        # Generate otp code for user
        generate_otp(user_id=user.id)
        
        return redirect("login-page")
    
    return render(request, "example/sign-up.html")


def login_page(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Validate the user credentials
        user = authenticate(username=username, password=password)
        
        # Log the user in :
        # - if the user is exists 
        # - redirect back to the login page if the user doesn't
        if user is not None:
            login(request, user)
            return redirect("welcome-page")
        
        else:
            return redirect("login-page")
    
    return render(request, "example/login.html")


def confirm_otp_page(request):
    
    if request.method == "POST":
        otp = request.POST.get("otp-code")
        email = request.POST.get("email")
        
        # Get user
        user = User.objects.get(email=email)
        
        # Validate the user otp
        if otp == UserSOTP.objects.get(user=user).otp:
        
            # Log the user in :
            # - if the user is exists 
            # - redirect back to the login page if the user doesn't
            if user is not None:
                login(request, user)
                return redirect("welcome-page")
        
        else:
            return redirect("confirm-otp-page")

    return render(request, "example/confirm-otp.html")    


def welcome_page(request):
    user = User.objects.get(id=request.user.id)
    return render(request, "example/welcome.html", {"username": user.username})