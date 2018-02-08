from abc import ABCMeta, abstractmethod
from django.core.paginator import Paginator


class IService(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def get_books(cls, page) -> Paginator:
        pass

    @classmethod
    @abstractmethod
    def get_all_book(cls) -> list:
        pass
