from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import Phone

# Create your views here.

def render_home(request):

    phones = Phone.objects.all()

    return render(request, "phones/phone_list.html", {"phones" : phones})


def render_detail(request, model):
    
    phone = Phone.objects.get(model_name=model)

    quantity_range = range(1, phone.instock + 1)

    return render(request, "phones/phone_detail.html", {"phone" : phone, "quantity_range" : quantity_range})

def render_order(request, model):
    phones = Phone.objects.filter(model_name = model)

    if request.method == "POST":
        quantity = request.POST.get("quantity")

    context = {
        "phones" : phones,
        "quantity" : quantity
    }   

    return render(request, "orders/index.html", {"context" : context})