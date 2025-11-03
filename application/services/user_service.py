from application.dtos import UserDTO
from core.ports.repositories.user_repository_port import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user_dto: UserDTO) -> None:
        user = user_dto.to_domain()  # Convert DTO to core model
        self.user_repo.save(user)  # Save core model to the repository

    def get_user(self, user_id: str) -> UserDTO:
        user = self.user_repo.get(user_id)
        return UserDTO.from_domain(user) if user else None

    def delete_user(self, user_id: str) -> None:
        self.user_repo.delete(user_id)
