from submodules.decorators import valid_attr_or_failed, valid_request_methods
from typing import Iterable
from importlib import import_module
from submodules import logger


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


def format_enum_to_choices(enum):
    return [(unit.value, unit.name) for unit in enum]


def is_iterable(obj):
    return hasattr(obj, '__iter__')


def has_str(obj):
    return hasattr(obj, '__str__')


def be_list_or_return(obj):
    if is_iterable(obj):
        return obj
    return [obj]


class ViewRouter:
    """不思議なルーター、お一つどうぞ"""

    def __init__(self, view_package_path: str = None, app_name: str = None):
        if app_name is not None:
            self.package_path = 'application.{0}.views'.format(app_name)
        else:
            self.package_path = view_package_path

    def __getattr__(self, module_name: str):
        path = '{0}.{1}'.format(self.package_path, module_name)
        module = import_module(path)
        logger.info(path)
        return self._call(module)

    @classmethod
    def _call(cls, module):
        """requestメソッドに対応するメソッドを実行"""

        def callback(request, *args, **kwargs):
            call_func_name = request.method.lower()
            return getattr(module, call_func_name)(request, *args, **kwargs)

        return callback
