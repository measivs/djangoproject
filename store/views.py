import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse

from .data import items
from .models import Category, Product


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

def category_info(request):
    categories = Category.objects.values('id', 'category_name', 'parent')
    return JsonResponse(list(categories), safe=False)

def product_info(reqeust):
    products = Product.objects.prefetch_related('categories')
    products_json = serializers.serialize('json', products)
    products_data = json.loads(products_json)
    return JsonResponse(products_data, safe=False)

