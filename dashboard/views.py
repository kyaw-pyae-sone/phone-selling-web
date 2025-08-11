from django.shortcuts import render, redirect
from .forms import PhoneForm
from .models import Phone

# Create your views here.

# get phones
def get_phone(request):
    phones = Phone.objects.all()
    return render(request, "dashboard/phones/list.html", {"phones" : phones})

# insert phone
def insert_phone(request):
    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_phone")
    else:
        form = PhoneForm()
    return render(request, "dashboard/phones/add_form.html", {"form" : form})

# update phone
def update_phone(request):
    pass

# delete phones
def delete_phone(request):
    pass