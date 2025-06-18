# مثال urls.py داخل أي تطبيق

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
