from modules.book.models import Book as _Book
from submodules.helper import filter_dict
from submodules import logger
from .constants import BookTypes


def get_books() -> list:
    """本を取得する"""
    return _Book.get_all()


def get_book(pk: int):
    """本を取得する"""
    return _Book.get(pk)


def new_book(params: dict, is_save=False):
    """新しい本を作成する"""
    params = filter_dict(keys=get_book_fields(), dictionary=params)
    logger.info(params)
    # book_urlは電子本限定。電子本が読めるURLを登録する必要がある。
    if params['type'] is not int(BookTypes.ebook):
        del params['book_url']
    book = _Book(**params)
    if is_save:
        book.save()
    return book


def get_book_fields() -> list:
    """本のフィールドを全て取得する"""
    return _Book.get_all_field_names()
