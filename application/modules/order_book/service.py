from .iservice import IService
from .models import OrderBook


class Service(IService):
    """購入発注書サービス"""

    @classmethod
    def create_order(cls, user, book, price, ordered_at) -> OrderBook:
        """注文する"""
        order_book = OrderBook(user=user, book=book, price=price,
                               ordered_at=ordered_at)
        order_book.save()
        return order_book

    @classmethod
    def cancel_order(cls, pk: int) -> bool:
        """注文の取り消し"""
        return OrderBook.cancel_order_by_id(pk=pk)

    @classmethod
    def get_order_book(cls) -> OrderBook:
        """購入発注書の取得"""
        return OrderBook()

    @classmethod
    def get_order_book_by_user(cls, user) -> list:
        """指定したユーザーの購入発注書の取得"""
        return OrderBook.get_list_by_user(user=user)

    @classmethod
    def is_exists_record_by_user(cls, user) -> bool:
        """指定したユーザーは購入記録があるかどうか"""
        return OrderBook.has_book_by_user(user=user)

    @classmethod
    def get_order_book_by_book(cls, book: OrderBook | int) -> list:
        """指定した本の購入注文書の取得"""
        return OrderBook.get_list_by_book(book=book)
