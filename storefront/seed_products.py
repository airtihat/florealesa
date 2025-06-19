# storefront/seed_products.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'florealesa.settings')
django.setup()

from storefront.models import Category, Product
from django.core.files import File

# حذف المنتجات القديمة
Product.objects.all().delete()
Category.objects.all().delete()

# الفئات
flowers = Category.objects.create(name="زهور")
chocolates = Category.objects.create(name="شوكولاتة")
gifts = Category.objects.create(name="هدايا")

# منتجات وهمية
products_data = [
    {
        "name": "بوكيه ورد أحمر",
        "description": "باقة من الورود الحمراء الفاخرة.",
        "price": 150,
        "discount_price": 120,
        "rating": 5,
        "category": flowers,
        "image_path": "media/demo/flower.jpg"
    },
    {
        "name": "علبة شوكولاتة فاخرة",
        "description": "علبة مميزة تحتوي على مجموعة من الشوكولاتة البلجيكية.",
        "price": 100,
        "rating": 4,
        "category": chocolates,
        "image_path": "media/demo/chocolate.jpg"
    },
    {
        "name": "صندوق هدايا ذهبي",
        "description": "هدية فاخرة مغلفة بصندوق أنيق.",
        "price": 200,
        "discount_price": 180,
        "rating": 4,
        "category": gifts,
        "image_path": "media/demo/gift.jpg"
    },
]

for item in products_data:
    product = Product(
        name=item["name"],
        description=item["description"],
        price=item["price"],
        discount_price=item.get("discount_price"),
        rating=item["rating"],
        category=item["category"]
    )
    with open(item["image_path"], 'rb') as img:
        product.image.save(os.path.basename(item["image_path"]), File(img), save=True)

print("✅ تم إنشاء المنتجات بنجاح.")
