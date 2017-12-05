from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    '''
    A note made by a user (logged in or not)
    '''
    content = models.TextField()
    url_title = models.CharField(
        max_length=500
    )
    last_modified_date = models.DateTimeField(
        auto_now=True
    )
    created_by = models.ForeignKey(
        User,
        on_delete='CASCADE',
        blank=True,
        null=True
    )

    def __str__(self):
        if self.created_by is not None:
            return 'A note by {}.'.format(self.created_by.name)
        return 'An annonymous note.'
