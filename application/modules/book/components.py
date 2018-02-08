from django.core.paginator import Paginator


def get_book_paginated(page: int) -> Paginator:
    return Paginator(cls.objects.all().order_by('created_at'), page)
