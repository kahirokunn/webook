from modules.order_book import service as order_book_sv


def get_user_balance(user) -> int:
    """残高を取得する"""
    return order_book_sv.get_bought_sum_price(user)
