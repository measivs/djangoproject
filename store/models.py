from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    category_name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['category_name']

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to='products/', null=True, blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.product_name
