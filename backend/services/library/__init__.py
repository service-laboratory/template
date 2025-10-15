from litestar import Litestar
from litestar import Router


from litestar import get
from litestar.controller import Controller
from msgspec import Struct


class Book(Struct):
    name: str


class BookController(Controller):
    @get("/books")
    async def get_books(self) -> list[Book]:
        books = [
            Book(name="poems"),
            Book(name="stories"),
        ]
        return books


book_router = Router(
    path="/api/library",
    route_handlers=[BookController],
)


def init_app(services):
    services.handlers.append(book_router)
