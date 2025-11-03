from abc import ABC, abstractmethod

from core.entities.order import Order


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
