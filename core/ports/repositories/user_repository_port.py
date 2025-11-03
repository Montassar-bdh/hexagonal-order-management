from abc import ABC, abstractmethod


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
