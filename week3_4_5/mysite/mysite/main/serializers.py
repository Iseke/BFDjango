from rest_framework import serializers
from mysite.main.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)

    class Meta:
        model = Product
        #exclude = ['created_at', 'updated_at']
        fields = ['id','icon','name','price','description','available','category']