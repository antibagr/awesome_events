from datetime import datetime

from django.db import models

from .base import TimeBasedModel
from .place import Place
from .topic import Topic
from .event import Event
from .user import User



class EventFilter(TimeBasedModel):

    class Meta:
        ordering = ('-created_at',)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='filters')
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='filters')
    topics = models.ManyToManyField(Topic, related_name='filters')
    new_events = models.ManyToManyField(Event, related_name='filters')

    def __str__(self) -> str:
        return f"{self.title}. {self.place} {self.pretty_date(self.start_at)} - {self.pretty_date(self.end_at)} {self.topics}"
