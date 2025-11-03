from application.dtos import OrderDTO
from core.ports.repositories.order_repository_port import OrderRepository
from core.ports.repositories.product_repository_port import ProductRepository
from core.ports.repositories.user_repository_port import UserRepository


class OrderService:
    def __init__(self, order_repo: OrderRepository, user_repo: UserRepository, product_repo: ProductRepository):
        self.order_repo = order_repo
        self.user_repo = user_repo
        self.product_repo = product_repo

    def create_order(self, order_dto: OrderDTO) -> None:
        user = self.user_repo.get(order_dto.user_id)
        product = self.product_repo.get(order_dto.product_id)
        
        if not user or not product:
            raise ValueError("Invalid user or product.")
        
        order = order_dto.to_domain(user=user, product=product)  # Convert DTO to core model
        self.order_repo.save(order)  # Save core model to the repository

    def get_order(self, order_id: str) -> OrderDTO:
        order = self.order_repo.get(order_id)
        return OrderDTO.from_domain(order) if order else None

    def delete_order(self, order_id: str) -> None:
        self.order_repo.delete(order_id)