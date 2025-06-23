from django.contrib import admin
from .models import Category, Product
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_active', 'image_preview']
    list_filter = ['is_active', 'category']
    search_fields = ['name', 'description']

    def image_preview(self, obj):
        image_url = obj.image.url if obj.image else obj.image_url
        if image_url:
            return format_html('<img src="{}" width="60" style="border-radius:4px;" />', image_url)
        return "-"
    image_preview.short_description = "الصورة"
