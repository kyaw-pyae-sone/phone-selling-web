from django.shortcuts import render

# Create your views here.

def render_login(request):
    render(request, "user/login.html")

def render_register(request):
    render(request, "user/register.html")


def render_profile(request):
    render(request, "user/register.html")