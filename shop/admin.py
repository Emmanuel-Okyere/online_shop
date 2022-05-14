"""Django admin model"""
from django.contrib import admin
from .models import Category, Product

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin"""
    list_display = ("name", "slug",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin"""
    list_display = ("category", "name", "image", "price", "available",)
    search_fields = ("name",)
    list_editable = ['price', 'available', 'image', "name"]
