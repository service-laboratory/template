import importlib
from app.core.settings import settings
from app.core.database import session_maker


class Services:
    def __init__(self, service_paths: list[str]):
        self.handlers = []
        self.plugins = []

        for path in service_paths:
            service = importlib.import_module(path)
            service.init_app(self, session_maker)


services = Services(settings.services)
