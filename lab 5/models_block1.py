#1 task
from typing import List
from datetime import datetime


class User:
    def __init__(self, id, name, email):
        self._id = int(id)
        self._name = name.strip().title()
        email = email.lower()
        if "@" not in email:
            raise ValueError("Invalid email")
        self._email = email

    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"

    def __del__(self):
        print(f"User <{self._name}> deleted")
        pass

#2 task
    @classmethod
    def from_string(cls, data: str):
        parts = data.split(",")
        id = int(parts[0].strip())
        name = parts[1].strip()
        email = parts[2].strip()
        return cls(id, name, email)



#3 task
class Product:
    def __init__(self, id, name, price, category):
        self._id = int(id)
        self._name = str(name)
        self.price = float(price)
        self.category = str(category)

    def __repr__(self):
        return f"Product({self._id}, \"{self._name}\", {self.price}, \"{self.category}\")"

    def __str__(self):
        return f"Product(id={self._id}, name='{self._name}', price={self.price}, category='{self.category}')"

    def __hash__(self): #экономия времени
        return hash(self._id)

    def __eq__(self, other): #экономия времени
        if not isinstance(other, Product):
            return False
        return (self._id == other._id) and (self._name == other._name)

    @property
    def name(self):
        return self._name

    def to_dict(self):
        return {"id": self._id, "name": self._name, "price": self.price, "category": self.category}

#4 task
class Inventory:
    def __init__(self, products: List[Product] = None):
        self._products = {}

    def add_product(self, product: Product):
        product_id = product._id
        if product_id in self._products:
            raise ValueError(f"Product <{product_id}> already exists")
        self._products[product_id] = product
        pass

    def remove_product(self, product_id: int):
        if product_id in self._products:
            del self._products[product_id]

    def get_product(self, product_id: int):
        return self._products.get(product_id)

    def get_all_products(self):
        return list(self._products.values())

    def unique_products(self):
        return list(set(self._products.values()))

    def to_dict(self):
        return {product_id: product.to_dict() for product_id, product in self._products.items()}

#5 task
    def filter_by_price(self, min_price: float) -> list[Product]:
        return list(filter(lambda product: product.price >= min_price, self._products.values()))

#6 task
class Logger:
    def __init__(self, logger):
        self._logger = logger

    def log_action(self, user: User, action: str, product: Product, filename: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry =  f"{timestamp};{user._id};{action};{product._id}"
        with open(filename, "a") as f:
            f.write(f"{log_entry}\n")

    def read_logs(self, filename: str):
        logs = []
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                parts = line.split(";")
                timestamp = parts[0]
                user_id = parts[1]
                action = parts[2]
                product_id = parts[3]
                log_entry = {"timestamp": timestamp,
                             "user_id": user_id,
                             "action": action,
                             "product": product_id}
                logs.append(log_entry)
            return logs

#7 task
class Order:
    def __init__(self, order_id: int, user: User, products: List[Product]):
        self._id = order_id
        self._user = user
        self._products = products if products is not None else []

    def add_product(self, product: Product):
        self._products.append(product)

    def remove_product(self, product_id: int):
        for product in self._products:
            if product._id == product_id:
                self._products.remove(product)
                break

    def total_price(self):
        total = 0
        for product in self._products:
            total += product.price
        return total

    def __str__(self):
        id = self._id
        name = self._user._name
        total_price = self.total_price()
        items_count = len(self._products)
        return f"Order id:{id} | Customer: {name} | Items: {items_count} | Total: ${total_price}"

#8 task
    def most_expensive_products(self, n: int) -> list[Product]:
        sorted_list = sorted(self._products, key = lambda p: p.price, reverse=True)
        return sorted_list[:n]

#9 task
def price_stream(products):
    for product in products:
        yield product.price #генератор

#10 task
class OrderIterator:
    def __init__(self, orders: list[Order]):
        self._order = orders
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._order):
            product = self._order[self._index]
            self._index += 1
            return product
            pass
        else:
            raise StopIteration


