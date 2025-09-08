from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from phones.forms import ReviewForm
from dashboard.models import Phone
# Create your views here.

@login_required
def add_review(request, model):

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            phone = Phone.objects.get(model_name=model)
            review_form = form.save(commit=False)
            review_form.username = request.user
            review_form.phone = phone
            review_form.save()

    return redirect("detail", model=phone)