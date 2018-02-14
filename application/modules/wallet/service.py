from modules.order_book.service import \
    get_bought_sum_price as _get_bought_sum_price


def get_user_balance(user) -> int:
    """残高を取得する"""
    return _get_bought_sum_price(user)
