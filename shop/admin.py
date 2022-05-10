"""Django admin model"""
from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin"""
    list_display = ("name","slug",)
    list_filter = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug":("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin"""
    list_display = ("category","name","image","price","available",)
    list_filter = ("category",)
    search_fields = ("name",)
    list_editable = ['price', 'available','image']
    prepopulated_fields = {"slug":("name",)}
