from abc import ABCMeta, abstractmethod
from .models import OrderBook


class IService(metaclass=ABCMeta):
    """購入発注書サービス"""

    @classmethod
    @abstractmethod
    def get_order_book(cls) -> OrderBook:
        """購入発注書の取得"""
        pass

    @classmethod
    @abstractmethod
    def get_order_book_by_user(cls, user) -> list:
        """指定したユーザーの購入発注書の取得"""
        pass

    @classmethod
    @abstractmethod
    def is_exists_record_by_user(cls, user) -> bool:
        """指定したユーザーは購入記録があるかどうか"""
        pass

    @classmethod
    @abstractmethod
    def get_order_book_by_book(cls, book: OrderBook | int) -> list:
        """指定した本の購入注文書の取得"""
        pass

    @classmethod
    def cancel_order(cls, pk: int) -> bool:
        """注文の取り消し"""
        pass
