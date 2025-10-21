from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from domain.models import User as DomainUser, Product as DomainProduct, Order as DomainOrder

Base = declarative_base()

class SQLAlchemyUser(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)

    def to_domain(self):
        return DomainUser(id=self.id, name=self.name, email=self.email)

    @classmethod
    def from_domain(cls, domain_user):
        return cls(id=domain_user.id, name=domain_user.name, email=domain_user.email)


class SQLAlchemyProduct(Base):
    __tablename__ = 'products'

    id = Column(String, primary_key=True)
    name = Column(String)
    price = Column(Float)

    def to_domain(self):
        return DomainProduct(id=self.id, name=self.name, price=self.price)

    @classmethod
    def from_domain(cls, domain_product):
        return cls(id=domain_product.id, name=domain_product.name, price=domain_product.price)


class SQLAlchemyOrder(Base):
    __tablename__ = 'orders'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('users.id'))
    product_id = Column(String, ForeignKey('products.id'))
    quantity = Column(Integer)

    user = relationship('SQLAlchemyUser')
    product = relationship('SQLAlchemyProduct')

    def to_domain(self):
        return DomainOrder(id=self.id, user=self.user.to_domain(), product=self.product.to_domain(), quantity=self.quantity)

    @classmethod
    def from_domain(cls, domain_order):
        return cls(id=domain_order.id, user_id=domain_order.user.id, product_id=domain_order.product.id, quantity=domain_order.quantity)