from . import models


def new_profile(user, join_at) -> models.Profile:
    profile = models.Profile()
    profile.user = user
    profile.join_at = join_at
    profile.save()
    return profile


def update_profile(user, params: dict) -> models.Profile:
    profile = models.Profile(user=user, **params)
    profile.save()
    return profile
