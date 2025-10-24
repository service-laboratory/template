from auth.api import auth_router
from auth.plugin import AuthPlugin
from core.database import sqlalchemy_plugin
from core.openapi import openapi_config
from litestar import Litestar


def create_app():
    app = Litestar(
        route_handlers=[auth_router],
        plugins=[sqlalchemy_plugin, AuthPlugin()],
        openapi_config=openapi_config,
        debug=True,
    )
    return app
