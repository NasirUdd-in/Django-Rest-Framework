from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductImages(models.Model):
    product = models.ManyToManyField(Products, related_name='product_images')
    file_path = models.CharField(max_length=255)
    thumbnail = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Variants(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductVariants(models.Model):
    variant = models.CharField(max_length=255)
    variant_id = models.ForeignKey(Variants, on_delete=models.CASCADE, related_name='product_variants')
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_variants')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductVariantPrices(models.Model):
    product_variant_one = models.ForeignKey(ProductVariants, on_delete=models.CASCADE, related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariants, on_delete=models.CASCADE, related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariants, on_delete=models.CASCADE, related_name='product_variant_three')
    price = models.FloatField()
    stock = models.IntegerField()
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_variant_prices')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
