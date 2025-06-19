# storefront/cart.py

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id] += 1
        else:
            self.cart[product_id] = 1
        self.save()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True

    def save(self):
        self.session.modified = True

    def get_items(self):
        from .models import Product
        products = []
        for pid, qty in self.cart.items():
            try:
                product = Product.objects.get(id=pid)
                products.append({'product': product, 'quantity': qty})
            except Product.DoesNotExist:
                continue
        return products
