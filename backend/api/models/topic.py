from django.db import models


class Topic(models.Model):
    """
    Topic model class. Not so smart.
    """

    name = models.CharField(max_length=256)

    # Reversed ManyToManyField -> topic.filters.all
    # Reversed ManyToManyField -> topic.events.all
