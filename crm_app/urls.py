
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('add_customer/', views.add_customer, name='add_customer_record'),
    path('single_customer/<int:pk>/', views.single_customer, name='single_customer'),
    path('update_customer/<int:pk>/', views.update_customer, name='update_customer_record'),
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer_record'),
]
