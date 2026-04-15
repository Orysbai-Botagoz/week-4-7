import numpy as np
from models_block1 import Product

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














products = [Product(1, "Laptop", 1200.0, "Electronics"),
            Product(2, "Mouse", 25.0, "Electronics"),
            Product(3, "Mous", 450.0, "Electronics")]
cats = create_category_array(products)
print(count_unique_categories(cats))
print(filter_prices_by_category(products))


