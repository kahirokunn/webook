from modules.orderbook import service as orderbook_sv


def get_user_balance(user) -> int:
    """残高を取得する"""
    return orderbook_sv.get_bought_sum_price(user)
