from django.db import models

from nuvola.models.timestamped import TimeStampedModel


class Posts(TimeStampedModel):

    title = models.CharField(max_length=255)
    content = models.TextField(default='')
    author1 = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'posts'
