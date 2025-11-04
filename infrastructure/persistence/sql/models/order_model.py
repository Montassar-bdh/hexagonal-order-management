from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from core.entities.order import Order as DomainOrder
from infrastructure.persistence.sql.models.base_model import Base


class OrderModel(Base):
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
