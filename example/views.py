from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Sotp Imports
from sotp.models import UserSOTP
from sotp.services import GenerateSOTP


User = get_user_model()
otp = GenerateSOTP()


def redirect_to_register_page(request):
    return redirect("example:register-page")


def register_page(request):
    
    if request.user.is_authenticated:
        return redirect("example:welcome-page")
    
    else:
    
        if request.method == "POST":
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            
            # Creates user and save to database
            user = User.objects.create(
                first_name=firstname, last_name=lastname,
                username=username, email=email, password=password
            )
            user.set_password(password)
            user.save()
            
            # Generate otp code for user
            otp.generate_otp(user_email=user.email)
            
            return redirect("example:confirm-otp-page")
        
        return render(request, "example/sign-up.html")


def login_page(request):
    
    if request.user.is_authenticated:
        return redirect("example:welcome-page")
    
    else:
    
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
                return redirect("example:welcome-page")
            
            else:
                return redirect("example:login-page")
        
        return render(request, "example/login.html")


def confirm_otp_page(request):
    
    if request.user.is_authenticated:
        return redirect("example:welcome-page")
    
    else:
    
        if request.method == "POST":
            otp = request.POST.get("otp-code")
            email = request.POST.get("email") 
            
            # Get user
            user = User.objects.get(email=email)
            user_otp = UserSOTP.objects.get(user=user)
            
            # Validate the user otp
            if int(otp) == user_otp.otp:
                
                # Set the user verification to True
                user_otp.verified = True
                user_otp.save()
                
                messages.success(request, "Your account has been verified!")
                return redirect("example:login-page")
            
            else:
                messages.warning(request, "OTP isn't correct. Please try again.")
                return redirect("example:confirm-otp-page")

        return render(request, "example/confirm-otp.html")    


@login_required(login_url="/login/")
def welcome_page(request):
    user = User.objects.get(id=request.user.id)
    return render(request, "example/welcome.html", {"username": user.username})


@login_required(login_url="/login/")
def logout_user(request):
    logout(request)
    return redirect("example:login-page")