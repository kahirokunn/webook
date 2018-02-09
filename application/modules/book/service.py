from modules.book.models import Book


def get_books() -> list:
    """本を取得する"""
    return Book.get_all()
