from constants import ROOT_NAME
from settings import MEDIA_URL
from modules.wallet.service import get_user_balance
from submodules import logger


def constants(request):
    """Return context variables helpful for everything."""

    variable = {
        'ROOT_NAME': ROOT_NAME,
        'MEDIA_URL': MEDIA_URL,
        'BALANCE': get_user_balance(request.user),
    }

    return variable
