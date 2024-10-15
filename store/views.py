from django.core.paginator import Paginator

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum, Max, Min, Avg, F

from .data import items
from .models import Category, Product
import os

def home(request):
    return HttpResponse('<h1>Welcome!</h1><p>Browse our products and enjoy easy shopping and quick ordering.</p>')

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
    categories = Category.objects.select_related('parent')
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
    products = Product.objects.prefetch_related('categories')
    for p in products:
        prdcts_data = {
            'product name': p.product_name,
            'image url': os.path.basename(p.product_image.name) if p.product_image else None,
            'categories': [{'id': category.id, 'name': category.category_name} for category in p.categories.all()],
        }
        products_data.append(prdcts_data)

    return JsonResponse(products_data, safe=False)

def category_listing(request):
    filtered_category_queryset = (Category.objects
                                  .filter(parent__isnull=True)
                                  .annotate(products_quantity=Sum('children__products__quantity', distinct=True))
                                  .values('id', 'category_name', 'products_quantity'))

    return render(request, 'store/listing_category.html',
                  {'category_names': filtered_category_queryset})

def product_listing(request, category_id):
    parent_category = get_object_or_404(Category.objects.prefetch_related('children__products'), id=category_id)
    all_products_from_category = (Product.objects.filter(categories__in=parent_category.children.all())
                                  .distinct())
    for product in all_products_from_category:
        product.total_cost = product.price * product.quantity

    max_price = all_products_from_category.aggregate(Max('price'))['price__max']
    min_price = all_products_from_category.aggregate(Min('price'))['price__min']
    avg_price = all_products_from_category.aggregate(Avg('price'))['price__avg']
    total_price = all_products_from_category.aggregate(total=Sum(F('price') * F('quantity')))['total']

    paginator = Paginator(all_products_from_category, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'store/listing_product.html', {
        'product_names': page_obj,
        'max_price': max_price,
        'min_price': min_price,
        'avg_price': avg_price,
        'total_price': total_price,
    })

def details_of_product(request, product_id):
    fields_of_product = get_object_or_404(Product, id=product_id)

    return render(request, 'store/details_product.html', {'product': fields_of_product})

