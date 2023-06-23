from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('restaurants/', views.restaurants, name="restaurants"),
    path('rest-items/<int:pk>/', views.restaurantItems, name="restaurantItems"),
]
