from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import Phone

# Create your views here.

def render_home(request):

    phones = Phone.objects.all()[:8]
    latest_phones = Phone.objects.filter().order_by("-release_date")[:8]
    brands = Phone.objects.values_list("brand", flat=True).distinct()

    if request.user.username:
        print(request.user.username)
        print(request.user.email)
    else:
        print("User not exists")

    return render(request, "phones/phone_list.html", {"phones" : phones, "latest_phones" : latest_phones, "brands" : brands})


def render_detail(request, model):
    
    phone = Phone.objects.get(model_name=model)

    quantity_range = range(1, phone.instock + 1)

    return render(request, "phones/phone_detail.html", {"phone" : phone, "quantity_range" : quantity_range})