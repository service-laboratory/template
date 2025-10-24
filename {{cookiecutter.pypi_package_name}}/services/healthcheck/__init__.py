from litestar import get


@get("/healthcheck")
async def healthcheck() -> dict:
    return {"status": "ok"}
