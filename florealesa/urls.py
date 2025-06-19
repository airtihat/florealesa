# florealesa/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from storefront.views import home_view  # يمكنك حذف هذا إذا كانت الصفحة الرئيسية داخل storefront.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # أو استخدم include حسب طريقة تنظيمك
    path('core/', include('core.urls')),
    path('storefront/', include('storefront.urls')),
    path('orders/', include('orders.urls')),
]

# دعم ملفات الصور أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
