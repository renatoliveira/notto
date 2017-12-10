'''
Notto tests
'''
from django.test import TestCase
from django.db import transaction
from django.db.utils import IntegrityError
from nottoapp.models import Note

class NoteTestCase(TestCase):
    '''
    Test case for the Note
    '''
    def setUp(self):
        '''
        Set records up.
        '''
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

    def test_get_children(self):
        '''
        Tests if the note is able to list its children, if they exist.
        If they don't exist, then return an empty list.
        '''
        parent = Note.objects.get(url_title='parent')
        loose_note = Note.objects.get(url_title='lonely_note')
        children = parent.get_children()
        self.assertEqual(1, len(children))
        children = loose_note.get_children()
        self.assertEqual(0, len(children))

    def test_get_parent(self):
        '''
        Tests if the note is able to get its parent record, if it exists.
        If it doesn't exist, then return None.
        '''
        child = Note.objects.get(url_title='parent/child')
        parent = child.get_parent()
        loose_note = Note.objects.get(url_title='lonely_note')
        self.assertNotEqual(None, parent)
        self.assertEqual('parent', parent.url_title)
        parent = loose_note.get_parent()
        self.assertEqual(None, parent)

class NoteAccessTest(TestCase):
    '''
    Tests of access using URLs
    '''
    def test_post_note(self):
        '''
        Test the post of a single note
        '''
        form_data = {
            'content': 'a note content'
        }
        self.client.post('/foo', form_data)
        self.assertEqual(1, len(Note.objects.all()))

    def test_post_children(self):
        '''
        Test the post of a single note that is a child of a non-existing note.
        '''
        form_data = {
            'content': 'a children content'
        }
        self.client.post('/foo/bar', form_data)
        self.assertEqual(1, len(Note.objects.all()))

    def test_do_not_create_duplicates(self):
        '''
        Tests that the database is enforcing the unique constraint on "url_title".
        '''
        form_data = {
            'content': 'some text'
        }
        self.client.post('/foo', form_data)
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
