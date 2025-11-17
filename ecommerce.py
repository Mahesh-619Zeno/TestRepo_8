# Filename: flawed_ecommerce.py

import uuid
import datetime
import pickle

class Product:
    def __init__(self, product_id, name, price, quantity, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

class User:
    def __init__(self, user_id, username, email, role='customer'):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.role = role

class Order:
    def __init__(self, order_id, user, items, created_at=None):
        self.order_id = order_id
        self.user = user
        self.items = items  # dict of product_id: quantity
        self.created_at = created_at or datetime.datetime.now()
        self.status = 'Created'

    def total_price(self, catalog):
        total = 0
        for pid, qty in self.items.items():
            product = catalog.get(pid)
            if product:
                total += product.price * qty
        return total

    def update_status(self, new_status):
        self.status = new_status

class EcommercePlatform:
    def __init__(self):
        self.products = {}   # product_id: Product
        self.users = {}      # user_id: User
        self.orders = {}     # order_id: Order

    def add_product(self, name, price, quantity, category):
        pid = str(uuid.uuid4())
        product = Product(pid, name, price, quantity, category)
        self.products[pid] = product
        return product

    def register_user(self, username, email, role='customer'):
        user_id = str(uuid.uuid4())
        user = User(user_id, username, email, role)
        self.users[user_id] = user
        return user

    def place_order(self, user_id, items):
        if user_id not in self.users:
            return None
        order_id = str(uuid.uuid4())
        order = Order(order_id, self.users[user_id], items)
        self.orders[order_id] = order
        return order

    def cancel_order(self, order_id):
        order = self.orders.get(order_id)
        if order and order.status != 'Cancelled':
            order.update_status('Cancelled')
            return True
        return False

    def ship_order(self, order_id):
        order = self.orders.get(order_id)
        if order and order.status == 'Created':
            order.update_status('Shipped')
            return True
        return False

    def serialize_orders(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.orders, f)

    def deserialize_orders(self, filename):
        with open(filename, 'rb') as f:
            self.orders = pickle.load(f)

# Usage example
platform = EcommercePlatform()
p1 = platform.add_product("Camera", 299.99, 5, "Electronics")
p2 = platform.add_product("Microphone", 89.99, 10, "Audio")

user = platform.register_user("alice", "alice@example.com")
order = platform.place_order(user.user_id, {p1.product_id: 2, p2.product_id: 1})

platform.serialize_orders("orders.pkl")
platform.deserialize_orders("orders.pkl")
