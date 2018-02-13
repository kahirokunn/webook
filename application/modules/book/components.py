from .models import Book
from submodules.helper import filter_dict
from .constants import BookTypes


def get_book_fields() -> list:
    """本のフィールドを全て取得する"""
    return Book.get_all_field_names()


def filter_book_params(params: dict) -> dict:
    """フィルターに通し、危険な値の可能性を排除する"""
    return filter_dict(keys=get_book_fields(), dictionary=params)


def generate_book(params: dict) -> Book:
    """新しい本を作成する"""
    params = filter_book_params(params)

    # book_urlは電子本限定。電子本が読めるURLを登録する必要がある。
    if params['type'] is not int(BookTypes.ebook):
        del params['book_url']

    book = Book(**params)
    book.save()
    return book
