from rest_framework import serializers
from .models import User,Product,Sale

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,read_only=True)

    class Meta:
        model = Sale
        fields = '__all__'