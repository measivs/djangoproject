from django.http import HttpResponse

items = [
    {'id': 1,
     'name': 'Chic Dangle Earrings',
     'description': 'These elegant dangle earrings feature a sleek gold finish and a delicate chain design that adds sophistication to any outfit.',
     'price': 50.00},
    {'id': 2,
     'name': 'Bohemian Layered Necklace',
     'description': 'This stunning layered necklace showcases colorful beads and a charming pendant, perfect for adding a free-spirited flair to your wardrobe.',
     'price': 77.99},
    {'id': 3,
     'name': 'Elegant Rose Gold Ring',
     'description': 'This timeless rose gold ring features a delicate twist pattern, making it an ideal accessory for stacking or wearing solo.',
     'price': 45.00},
    {'id': 4,
     'name': 'Charming Beaded Bracelet',
     'description': 'This delightful beaded bracelet features a vibrant mix of colors and a stretch design, perfect for layering or wearing alone to brighten up any outfit.',
     'price': 80.00},
    {'id': 5,
     'name': 'Elegant Dress Watch',
     'description': 'This classic dress watch features a sleek stainless steel case, a minimalist dial with subtle hour markers, and a genuine leather strap, making it the perfect accessory for any formal occasion.',
     'price': 150.00},
]

def product_list(request):
    prdct_list = "<h1>List of Products</h1><ul>"
    for item in items:
        prdct_list += f"<li><a href='/store/{item['id']}'>{item['name']}</a> - ${item['price']}</li>"
    prdct_list += "</ul>"
    return HttpResponse(prdct_list)

def product_detail(request, product_id):
    product = next((item for item in items if item['id'] == product_id), None)
    if product:
        return HttpResponse(f"<h1>Details of {product['name']}</h1><p>{product['description']}</p><p>Price: ${product['price']}</p>")
    else:
        return HttpResponse("<h1>Product not found</h1>")
