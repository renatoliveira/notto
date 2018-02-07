"""
Notto models
"""
from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    """
    A note made by a user (logged in or not)
    """
    content = models.TextField()
    url_title = models.CharField(
        max_length=500,
        unique=True,
        blank=False,
        null=False
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
            return '{} by {}.'.format(self.url_title, self.created_by.name)
        return '{} by anonymous.'.format(self.url_title)

    def get_children(self):
        """
        Get children notes
        """
        children = None
        if self.url_title is not None:
            children = Note.objects.filter(
                url_title__startswith=self.url_title+'/'
            )
        return children

    def has_parent(self):
        """
        Returns if this note has a parent note
        """
        if len(self.url_title.split('/')) > 1:
            return True
        return False

    def get_parent(self):
        """
        Get parent note
        """
        parent = [None]
        if self.url_title is not None and self.has_parent():
            parent = Note.objects.filter(
                url_title=''.join(self.url_title.split('/')[:-1])
            )
            if not parent:
                parent = [Note(
                    url_title=''.join(self.url_title.split('/')[:-1]),
                    content=''
                )]
        return parent[0]
