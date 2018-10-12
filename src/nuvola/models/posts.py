from django.db import models

from nuvola.models.timestamped import TimeStampedModel


class Posts(TimeStampedModel):

    title = models.CharField(max_length=255)
    content = models.TextField(default='')

    class Meta:
        db_table = 'posts'
