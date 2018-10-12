from django.db import models

from nuvola.models.timestamped import TimeStampedModel


class Category(TimeStampedModel):

    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'
