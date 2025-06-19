from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('categories/', views.categories_view, name='categories'),
    path('cart/', views.cart_view, name='cart'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
