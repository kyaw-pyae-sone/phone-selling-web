from django.shortcuts import render
from .forms import UserRegistrationForm

def register(request):
    if request.method == "POST":    
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, "user/login.html", {"user": user})
    form = UserRegistrationForm()
    return render(request, "user/registration.html", {"form": form})