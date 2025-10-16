from litestar import get


@get("/healthcheck")
async def healthcheck() -> dict:
    return {"status": "ok"}


def init_app(services, *args, **kwargs):
    services.handlers.append(healthcheck)
