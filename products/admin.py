from django.contrib import admin
from .models import Products, ProductImages, Variants, ProductVariants, ProductVariantPrices


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sku', 'created_at', 'updated_at')
    search_fields = ('title', 'sku')


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_path', 'thumbnail', 'created_at', 'updated_at')
    search_fields = ('file_path',)


@admin.register(Variants)
class VariantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(ProductVariants)
class ProductVariantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'variant', 'variant_id', 'product_id', 'created_at', 'updated_at')
    search_fields = ('variant',)


@admin.register(ProductVariantPrices)
class ProductVariantPricesAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_variant_one', 'product_variant_two', 'product_variant_three', 'price', 'stock', 'product_id', 'created_at', 'updated_at')
    search_fields = ('product_id__title',)

