from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import Phone
from .forms import ReviewForm
from .models import ReviewModel
from dashboard.decorators import regular_user_required

# Create your views here.

@regular_user_required
def render_home(request):

    phones = Phone.objects.all()[:8]
    latest_phones = Phone.objects.filter().order_by("-release_date")[:8]
    brands = Phone.objects.values_list("brand", flat=True).distinct()

    return render(request, "phones/phone_list.html", {"phones" : phones, "latest_phones" : latest_phones, "brands" : brands})

@regular_user_required
def render_detail(request, model):
    
    phone = Phone.objects.get(model_name=model)
    quantity_range = range(1, phone.instock + 1)
    reviews = ReviewModel.objects.filter(phone = phone).order_by("-created_at")
    form = ReviewForm()

    return render(request, "phones/phone_detail.html", {"phone" : phone, "quantity_range" : quantity_range, "form" :form, "reviews" : reviews})