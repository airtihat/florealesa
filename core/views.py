
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm

# عرض صفحة تسجيل حساب جديد
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # إذا كنت تستخدم نموذج مستخدم مخصص يحتوي على phone، فيجب التحقق من وجوده
            user.save()
            return redirect('login')  # إعادة التوجيه إلى صفحة تسجيل الدخول
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'core/register.html', {'form': form})


# عرض صفحة تسجيل الدخول
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # يمكنك تغييره حسب وجهتك بعد الدخول
    else:
        form = LoginForm()
    
    return render(request, 'core/login.html', {'form': form})
from django.http import HttpResponse

def index(request):
    return HttpResponse("مرحباً بك في الصفحة الرئيسية لـ Core.")
