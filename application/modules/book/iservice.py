from abc import ABCMeta, abstractmethod
from .models import Book


class IService(metaclass=ABCMeta):
    """本サービス"""

    @classmethod
    @abstractmethod
    def get_book(cls) -> Book:
        """本を取得する"""
        pass
