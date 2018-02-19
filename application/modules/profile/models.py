from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    thumbnail_url = models.ImageField(upload_to='images',
                                      null=True, blank=True)
    join_at = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_by_id(cls, pk: int):
        return cls.objects.get(pk=pk)

    def __str__(self):
        return 'username: [{0}], join_at: [{1}]'.format(self.user.username,
                                                        self.join_at)
