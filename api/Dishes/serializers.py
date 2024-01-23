from rest_framework import serializers
from Dishes.models import Dishes


class DishesSerializer(serializers.ModelSerializer):
    """
    Dishes Serializer
    """
    class Meta:
        model = Dishes
        fields = '__all__'