from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Category, Product
from mptt.admin import MPTTModelAdmin

# admin.site.register(Category, MPTTModelAdmin)
# admin.site.register(Product)

@admin.register(Category)
class CustomCategory(MPTTModelAdmin):
    model = Category
    list_display = ('category_name', 'parent')
    search_fields = ('category_name',)
    list_filter = ('category_name',)



@admin.register(Product)
class CustomProduct(ModelAdmin):
    model = Product
    list_display = ('product_name', 'product_image')
    search_fields = ('product_name',)
    list_filter = ('product_name',)

