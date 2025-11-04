from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.ports.repositories.product_repository_port import ProductRepository
from infrastructure.persistence.sql.models.product_model import ProductModel


class SQLAlchemyProductAdapter(ProductRepository):
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        ProductModel.__table__.create(self.engine)
    def save(self, product):
        session = self.Session()
        db_product = ProductModel.from_domain(product)
        session.add(db_product)
        session.commit()

    def get(self, product_id: str):
        session = self.Session()
        db_product = session.query(ProductModel).filter(ProductModel.id == product_id).first()
        return db_product.to_domain() if db_product else None

    def delete(self, product_id: str):
        session = self.Session()
        db_product = session.query(ProductModel).filter(ProductModel.id == product_id).first()
        if db_product:
            session.delete(db_product)
            session.commit()
