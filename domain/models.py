class User:
    def __init__(self, id: str, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def change_email(self, new_email: str):
        if '@' not in new_email:
            raise ValueError("Invalid email format")
        self.email = new_email


class Product:
    def __init__(self, id: str, name: str, price: float):
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        self.id = id
        self.name = name
        self.price = price


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