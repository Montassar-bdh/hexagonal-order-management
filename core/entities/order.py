from core.entities.product import Product
from core.entities.user import User

class Order:
    def __init__(self, id: str, user: User, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.id = id
        self.user = user
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def update_quantity(self, new_quantity: int):
        if new_quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.quantity = new_quantity
        self.total_price = self.product.price * new_quantity
