from rest_framework import serializers
from .models import  Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True, required=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'stock', 'category', 'image', 'owner')
    
