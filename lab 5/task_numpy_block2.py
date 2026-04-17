import numpy as np
from models_block1 import Product, Order, User

#11 task
def create_price_array(products):
    prices = np.array([p.price for p in products], dtype=np.float64)
    return prices

#12 task
def mean_price(prices):
    return np.mean(prices)
def median_price(prices):
    return np.median(prices)

#13 task
def normalize_prices(prices):
    min_price = np.min(prices)
    max_price = np.max(prices)
    normalized_prices = (prices - min_price)/(max_price - min_price)
    return normalized_prices

#14 task
def create_category_array(products):
    categories = np.array([p.category for p in products])
    return categories

#15 task
def count_unique_categories(category_array):
    unique_elements = set(category_array)
    return len(unique_elements)

#16 task
def filter_prices_by_category(products):
    prices = np.array([p.price for p in products])
    price_mean = np.mean(prices)
    expensive_products = [p for p in products if p.price > price_mean]
    return expensive_products

#17 task
def reduce_prices(products):
    prices = np.array([p.price for p in products])
    reduced_prices = prices * 0.9
    for i, product in enumerate(products):
        product.price = reduced_prices[i]
    return reduced_prices, products

#18 task
def create_orders_matrix(orders):
    sums = [order.total_price() for order in orders]
    orders_matrix = np.array(sums).reshape(-1, 1)
    return orders_matrix

#19 task
def average_purchase_per_user(orders_matrix):
    average = np.mean(orders_matrix)
    return average

#20 task
def get_indices_over_1000(orders_matrix):
    indices = np.where(orders_matrix > 1000)[0]
    return indices






u1 = User(1, "Alice", "alice@example.com")
u2 = User(2, "Bob", "bob@example.com")
u3 = User(3, "Charlie", "charlie@email.com")

p1 = Product(1, "Mouse", 400, "Electronics")
p2 = Product(2, "T-shirt", 25.0, "Clothing")
p3 = Product(3, "Laptop", 1225.0, "Electronics")


# 3. Теперь создаем список заказов
orders = [
    Order(1, u1, [p1]),          # Список из одного товара
    Order(2, u2, [p2]),
    Order(3, u3, [p3]),          # Список из двух товаров
    Order(4, u2, [p1])
]
products = []
for order in orders:
    products.extend(order._products)

rows = []
for order in orders:
    for product in order._products:
        row = {
            "order_id": order._id,
            "user_name": order._user._name,
            "product_name": product.name,
            "category": product.category,
            "price": product.price,
        }
        rows.append(row)

orders_data = []
users_data = {}
for order in orders:
    orders_data.append({
        "order_id": order._id,
        "user_id": order._user._id,
        "total": order.total_price(),
    })
    u = order._user
    if u._id not in users_data:
        users_data[u._id] = {'user_id': u._id, "user_name": u._name}


