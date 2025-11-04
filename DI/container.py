from dependency_injector import containers, providers

from application.services.order_service import OrderService
from application.services.product_service import ProductService
from application.services.user_service import UserService
from infrastructure.adapters.repositories.order_repository_impl import SQLAlchemyOrderAdapter
from infrastructure.adapters.repositories.product_repository_impl import SQLAlchemyProductAdapter
from infrastructure.adapters.repositories.user_repository_impl import SQLAlchemyUserAdapter
from infrastructure.persistence.sql.session import get_db_session


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    session = providers.Resource(get_db_session)

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
        db=session
    )
    
    order_service = providers.Singleton(
        OrderService,
        order_repo=order_repo,
        user_repo=user_repo,
        product_repo=product_repo
    )