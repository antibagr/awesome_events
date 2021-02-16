from django.db import models


class Place(models.Model):
    """
    It could've been called 'City'
    But it's nice to have flexible structure
    """

    name = models.CharField(max_length=128, unique=True)

    # Reversed ForeignKey -> place.filters.all
    # Reversed ForeignKey -> place.events.all

    def __str__(self) -> str:
        return self.name
