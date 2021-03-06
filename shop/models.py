"""Models.py"""
from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    """Class"""
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True, null=True)

    class Meta:
        """Things that come with the class"""
        ordering = ("-name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        """Human name"""
        return self.name

    def get_absolute_url(self):
        """Getting absolute URL"""
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    """Products model"""
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products/%Y%m%d", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Already here"""
        ordering = ("-name",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Getting absolute URL"""
        return reverse("shop:product_detail", args=[self.id, self.slug])
