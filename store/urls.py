from tkinter.font import names

from django.urls import path
from .views import (product_list, product_detail, category_info, product_info,
                    category_listing, details_of_product, product_listing)

urlpatterns = [
    path('', product_list),
    path('<int:product_id>/', product_detail),
    path('categories/', category_info),
    path('products/', product_info),
    path('category/', category_listing),
    path('category/<int:category_id>/products/', product_listing, name='product_listing'),
    path('product/<int:product_id>/', details_of_product, name='details_of_product'),
]