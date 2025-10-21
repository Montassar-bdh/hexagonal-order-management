from application.services import UserService, ProductService, OrderService
from infrastructure.adapters import SQLAlchemyUserAdapter, SQLAlchemyProductAdapter, SQLAlchemyOrderAdapter
from infrastructure.models import SQLAlchemyUser, SQLAlchemyOrder, SQLAlchemyProduct
from application.dtos import UserDTO, ProductDTO, OrderDTO

def main():
    db_url = 'sqlite:///example.db'  # Example SQLite database URL

    # Initialize repositories
    user_repo = SQLAlchemyUserAdapter(db_url)
    product_repo = SQLAlchemyProductAdapter(db_url)
    order_repo = SQLAlchemyOrderAdapter(db_url)

    # Initialize services
    user_service = UserService(user_repo)
    product_service = ProductService(product_repo)
    order_service = OrderService(order_repo, user_repo, product_repo)

    # Create and save a user
    user_dto = UserDTO(id='1', name='Alice', email='alice@example.com')
    user_service.create_user(user_dto)

    # Create and save a product
    product_dto = ProductDTO(id='101', name='Laptop', price=999.99)
    product_service.create_product(product_dto)

    # Create and save an order
    order_dto = OrderDTO(id='5001', user_id='1', product_id='101', quantity=2)
    order_service.create_order(order_dto)

    # Retrieve and print the order
    retrieved_order = order_service.get_order('5001')
    print(f"Retrieved Order: {retrieved_order}")


if __name__ == '__main__':
    main()
