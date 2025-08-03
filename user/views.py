from django.shortcuts import render
from django.views import View

# Create your views here.

# def render_login(request):
#     return render(request, "user/login.html")
#
# def render_register(request):
#     return render(request, "user/registration.html")
#
#
# def render_profile(request):
#     return render(request, "user/profile.html")

class Login(View):
    def get(self, request):
        return render(request, "user/login.html")

class Register(View):
    def get(self, request):
        return render(request, "user/registration.html")

class Profile(View):
    def get(self, request):
        return render(request, "user/profile.html")

