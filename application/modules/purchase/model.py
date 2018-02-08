from django.db import models


class PurchaseOrder(models.Model):
    # user 1 対 n
    user_id = models.ForeignKey(to=User, on_delete=False)
    # book 1 対 1
    book_id = models.ForeignKey(to=Book, on_delete=False)
    price = models.IntegerField()
    ordered_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ordered_at
