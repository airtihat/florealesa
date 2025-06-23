from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# استيراد الصفحة الرئيسية من storefront (يمكن نقلها لاحقًا لـ core)
from storefront.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية
    path('', home_view, name='home'),

    # روابط التطبيقات
    path('', include('core.urls')),
    path('storefront/', include('storefront.urls')),
    path('orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
