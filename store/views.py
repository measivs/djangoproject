from django.http import HttpResponse, JsonResponse

from .data import items
from .models import Category, Product
import os

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
    categories_data = []
    categories = Category.objects.all()
    for category in categories:
        ctgrs_data = {
            'id': category.id,
            'category name': category.category_name,
            'parent': category.parent.id if category.parent else None,
        }
        categories_data.append(ctgrs_data)

    return JsonResponse(categories_data, safe=False)

def product_info(request):
    products_data = []
    products = Product.objects.all()
    for p in products:
        prdcts_data = {
            'product name': p.product_name,
            'image url': os.path.basename(p.product_image.name) if p.product_image else None,
            'categories': [{'id': category.id, 'name': category.category_name} for category in p.categories.all()],
        }
        products_data.append(prdcts_data)

    return JsonResponse(products_data, safe=False)
