from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.ports.repositories.order_repository_port import OrderRepository
from infrastructure.persistence.models import SQLAlchemyOrder


class SQLAlchemyOrderAdapter(OrderRepository):
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        SQLAlchemyOrder.__table__.create(self.engine)

    def save(self, order):
        session = self.Session()
        db_order = SQLAlchemyOrder.from_domain(order)
        session.add(db_order)
        session.commit()

    def get(self, order_id: str):
        session = self.Session()
        db_order = session.query(SQLAlchemyOrder).filter(SQLAlchemyOrder.id == order_id).first()
        return db_order.to_domain() if db_order else None

    def delete(self, order_id: str):
        session = self.Session()
        db_order = session.query(SQLAlchemyOrder).filter(SQLAlchemyOrder.id == order_id).first()
        if db_order:
            session.delete(db_order)
            session.commit()
