from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.ports.repositories.user_repository_port import UserRepository
from infrastructure.persistence.models import SQLAlchemyUser


class SQLAlchemyUserAdapter(UserRepository):
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
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
