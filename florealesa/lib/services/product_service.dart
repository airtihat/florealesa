import 'dart:convert';
import '../models/product.dart';

class ProductService {
  static Future<List<Product>> fetchDummyProducts() async {
    final String jsonString = '''
    [
      {
        "id": 1,
        "name": "باقة ورد وردية",
        "description": "باقة مميزة من الورود الوردية الفاخرة.",
        "price": 149.99,
        "image": "https://via.placeholder.com/150x150"
      },
      {
        "id": 2,
        "name": "علبة شوكولاتة فاخرة",
        "description": "شوكولاتة مستوردة مع تغليف أنيق.",
        "price": 99.50,
        "image": "https://via.placeholder.com/150x150"
      }
    ]
    ''';

    final List decoded = json.decode(jsonString);
    return decoded.map((item) => Product.fromJson(item)).toList();
  }
}
