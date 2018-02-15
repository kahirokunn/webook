from .models import Book as _Book
from .constants import BookTypes
from . import components as book_cmpt


def get_books() -> list:
    """本を取得する"""
    return _Book.get_all()


def get_book(pk: int):
    """本を取得する"""
    return _Book.get(pk)


def new_book(params: dict) -> _Book:
    """新しい本を作成する"""
    return book_cmpt.generate_book(params)


def add_category_to_book(book, category_id: int) -> bool:
    """本にカテゴリを追加する"""
    _Book(book).category_set.add(category_id)
    return True


def new_category(category_name: str) -> bool:
    """
    新しいカテゴリを作成する
    重複する場合は作成しない

    :return created=True is_exists=False
    """
    return book_cmpt.add_category_by_name_if_not_exists(category_name)
