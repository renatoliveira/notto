'''
Notto models
'''
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
    parent_note = models.ForeignKey(
        'self',
        on_delete='CASCADE',
        blank=True,
        null=True
    )

    def __str__(self):
        if self.created_by is not None:
            return '{} by {}.'.format(self.url_title, self.created_by.name)
        return '{} by annonymous.'.format(self.url_title)

    def get_children(self):
        '''
        Get children notes
        '''
        if self.url_title is not None:
            return Note.objects.filter(
                parent_note=self.id
            )

    def get_parent(self):
        '''
        Get parent note
        '''
        if self.url_title is not None and self.parent_note is not None:
            return Note.objects.get(pk=self.parent_note.id)
