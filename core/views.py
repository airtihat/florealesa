from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, LoginForm  # استخدم النماذج المخصصة


# ✅ الصفحة الرئيسية - تتطلب تسجيل دخول
@login_required
def index(request):
    return render(request, 'core/home.html')


# ✅ عرض صفحة إنشاء حساب
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # تسجيل دخول تلقائي بعد التسجيل
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'core/signup.html', {'form': form})


# ✅ عرض صفحة تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    
    return render(request, 'core/login.html', {'form': form})


# ✅ عرض صفحة اختبار
def test_view(request):
    return render(request, 'core/test.html')
