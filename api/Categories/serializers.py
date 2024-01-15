from rest_framework import serializers
from Categories.models import Categories

class CategoriesSerializer(serializers.ModelSerializer):
    """
    Categories Serializer
    """
    class Meta:
        model = Categories
        fields = '__all__'