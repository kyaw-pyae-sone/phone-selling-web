from django.shortcuts import render
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, "user/login.html")

class Register(View):
    def get(self, request):
        return render(request, "user/registration.html")

class Profile(View):
    def get(self, request):
        return render(request, "user/profile.html")

