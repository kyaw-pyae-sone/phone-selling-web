from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import Phone

# Create your views here.

def render_home(request):

    phones = Phone.objects.all()

    if request.user.username:
        print(request.user.username)
        print(request.user.email)
    else:
        print("User not exists")

    return render(request, "phones/phone_list.html", {"phones" : phones})


def render_detail(request, model):
    
    phone = Phone.objects.get(model_name=model)

    quantity_range = range(1, phone.instock + 1)

    return render(request, "phones/phone_detail.html", {"phone" : phone, "quantity_range" : quantity_range})