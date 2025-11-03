from application.dtos import ProductDTO
from core.ports.repositories.product_repository_port import ProductRepository


class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    def create_product(self, product_dto: ProductDTO) -> None:
        product = product_dto.to_domain()  # Convert DTO to core model
        self.product_repo.save(product)  # Save core model to the repository

    def get_product(self, product_id: str) -> ProductDTO:
        product = self.product_repo.get(product_id)
        return ProductDTO.from_domain(product) if product else None

    def delete_product(self, product_id: str) -> None:
        self.product_repo.delete(product_id)
