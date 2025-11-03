from abc import ABC, abstractmethod


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
