from rest_framework import serializers, viewsets
from .models import Menu, Booking


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  
        fields = '__all__'  # Use all fields from the model

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'