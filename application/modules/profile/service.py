from . import models
from . import components as profile_cmpt
from submodules.helper import elapsed_months


def new_profile(user, params) -> models.Profile:
    return profile_cmpt.new_profile(user, params)


def update_profile(user, params) -> models.Profile:
    return profile_cmpt.update_profile(user, params)


def month_enrollment_period(user) -> int:
    return elapsed_months(str(user.profile.join_at)) + 1
