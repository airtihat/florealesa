from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('categories/', views.categories_view, name='categories'),
    path('cart/', views.cart_detail, name='cart_detail'),  # ✅ عرض السلة
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),  # ✅ إضافة للسلة
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),  # ✅ إزالة من السلة

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),  # ✅ تفاصيل المنتج
]
