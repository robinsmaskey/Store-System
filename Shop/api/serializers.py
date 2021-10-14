from rest_framework import serializers
from Shop.models import Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'address', 'established_date', 'description', 'phone', 'is_active']

class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ShopCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name']


