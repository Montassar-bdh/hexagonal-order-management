from abc import ABC, abstractmethod

from domain.models import Order


class UserRepository(ABC):
    @abstractmethod
    def save(self, user) -> None:
        pass

    @abstractmethod
    def get(self, user_id: str):
        pass

    @abstractmethod
    def delete(self, user_id: str) -> None:
        pass

class ProductRepository(ABC):
    @abstractmethod
    def save(self, product) -> None:
        pass

    @abstractmethod
    def get(self, product_id: str):
        pass

    @abstractmethod
    def delete(self, product_id: str) -> None:
        pass

class OrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        pass

    @abstractmethod
    def get(self, order_id: str) -> Order:
        pass

    @abstractmethod
    def delete(self, order_id: str) -> None:
        pass