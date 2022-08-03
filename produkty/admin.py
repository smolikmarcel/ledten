from django.contrib import admin
from .models import ProductsImg, Product, ProductCategory

# Register your models here.
admin.site.register(ProductsImg)
admin.site.register(Product)
admin.site.register(ProductCategory)
