#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/items/', views.MenuItemsView.as_view(), name='menu-item-list'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
]