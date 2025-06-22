from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Product
from .cart import Cart

# الصفحة الرئيسية
def home_view(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'storefront/home.html', {'products': products})

# صفحة التصنيفات
def categories_view(request):
    return render(request, 'storefront/categories.html')

# صفحة السلة
def cart_view(request):
    cart = Cart(request)
    return render(request, 'storefront/cart.html', {'cart_items': cart.get_items()})

# تسجيل مستخدم جديد
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "تم إنشاء الحساب بنجاح 🎉")
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'storefront/register.html', {'form': form})

# تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح ✅")
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'storefront/login.html', {'form': form})

# تسجيل الخروج
def logout_view(request):
    logout(request)
    messages.info(request, "تم تسجيل الخروج 👋")
    return redirect('/')

# إضافة منتج إلى السلة
def add_to_cart(request, id):
    cart = Cart(request)
    cart.add(id)
    return redirect('cart_detail')

# إزالة منتج من السلة
def remove_from_cart(request, id):
    cart = Cart(request)
    cart.remove(id)
    return redirect('cart_detail')

# عرض تفاصيل السلة
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'storefront/cart.html', {'cart_items': cart.get_items()})

# عرض تفاصيل المنتج
def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
