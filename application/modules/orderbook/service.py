from .models import OrderBook as _OrderBook
from ..book import service as book_sv
from . import components as orderbook_cmpt


def order_new_one(user, book_params: dict,
                  price: int, ordered_at: str) -> _OrderBook:
    """新しい本を注文する"""
    book = book_sv.new_book(book_params)
    return orderbook_cmpt.order_the_book(user, book, price, ordered_at)


def order_existing_one(
        user, book, price: int, ordered_at: str) -> _OrderBook:
    """登録されてる本を注文する"""
    return orderbook_cmpt.order_the_book(user, book, price, ordered_at)


def cancel_order(pk: int) -> bool:
    """注文を取り消す"""
    return _OrderBook.cancel_order_by_id(pk=pk)


def get_bought_sum_price(user) -> int:
    """ユーザーが購入した総額を取得する(jpy)"""
    orderbook = orderbook_cmpt.get_orderbook_by_user(user)

    sum_price = 0
    for record in orderbook:
        sum_price += record.price
    return sum_price


def is_exists_record_by_user(user) -> bool:
    """指定したユーザーは購入記録があるかどうか"""
    return _OrderBook.has_book_by_user(user=user)
