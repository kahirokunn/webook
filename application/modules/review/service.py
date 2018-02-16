from . import models
from . import components as review_cmpt


def post_review(user, book, review_text: str, star: int) -> bool:
    if is_reviewed(user, book):
        return False

    return review_cmpt.new_review(user, book, review_text, star)


def is_reviewed(user, book) -> bool:
    """レビュー済み？"""
    return models.Review.is_exists(user, book)


def get_reviews(book) -> list:
    return models.Review.get_by_book(book)


def get_reviews_separate_user(user, book) -> dict:
    """指定ユーザーのは分けてレビューの一覧を取得"""
    return review_cmpt.get_reviews_separate_user(user, book)


def get_review(user, book):
    if is_reviewed(user, book):
        return models.Review.get_by_user_with_book(user, book)
    else:
        return None
