from django.http import HttpResponse
from .data import orders

def order_list(request):
    ordr_list = "<h1>List of Orders</h1><ul>"
    for order in orders:
        ordr_list += f"<li><a href='/order/{order['id']}'>{order['product_name']}</li>"
    ordr_list += "</ul>"
    return HttpResponse(ordr_list)


def order_detail(request, order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    if order:
        return HttpResponse(f"<h1>Order Details</h1><p>Product: {order['product_name']}</p><p>Quantity: {order['quantity']}</p><p>Total Price: ${order['total_price']}</p>")
    else:
        return HttpResponse("<h1>Order not found</h1>")
