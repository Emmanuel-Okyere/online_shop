"""Shop URLS"""
from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
app_name = "shop"
urlpatterns = [
    path("list/all/", views.product_list, name = "product_list"),
    path("list/<slug:category_slug>/", views.product_list, name = "product_list_by_category"),
    path("<int:id>/<slug:slug>/detail/", views.product_detail, name = "product_detail"),
]
