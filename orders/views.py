from django.shortcuts import render, redirect
from dashboard.models import Phone
from .models import Order, OrderDetail
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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

        form = OrderForm()

    return render(request, "orders/index.html", {"order_items" : order_items, "grand_total" : order_items[0]["total"], "form" : form})

@login_required
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

    order["grand_total"] = grand_total

    print(order)

    context = {
        "order_items" : order_items,
        "grand_total" : grand_total
    }

    return render(request, "orders/index.html", context)


def purchase(request):

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # model save
            order = request.session.get("order", {})
            model_instance = form.save(commit=False)

            model_instance.grand_total = order["grand_total"]
            print(request.user)
            model_instance.user_name = request.user

            model_instance.save()

            # reduce quantity & order_detail
            for each in order["items"]:
                try:
                    phone = Phone.objects.get(model_name = each["model"])
                    wanted_qty = each["quantity"]

                    if not wanted_qty > phone.instock:
                        phone.instock -= wanted_qty
                        phone.save()
                        print("update successfully")

                    order_id = Order.objects.get(transaction_id = form.cleaned_data["transaction_id"])

                    OrderDetail.objects.create(order_id=order_id, phone_model = phone, quantity = wanted_qty, price = each["price"])

                    print(OrderDetail.objects.get(order_id=order_id))

                except Phone.DoesNotExist:
                    print("Phone does not exists")      

            # print(order["items"][0]["model"])        

    return redirect("home") 