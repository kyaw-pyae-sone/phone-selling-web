from statistics import quantiles
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from dashboard.models import Phone


# Create your views here.
def add_to_cart(request, model):

    if request.method == "POST":

        phone = get_object_or_404(Phone, model_name=model)

        quantity_str = request.POST.get("quantity")

        try :
            quantity_int = int(quantity_str)

            if quantity_int < 0 :
                return redirect("detail")

            if quantity_int > phone.instock :
                return redirect("detail")

        except (ValueError, TypeError):
            return redirect("detail")

        if "cart" not in request.session:
            request.session["cart"] = {} 

        cart = request.session["cart"]
        cart[model] = quantity_int
        request.session.modified = True

    return redirect("view_cart")

def view_cart(request):

    cart = request.session.get("cart", {})

    cart_items = []
    grand_total = 0

    for model_name, quantity in cart.items():

        try :
            phone = Phone.objects.get(model_name = model_name)
            item_total = phone.price * quantity
            grand_total += item_total

            cart_items.append({
                "phone" : phone,
                "quantity" : quantity,
                "item_total" : item_total
            })

        except Phone.DoesNotExist :
            pass

    context = {
        "cart_items" : cart_items,
        "grand_total" : grand_total
    }
    return render(request, "cart/cart.html", context)