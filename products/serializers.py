from rest_framework import serializers
from .models import Products, ProductImages, Variants, ProductVariants, ProductVariantPrices


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'


class VariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variants
        fields = '__all__'


class ProductVariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariants
        fields = '__all__'


class ProductVariantPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantPrices
        fields = '__all__'

