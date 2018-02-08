from abc import ABCMeta, abstractmethod
from django.core.paginator import Paginator


class IService(metaclass=ABCMeta):
    """本の注文サービス"""

    @classmethod
    @abstractmethod
    def history(cls, page=None) -> Paginator | list:
        """注文履歴"""
        pass

    @classmethod
    @abstractmethod
    def account_history(cls, account_id, page=None) -> Paginator | list:
        """アカウントの注文履歴"""
        pass

    @classmethod
    @abstractmethod
    def purchase(cls, account_id, book_id, price) -> bool:
        """本を購入する"""
        pass

    @classmethod
    @abstractmethod
    def cancel_book(cls, account_id, book_id) -> bool:
        """購入した本を返品する"""
        pass
