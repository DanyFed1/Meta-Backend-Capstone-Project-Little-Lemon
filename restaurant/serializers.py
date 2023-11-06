from rest_framework import serializers
from .models import Menu  


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  
        fields = '__all__'  # Use all fields from the model