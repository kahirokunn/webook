from constants import ROOT_NAME
from settings import MEDIA_URL
from modules.wallet import service as wallet_sv
from django.contrib.auth.decorators import login_required


def constants(request):
    """Return context variables helpful for everything."""

    variable = {
        'ROOT_NAME': ROOT_NAME,
        'MEDIA_URL': MEDIA_URL,
        'BALANCE': 0,
    }

    if request.user.is_authenticated:
        variable['BALANCE'] = wallet_sv.get_user_balance(request.user)

    return variable
