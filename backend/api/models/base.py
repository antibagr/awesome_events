from datetime import datetime

from django.db import models


class TimeBasedModel(models.Model):
    """Base class to store create and update timestamp"""

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def pretty_date(self, date: datetime) -> str:
        """
        Format date of an event to a readable string
        """
        return date.strftime("%Y.%m.%d %H:%M")
