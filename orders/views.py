from django.shortcuts import render
from dashboard.models import Phone
# from django.contrib.auth.decorators import login_required

# Create your views here.
def order_now(request, model):

    if request.method == "POST":
        phone = Phone.objects.get(model_name = model)
        quantity = int(request.POST.get("quantity", 1))

        request.session["order"] = {}
        order = request.session["order"]
        order["items"] = [{
            "model" : phone.model_name,
            "quantity" : quantity,
            "price" : phone.price,
            "total" : phone.price * quantity
        }]

        order["grand_total"] = phone.price * quantity

        print(order)

        order_items = [{
            "phone": phone,
            "quantity": quantity,
            "total": phone.price * quantity
        }]

    return render(request, "orders/index.html", {"order_items" : order_items, "grand_total" : order_items[0]["total"]})

def order_cart(request):

    cart = request.session.get("cart", {})
    grand_total = 0
    order_items = []

    request.session["order"] = {}
    order = request.session["order"]
    order["items"] = []

    for item in cart.items():
        phone = Phone.objects.get(model_name=item[0])
        grand_total += phone.price * item[1]
        order["items"].append({
            "model" : phone.model_name,
            "price" : phone.price,
            "quantity" : item[1],
            "total" : phone.price  * item[1]
        })
        order_items.append({
            "phone" : phone,
            "quantity" : item[1],
            "total" : phone.price  * item[1]
        })

    print(order)

    context = {
        "order_items" : order_items,
        "grand_total" : grand_total
    }

    return render(request, "orders/index.html", context)