from django.db import models


class Place(models.Model):
    """
    It could've been called 'City'
    But it's nice to have flexible structure
    """

    name = models.CharField(max_length=128)

    # Reversed ForeignKey -> place.filters.all
    # Reversed ForeignKey -> place.events.all
