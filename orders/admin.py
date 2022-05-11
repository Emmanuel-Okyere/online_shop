"""Admin model"""
from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]
@admin.register(Order)
class Orderadmin(admin.ModelAdmin):
    "Admin class"
    list_display = ("first_name","email","city","created","paid",)
    list_filter = ("city","email","created")
    inlines = [OrderItemInline]
