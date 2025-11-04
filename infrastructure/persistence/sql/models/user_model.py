from sqlalchemy import Column, String

from core.entities.user import User as DomainUser
from infrastructure.persistence.sql.models.base_model import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)

    def to_domain(self):
        return DomainUser(id=self.id, name=self.name, email=self.email)

    @classmethod
    def from_domain(cls, domain_user):
        return cls(id=domain_user.id, name=domain_user.name, email=domain_user.email)
