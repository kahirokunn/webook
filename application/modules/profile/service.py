from . import models
from . import components as profile_cmpt
from submodules.helper import elapsed_months


def new_profile(user, thumbnail_url, join_at) -> models.Profile:
    return profile_cmpt.new_profile(user, thumbnail_url, join_at)


def month_enrollment_period(user) -> int:
    return elapsed_months(str(user.profile.join_at)) + 1
