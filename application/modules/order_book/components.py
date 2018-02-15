from .models import OrderBook


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


def get_order_book_by_user(user) -> list:
    """指定したユーザーの購入発注書の取得"""
    return OrderBook.get_list_by_user(user=user)


def get_order_book_by_book(book) -> list:
    """指定した本の購入注文書の取得"""
    return OrderBook.get_list_by_book(book=book)
