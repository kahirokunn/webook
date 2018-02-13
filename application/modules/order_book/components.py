from .models import OrderBook
from ..book.service import new_book


def order_the_book(
        user, book, price: int, ordered_at: str) -> OrderBook:
    """本を注文する"""
    order_book = OrderBook()
    order_book.user = user
    order_book.book = book
    order_book.price = price
    order_book.ordered_at = ordered_at
    order_book.save()
    return order_book
