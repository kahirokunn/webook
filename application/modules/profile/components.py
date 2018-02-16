from . import models


def new_profile(user, thumbnail_url, join_at) -> models.Profile:
    profile = models.Profile()
    profile.user = user
    profile.thumbnail_url = thumbnail_url
    profile.join_at = join_at
    profile.save()
    return profile
