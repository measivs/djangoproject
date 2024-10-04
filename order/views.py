from django.http import HttpResponse

orders = [
    {'id': 1,
     'product_name': 'Chic Dangle Earrings',
     'quantity': 2,
     'total_price': 100.00},
    {'id': 2,
     'product_name': 'Bohemian Layered Necklace',
     'quantity': 1,
     'total_price': 77.99},
    {'id': 3,
     'product_name': 'Elegant Rose Gold Ring',
     'quantity': 3,
     'total_price': 135.00},
    {'id': 4,
     'product_name': 'Charming Beaded Bracelet',
     'quantity': 4,
     'total_price': 320.00},
    {'id': 5,
     'product_name': 'Elegant Dress Watch',
     'quantity': 1,
     'total_price': 150.00},
]

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
