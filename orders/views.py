from django.http import HttpResponse
from django.shortcuts import render

# عرض نص بسيط كاستجابة (للاختبار أو العرض السريع)
def index(request):
    return HttpResponse("مرحباً بك في قسم الطلبات")

# عرض صفحة HTML من مجلد القوالب
def orders_home(request):
    return render(request, 'orders/orders.html')
