class Product:
    def __init__(self, id: str, name: str, price: float):
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        self.id = id
        self.name = name
        self.price = price
