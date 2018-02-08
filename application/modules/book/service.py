from .iservice import IService
from .models import Book


class Service(IService):
    """本サービス"""

    @classmethod
    def get_book(cls) -> Book:
        """本を取得する"""
        return Book()
