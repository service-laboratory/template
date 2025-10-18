from litestar import Litestar
from app.core.database import sqlalchemy_plugin
from app.core.openapi import openapi_config
from app.core.tracing import init_tracing
from app.core.services import services


def create_app():
    init_tracing()
    app = Litestar(
        route_handlers=services.handlers,
        plugins=[sqlalchemy_plugin, *services.plugins],
        openapi_config=openapi_config,
        debug=True,
    )
    return app
