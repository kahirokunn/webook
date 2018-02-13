from constants import ROOT_NAME
from settings import MEDIA_URL


def constants(request):
    """Return context variables helpful for everything."""

    variable = {
        'ROOT_NAME': ROOT_NAME,
        'MEDIA_URL': MEDIA_URL,
    }

    return variable
