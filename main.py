from dependency_injector.wiring import inject, Provide

from application.dtos import OrderDTO, ProductDTO, UserDTO
from application.services import OrderService, ProductService, UserService
from DI.container import Container


@inject
def main(
    user_service: UserService = Provide[Container.user_service],
    product_service: ProductService = Provide[Container.product_service],
    order_service: OrderService = Provide[Container.order_service]
):

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
    
    order_service.delete_order()


if __name__ == '__main__':
    db_url = 'sqlite:///example.db'  # Example SQLite database URL

    container = Container()
    container.config.db_url.from_value(db_url)
    container.init_resources()
    container.wire(modules=[__name__])
    main()
