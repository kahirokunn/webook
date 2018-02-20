from . import models


def new_profile(user, params) -> models.Profile:
    profile = models.Profile(**params)
    profile.user = user
    profile.save()
    return profile


def update_profile(user, params: dict) -> models.Profile:
    profile = models.Profile(user=user, **params)
    profile.save()
    return profile
