from django.shortcuts import render
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth.models import User

################ Registration View #################

def register(request):
    if request.method == "POST":    
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, "user/login.html", {"user": user})
    form = UserRegistrationForm()
    return render(request, "user/registration.html", {"form": form})

################ Registration View #################

################ Login View #################

def login(request):
    if request.method == "POST":
        pass
    # if method is GET method, render login form
    else: 
        form = LoginForm()
        return render(request, "user/login.html", {"form" : form})
        

################ Login View #################
