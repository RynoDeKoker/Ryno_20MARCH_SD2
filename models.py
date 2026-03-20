# models.py

class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role


class Product:
    def __init__(self, product_id, name, price, stock_qty):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_qty = stock_qty


class Order:
    def __init__(self, order_id, user_id, product_id, quantity):
        self.order_id = order_id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity


class Warehouse:
    def __init__(self, warehouse_id, location, capacity):
        self.warehouse_id = warehouse_id
        self.location = location
        self.capacity = capacity