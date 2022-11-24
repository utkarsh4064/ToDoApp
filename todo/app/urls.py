from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]
