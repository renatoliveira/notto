'''
Notto tests
'''
from django.test import TestCase
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
            url_title='child',
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
        child = Note.objects.get(url_title='child')
        parent = child.get_parent()
        loose_note = Note.objects.get(url_title='lonely_note')
        self.assertNotEqual(None, parent)
        self.assertEqual('parent', parent.url_title)
        parent = loose_note.get_parent()
        self.assertEqual(None, parent)
