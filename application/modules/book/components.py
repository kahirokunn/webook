from .models import Book, Category
from submodules.helper import \
    filter_dict, is_iterable, be_list_or_return, has_str
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

    # カテゴリを保持する
    categories = []
    if 'categories' in params:
        categories = be_list_or_return(params['categories'])
        del params['categories']

    # book_urlは電子本限定。電子本が読めるURLを登録する必要がある。
    if params['type'] is not int(BookTypes.ebook):
        del params['book_url']

    book = Book(**params)
    book.save()

    # 本にカテゴリを追加
    for category in categories:
        book.categories.add(category)

    return book


def add_category_by_name_if_not_exists(category_name: str) -> Category:
    """カテゴリがなかったら追加する"""
    if not Category.is_exists_by_name(category_name):
        category = Category()
        category.name = category_name
        category.save()
        return category
    else:
        return Category.get(category_name)
