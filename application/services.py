from application.dtos import OrderDTO, ProductDTO, UserDTO
from domain.ports import OrderRepository, ProductRepository, UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user_dto: UserDTO) -> None:
        user = user_dto.to_domain()  # Convert DTO to domain model
        self.user_repo.save(user)  # Save domain model to the repository

    def get_user(self, user_id: str) -> UserDTO:
        user = self.user_repo.get(user_id)
        return UserDTO.from_domain(user) if user else None

    def delete_user(self, user_id: str) -> None:
        self.user_repo.delete(user_id)


class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def create_product(self, product_dto: ProductDTO) -> None:
        product = product_dto.to_domain()  # Convert DTO to domain model
        self.product_repo.save(product)  # Save domain model to the repository

    def get_product(self, product_id: str) -> ProductDTO:
        product = self.product_repo.get(product_id)
        return ProductDTO.from_domain(product) if product else None

    def delete_product(self, product_id: str) -> None:
        self.product_repo.delete(product_id)


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
        
        order = order_dto.to_domain(user=user, product=product)  # Convert DTO to domain model
        self.order_repo.save(order)  # Save domain model to the repository

    def get_order(self, order_id: str) -> OrderDTO:
        order = self.order_repo.get(order_id)
        return OrderDTO.from_domain(order) if order else None

    def delete_order(self, order_id: str) -> None:
        self.order_repo.delete(order_id)