from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Menu
from .serializers import MenuSerializer


class MenuViewTest(APITestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        Menu.objects.create(id=1, title="Spaghetti Carbonara", price=9.99, inventory=5)
        Menu.objects.create(id=2, title="Margherita Pizza", price=7.99, inventory=10)
        Menu.objects.create(id=3, title="Caesar Salad", price=5.99, inventory=20)

    def test_get_all(self):
        # Get API response
        response = self.client.get(reverse('menu/items/'))  
        # Get data from db
        menus = Menu.objects.all().order_by('id')
        serializer = MenuSerializer(menus, many=True)
        # Compare the serialized data with the response data
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)