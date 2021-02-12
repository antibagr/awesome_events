from datetime import datetime

from django.db import models

from .base import TimeBasedModel
from .place import Place
from .topic import Topic



class Event(TimeBasedModel):

    class Meta:
        ordering = ('-created_at',)

    title = models.CharField(max_length=128)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='events')
    topics = models.ManyToManyField(Topic, related_name='events')

    # Reversed ManyToManyField -> event.filters.all


    def __str__(self) -> str:
        return f"{self.title}. {self.place} {self.pretty_date(self.start_at)} - {self.pretty_date(self.end_at)} {self.topics}"
