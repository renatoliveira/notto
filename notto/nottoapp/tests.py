"""
Notto tests
"""
from django.test import TestCase
from django.db import transaction
from django.db.utils import IntegrityError

from .models import Note


class NoteTestCase(TestCase):
    """
    Test case for the Note
    """
    def setUp(self):
        """
        Set records up.
        """
        parent = Note(
            url_title='parent',
            content='testing!'
        )
        parent.save()
        Note.objects.create(
            url_title='parent/child',
            content='testing!',
            parent_note=parent
        )
        Note.objects.create(
            url_title='lonely_note',
            content='I\'m sad'
        )


class NoteAccessTest(TestCase):
    """
    Tests of access using URLs
    """
    def test_post_note(self):
        """
        Test the post of a single note
        """
        form_data = {
            'content': 'a note content'
        }
        self.client.post('/n/foo', form_data)
        self.assertEqual(1, len(Note.objects.all()))

    def test_post_children(self):
        """
        Test the post of a single note that is a child of a non-existing note.
        """
        form_data = {
            'content': 'a children content'
        }
        self.client.post('/n/foo/bar', form_data)
        self.assertEqual(1, len(Note.objects.all()))

    def test_do_not_create_duplicates(self):
        """
        Tests that the database is enforcing the unique constraint on
        "url_title".
        """
        form_data = {
            'content': 'some text'
        }
        self.client.post('/n/foo', form_data)
        self.assertEqual(1, len(Note.objects.all()))
        duplicate = Note(
            content='more text',
            url_title='foo'
        )
        try:
            with transaction.atomic():
                duplicate.save()
            self.fail('Shouldn\'t have allowed creation of this note.')
        except IntegrityError:
            pass
        self.assertEqual(1, len(Note.objects.all()))

    def test_ignore_slash_at_end_of_url(self):
        """
        Should ignore the slash at the end, because '/n/foo' is the same note as
        '/n/foo/'
        """
        form_data = {
            'content': 'some text'
        }
        self.client.post('/n/foo', form_data)
        self.assertEqual(1, len(Note.objects.all()))
        self.client.post('/n/foo/', form_data)
        self.assertEqual(1, len(Note.objects.all()))
