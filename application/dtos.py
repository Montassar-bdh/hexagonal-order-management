from pydantic import BaseModel, EmailStr, confloat
from domain.models import User, Product, Order
from typing import List

class UserDTO(BaseModel):
    id: str
    name: str
    email: EmailStr

    @classmethod
    def from_domain(cls, domain_user):
        return cls(id=domain_user.id, name=domain_user.name, email=domain_user.email)

    def to_domain(self):
        return User(id=self.id, name=self.name, email=self.email)


class ProductDTO(BaseModel):
    id: str
    name: str
    price: confloat(gt=0)

    @classmethod
    def from_domain(cls, domain_product):
        return cls(id=domain_product.id, name=domain_product.name, price=domain_product.price)

    def to_domain(self):
        return Product(id=self.id, name=self.name, price=self.price)


class OrderDTO(BaseModel):
    id: str
    user_id: str
    product_id: str
    quantity: int

    @classmethod
    def from_domain(cls, domain_order):
        return cls(id=domain_order.id, user_id=domain_order.user.id, product_id=domain_order.product.id, quantity=domain_order.quantity)

    def to_domain(self, user: User, product: Product):
        return Order(id=self.id, user=user, product=product, quantity=self.quantity)