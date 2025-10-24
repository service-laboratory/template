from litestar import Router, get
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
