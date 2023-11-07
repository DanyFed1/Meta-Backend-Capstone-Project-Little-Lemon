"""LittleLemonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet, SingleMenuItemView, MenuItemsView

router = DefaultRouter()
router.register(r'booking/tables', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]

#To check auth users using djoser first need to login as superuser and then then
#go to http://127.0.0.1:8000/auth/users/
#to register new user go to  http://127.0.0.1:8000/auth/users/
#To login, visit the djoser generated URL http://127.0.0.1:8000/auth/token/login/
#To Logout, enter the URL http://127.0.0.1:8000/auth/token/logout/  with a POST method to logout the user.
# to access the post request for booking actually need to use http://127.0.0.1:8000/restaurant/api-token-auth/