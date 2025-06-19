from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # الصفحة الرئيسية (تحتاج تسجيل دخول)
    path('', views.index, name='index'),

    # تسجيل الدخول
    path('login/', views.login_view, name='login'),

    # إنشاء حساب
    path('signup/', views.signup_view, name='signup'),

    # تسجيل الخروج (يعيدك إلى login)
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # صفحة اختبار (اختيارية)
    path('test/', views.test_view, name='test'),
]
