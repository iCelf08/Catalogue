from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer




class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
      
    def get_object(self,queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Product, name=item)
    