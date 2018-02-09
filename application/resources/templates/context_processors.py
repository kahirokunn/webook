from constants import ROOT_NAME


def constants(request):
    """Return context variables helpful for everything."""

    variable = {
        'ROOT_NAME': ROOT_NAME
    }

    return variable
