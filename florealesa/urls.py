from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # روابط التطبيقات
    path('', include('core.urls')),                  # التطبيق الأول: core
    path('storefront/', include('storefront.urls')), # التطبيق الثاني: storefront
    path('orders/', include('orders.urls')),         # التطبيق الثالث: orders
]
