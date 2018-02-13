from submodules.decorators import valid_attr_or_failed
from typing import Iterable


@valid_attr_or_failed('urlpatterns', 'app_name')
def get_urls(module):
    valid_attr_or_failed(module, 'urlpatterns', 'app_name')
    urlpatterns = getattr(module, 'urlpatterns')
    app_name = getattr(module, 'app_name')
    return urlpatterns, app_name, app_name


def filter_dict(keys: Iterable, dictionary: dict) -> dict:
    """余分なキーが混ざらない、指定キーのみで構成されたdictを返す"""
    return {key: dictionary[key] for key in keys if key in dictionary}


def flatten_dict_only_one_element(iterable: Iterable, number: int = 1) -> dict:
    """
    dict型にある1つしかない要素を平坦にする

    example in: {a: [1], b:[1,2]}
    example out: {a: 1, b:[1,2]}
    """
    clone = dict(iterable)

    for key, value in clone.items():
        for i in range(number):
            if hasattr(value, '__iter__') and len(value) == 1:
                clone[key] = value[0]

    return clone
