from django.conf import settings
from django.db import models
from modules.book.models.book import Book
from submodules import logger


class OrderBook(models.Model):
    # user 1 対 n
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=False)
    # book 1 対 1
    book = models.ForeignKey(to=Book, on_delete=False)
    price = models.IntegerField()
    ordered_at = models.DateField()
    cancelled_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_all(cls) -> list:
        """全てを取得する"""
        return cls.objects.all()

    @classmethod
    def get_cancelled_all(cls) -> list:
        """キャンセルされた全てを取得する"""
        return cls.objects.filter(cancelled_at__isnull=False)

    @classmethod
    def get_list_by_user(cls, user) -> list:
        """特定ユーザーに紐づくエンティティを取得する"""
        return cls.objects.filter(user=user, cancelled_at__isnull=True)

    @classmethod
    def get_list_by_book(cls, book) -> list:
        """特定の本に紐づくエンティティを取得する"""
        return cls.objects.filter(book=book, cancelled_at__isnull=True)

    @classmethod
    def has_book_by_user(cls, user) -> bool:
        """特定のユーザーが本をもっているか確認する"""
        return cls.objects.filter(user=user,
                                  cancelled_at__isnull=True).exists()

    @classmethod
    def get_count(cls) -> int:
        """全ての本の数を取得する"""
        return cls.objects.filter(cancelled_at__isnull=True).count()

    @classmethod
    def get_count_by_user(cls, user) -> int:
        """特定のユーザーが持っている本の数を取得する"""
        return cls.objects.filter(user=user, cancelled_at__isnull=True).count()

    @classmethod
    def get_count_by_book(cls, book) -> int:
        """特定の本の注文数を取得する"""
        return cls.objects.filter(book=book, cancelled_at__isnull=True).count()

    @classmethod
    def get_by_id(cls, pk: int):
        try:
            return cls.objects.get(pk=pk)
        except cls.DoesNotExist:
            return None

    @classmethod
    def cancel_order_by_id(cls, pk: int) -> bool:
        obj = cls.get_by_id(pk=pk)
        if obj is not None:
            obj.cancelled_at(datetime.now)
            obj.save()
            return True
        else:
            return False

    def __str__(self):
        if self.cancelled_at is None:
            return str(self.ordered_at)
        else:
            return str(self.cancelled_at)
