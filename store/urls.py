from django.urls import path
from .views import product_list, product_detail, category_info, product_info

urlpatterns = [
    path('', product_list),
    path('<int:product_id>/', product_detail),
    path('categories/', category_info),
    path('products/', product_info),
]