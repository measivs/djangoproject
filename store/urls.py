from django.urls import path
from .views import product_list, product_detail, category_info, product_info, category_listing, details_of_category

urlpatterns = [
    path('', product_list),
    path('<int:product_id>/', product_detail),
    path('categories/', category_info),
    path('products/', product_info),
    path('category/', category_listing),
    path('category/<int:category_id>/', details_of_category, name='details_of_category'),
]