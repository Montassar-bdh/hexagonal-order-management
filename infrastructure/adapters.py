from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.ports import OrderRepository, ProductRepository, UserRepository
from infrastructure.models import (SQLAlchemyOrder, SQLAlchemyProduct,
                                   SQLAlchemyUser)


class SQLAlchemyUserAdapter(UserRepository):
    def __init__(self, engine_url: str, connect_args: dict=None):
        if connect_args is None:
            self.engine = create_engine(engine_url)
        else:
            self.engine = create_engine(engine_url, connect_args=connect_args)
        SQLAlchemyUser.__table__.create(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save(self, user):
        session = self.Session()
        db_user = SQLAlchemyUser.from_domain(user)
        session.add(db_user)
        session.commit()

    def get(self, user_id: str):
        session = self.Session()
        db_user = session.query(SQLAlchemyUser).filter(SQLAlchemyUser.id == user_id).first()
        return db_user.to_domain() if db_user else None

    def delete(self, user_id: str):
        session = self.Session()
        db_user = session.query(SQLAlchemyUser).filter(SQLAlchemyUser.id == user_id).first()
        if db_user:
            session.delete(db_user)
            session.commit()


class SQLAlchemyProductAdapter(ProductRepository):
    def __init__(self, engine_url: str):
        self.engine = create_engine(engine_url)
        self.Session = sessionmaker(bind=self.engine)
        SQLAlchemyProduct.__table__.create(self.engine)
    def save(self, product):
        session = self.Session()
        db_product = SQLAlchemyProduct.from_domain(product)
        session.add(db_product)
        session.commit()

    def get(self, product_id: str):
        session = self.Session()
        db_product = session.query(SQLAlchemyProduct).filter(SQLAlchemyProduct.id == product_id).first()
        return db_product.to_domain() if db_product else None

    def delete(self, product_id: str):
        session = self.Session()
        db_product = session.query(SQLAlchemyProduct).filter(SQLAlchemyProduct.id == product_id).first()
        if db_product:
            session.delete(db_product)
            session.commit()


class SQLAlchemyOrderAdapter(OrderRepository):
    def __init__(self, engine_url: str):
        self.engine = create_engine(engine_url)
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
