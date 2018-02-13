from .models import OrderBook as _OrderBook
from ..book.service import new_book


def order_new_one(user, book_params: dict,
                  price: int, ordered_at: str) -> _OrderBook:
    """新しい本を注文する"""
    book = new_book(book_params, is_save=True)
    order_book = _OrderBook(user=user, book=book, price=price,
                            ordered_at=ordered_at)
    order_book.save()
    return order_book


def order_existing_one(
        user, book, price: int, ordered_at: str) -> _OrderBook:
    """登録されてる本を注文する"""
    order_book = _OrderBook(user=user, book=book, price=price,
                            ordered_at=ordered_at)
    order_book.save()
    return order_book


def cancel_order(pk: int) -> bool:
    """注文を取り消す"""
    return _OrderBook.cancel_order_by_id(pk=pk)


def get_order_book_by_user(user) -> list:
    """指定したユーザーの購入発注書の取得"""
    return _OrderBook.get_list_by_user(user=user)


def is_exists_record_by_user(user) -> bool:
    """指定したユーザーは購入記録があるかどうか"""
    return _OrderBook.has_book_by_user(user=user)


def get_order_book_by_book(book) -> list:
    """指定した本の購入注文書の取得"""
    return _OrderBook.get_list_by_book(book=book)
