from auth.api import auth_router
from auth.plugin import AuthPlugin
from core.database import sqlalchemy_plugin
from litestar import Litestar

from app.plugins.error_tracking import init_error_tracking
from app.plugins.openapi import openapi_config


def create_app():
    init_error_tracking()
    app = Litestar(
        route_handlers=[auth_router],
        plugins=[sqlalchemy_plugin, AuthPlugin()],
        openapi_config=openapi_config,
        debug=True,
    )
    return app
