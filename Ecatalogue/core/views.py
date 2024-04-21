from django.shortcuts import get_object_or_404, render
from requests import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.permissions import AllowAny
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .models import Product, Category
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import AuthenticateSerializer, ProductSerializer, CategorySerializer, RegisterSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser




class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS



class AuthenticateView(TokenObtainPairView):
    serializer_class = AuthenticateSerializer
    permission_classes = [AllowAny]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=True, methods=['post'], parser_classes=[MultiPartParser, FormParser])
    def upload_image(self, request, pk=None):
        product = self.get_object()
        file = request.FILES.get('image')
        if not file:
            return Response({'message': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        product.image = file
        product.save()
        return Response({'message': 'Image uploaded successfully'}, status=status.HTTP_200_OK)
        
    def get_object(self,queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Product, name=item)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self,queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Category, name=item)
