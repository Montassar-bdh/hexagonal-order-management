from dependency_injector import containers, providers

from application.services import OrderService, ProductService, UserService
from infrastructure.adapters import (SQLAlchemyOrderAdapter,
                                     SQLAlchemyProductAdapter,
                                     SQLAlchemyUserAdapter)

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    
    user_repo = providers.Singleton(
        SQLAlchemyUserAdapter,
        db_url=config.db_url
    )

    user_service = providers.Singleton(
        UserService,
        user_repo=user_repo
    )
    
    product_repo = providers.Singleton(
        SQLAlchemyProductAdapter,
        db_url=config.db_url
    )
    
    product_service = providers.Singleton(
        ProductService,
        product_repo=product_repo
    )
    
    order_repo = providers.Singleton(
        SQLAlchemyOrderAdapter,
        db_url=config.db_url
    )
    
    order_service = providers.Singleton(
        OrderService,
        order_repo=order_repo,
        user_repo=user_repo,
        product_repo=product_repo
    )