from modules.orderbook import service as orderbook_sv
from modules.profile import service as profile_sv


def get_user_balance(user) -> int:
    """残高を取得する"""
    full_balance = profile_sv.month_enrollment_period(user) * 5000
    return full_balance - orderbook_sv.get_bought_sum_price(user)
