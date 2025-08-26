from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.conf import settings

################ Registration View #################

def signup(request):
    if request.method == "POST":    
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
            
    else:
        form = UserRegistrationForm()

    return render(request, "user/registration.html", {"form": form})

################ Registration View #################

################ Login View #################

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    return redirect("home")
                else:
                    form.add_error(None, "Invalid Email or Password")
            except User.DoesNotExist:
                form.add_error(None, "Invalid Email or Password")

            # if user.check_password(password):
            #     login(request, user)
            #     return redirect("user/profile")
            # else:
            #     form.add_error(None, "Invalid Email or Password")
    
    # if method is GET method, render login form
    else: 
        form = LoginForm()

    return render(request, "user/login.html", {"form" : form})
        

################ Login View #################

################ Profile View #################

def signout(request):
    return redirect("signin")

# @login_required
# def profile(request):
#     messages.info(request, "You have been successfully logged out!!!")
#     return render(request, "user/profile.html", {"user": request.user})


################ Profile View #################



