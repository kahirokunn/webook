from . import models as book_model
from .constants import BookTypes
from . import components as book_cmpt


def get_books() -> list:
    """本を取得する"""
    return book_model.Book.get_all()


def get_book(pk: int):
    """本を取得する"""
    return book_model.Book.get(pk)


def new_book(params: dict) -> book_model.Book:
    """新しい本を作成する"""
    return book_cmpt.generate_book(params)


def add_category_to_book(book, category_id: int) -> bool:
    """本にカテゴリを追加する"""
    book_model.Book(book).category_set.add(category_id)
    return True


def new_category(category_name: str) -> bool:
    """
    新しいカテゴリを作成する
    重複する場合は作成しない

    :return created=True is_exists=False
    """
    return book_cmpt.add_category_by_name_if_not_exists(category_name)


def post_review(
        user, book: book_model.Book, review_text: str, star: int) -> bool:
    if is_reviewed(user, book):
        return False

    return book_cmpt.new_review(user, book, review_text, star)


def is_reviewed(user, book) -> bool:
    """レビュー済み？"""
    return book_model.Review.is_exists(user, book)


def get_reviews(book) -> list:
    return book_model.Review.get_by_book(book)


def get_reviews_separate_user(user, book) -> dict:
    """指定ユーザーのは分けてレビューの一覧を取得"""
    return book_cmpt.get_reviews_separate_user(user, book)


def get_review(user, book):
    if is_reviewed(user, book):
        return book_model.Review.get_by_user_with_book(user, book)
    else:
        return None
