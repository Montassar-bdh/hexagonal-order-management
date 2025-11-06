from sqlalchemy.orm import Session

from core.ports.repositories.order_repository_port import OrderRepository
from infrastructure.persistence.sql.models.order_model import OrderModel


class SQLAlchemyOrderAdapter(OrderRepository):
    def __init__(self, db: Session):
        self.session = db

    def save(self, order):
        db_order = OrderModel.from_domain(order)
        with self.session as session:
            session.add(db_order)
            session.commit()

    def get(self, order_id: str):
        with self.session as session:
            db_order = session.query(OrderModel).filter(OrderModel.id == order_id).first()
            return db_order.to_domain() if db_order else None

    def delete(self, order_id: str):
        with self.session as session:
            db_order = session.query(OrderModel).filter(OrderModel.id == order_id).first()
            if db_order:
                self.session.delete(db_order)
                self.session.commit()
