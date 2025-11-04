from sqlalchemy import Column, String, Float

from core.entities.product import Product as DomainProduct
from infrastructure.persistence.sql.models.base_model import Base


class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(String, primary_key=True)
    name = Column(String)
    price = Column(Float)

    def to_domain(self):
        return DomainProduct(id=self.id, name=self.name, price=self.price)

    @classmethod
    def from_domain(cls, domain_product):
        return cls(id=domain_product.id, name=domain_product.name, price=domain_product.price)
