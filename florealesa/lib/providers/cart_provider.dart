
import 'package:flutter/foundation.dart';

class CartProvider with ChangeNotifier {
  final List<int> _cartItems = [];

  List<int> get cartItems => _cartItems;

  void addToCart(int productId) {
    _cartItems.add(productId);
    notifyListeners();
  }

  void removeFromCart(int productId) {
    _cartItems.remove(productId);
    notifyListeners();
  }

  void clearCart() {
    _cartItems.clear();
    notifyListeners();
  }
}
