from . import iservice
from .components import get_book_paginated
from .model import Book


class Service(iservice):

    @classmethod
    def get_books(cls, page):
        return get_book_paginated(page)

    @classmethod
    def get_all_book(cls):
        return Book.get_all()
