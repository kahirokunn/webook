from . import models
from . import components as memo_cmpt


def post_memo(user, book, memo_text: str) -> bool:
    return memo_cmpt.new_memo(user, book, memo_text)


def get_memos(book) -> list:
    return models.Memo.get_by_book(book)


def get_memos_separate_user(user, book) -> dict:
    """指定ユーザーのは分けてレビューの一覧を取得"""
    return memo_cmpt.get_memos_separate_user(user, book)


def get_user_memo(user, book) -> list:
    return models.Memo.get_by_user_with_book(user, book)
