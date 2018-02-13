from modules.book.models import Book as _Book
from .constants import BookTypes
from .components import get_book_fields, generate_book


def get_books() -> list:
    """本を取得する"""
    return _Book.get_all()


def get_book(pk: int):
    """本を取得する"""
    return _Book.get(pk)


def new_book(params: dict) -> _Book:
    """新しい本を作成する"""
    return generate_book(params)
