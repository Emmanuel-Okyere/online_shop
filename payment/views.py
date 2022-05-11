"""Payment View.py"""
import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order

gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def payment_process(request):
    """Payment view"""
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id= order_id)
    total_cost = order.get_total_cost()
    if request.method =="POST":
        nonce = request.POST.get("payment_method_nonce", None)
        result = gateway.transaction.sale({
            "amount": f"{total_cost:.2f}",
            "payment_method_nonce":nonce,
            "options":{
                "submit_for_settlement":True
            }
        })
        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            return redirect("payment:done")
        else:
            return redirect("payment:canceled")
    else:
        client_token = gateway.client_token.generate()
        return render(request,"payment/process.html", {"client_token":client_token,
        "order":order})
def payment_done(request):
    """When payment goes through"""
    return render(request, "payment/done.html")

def payment_canceled(request):
    """Canceled payments"""
    return render(request, "payment/canceled.html")
