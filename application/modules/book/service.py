from modules.book.models import Book as _Book


def get_books() -> list:
    """本を取得する"""
    return _Book.get_all()


def get_book(pk: int):
    """本を取得する"""
    return _Book.get(pk)
