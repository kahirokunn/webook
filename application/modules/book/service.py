from modules.book.models import Book


class Service:
    """本サービス"""

    @classmethod
    def get_book(cls) -> Book:
        """本を取得する"""
        return Book()
