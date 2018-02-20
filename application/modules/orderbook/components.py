from .models import OrderBook


def order_the_book(user, book, price: int, ordered_at: str,
                   receipt_url: str) -> OrderBook:
    """本を注文する"""
    orderbook = OrderBook()
    orderbook.user = user
    orderbook.book = book
    orderbook.price = price
    orderbook.ordered_at = ordered_at
    orderbook.receipt_url = receipt_url
    orderbook.save()
    return orderbook


def get_orderbook_by_user(user) -> list:
    """指定したユーザーの購入発注書の取得"""
    return OrderBook.get_list_by_user(user=user)


def get_orderbook_by_book(book) -> list:
    """指定した本の購入注文書の取得"""
    return OrderBook.get_list_by_book(book=book)
