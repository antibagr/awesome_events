import datetime

# from django.contrib.auth.models import AbstractUser
from django_passwordless_user.models import AbstractBaseUser
from django.db import models
from django.conf import settings
from django.core.cache import cache


class User(AbstractBaseUser):

    class Meta:
        db_table = 'user'

    ip = models.GenericIPAddressField(unique=True, db_index=True)

    USERNAME_FIELD = 'ip'
    # Reversed ForeignKey -> user.filters.all

    def __str__(self) -> str:
        return self.ip

    def last_seen(self) -> datetime.datetime:
        return cache.get(f'last_seen_{self.id}') or None

    def online(self) -> bool:
        if self.last_seen():
            return datetime.datetime.now() < (self.last_seen() + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT))
        return False
