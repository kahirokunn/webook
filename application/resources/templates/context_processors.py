from constants import ROOT_NAME
from settings import MEDIA_URL
from modules.wallet import service as wallet_sv


def constants(request):
    """Return context variables helpful for everything."""

    variable = {
        'ROOT_NAME': ROOT_NAME,
        'MEDIA_URL': MEDIA_URL,
        'BALANCE': wallet_sv.get_user_balance(request.user),
    }

    return variable
