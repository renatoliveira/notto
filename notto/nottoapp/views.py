'''
Notto views
'''
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Note
from django.core import serializers
import json

def index(request):
    '''
    Index
    '''
    return render(
        request,
        'index.html'
    )

@csrf_protect
def note(request, note_name):
    '''
    A record
    '''
    record = None
    if note_name == '':
        note_name = request.path[1:]
    try:
        notes = Note.objects.filter(
            url_title=note_name
        )
        if not notes:
            if request.method == 'GET':
                raise Note.DoesNotExist
            elif request.method == 'POST':
                if 'content' not in request.POST:
                    return render(
                        request,
                        'note.html',
                        {
                            'content': '',
                            'note_url': note_name,
                            'parent': record.get_parent(),
                            'children': []
                        }
                    )
                record = Note(
                    content=request.POST['content'],
                    url_title=note_name
                )
                record.save()
        else:
            if request.method == 'GET':
                record = notes[0]
            elif request.method == 'POST':
                record = notes[0]
                record.content = request.POST['content']
                record.save()
    except Note.DoesNotExist:
        record = Note(
            content='',
            url_title=note_name
        )
    children = serializers.serialize('python', record.get_children().all(), fields=('url_title'))
    children = json.dumps([c['fields'] for c in children])

    return render(
        request,
        'note.html',
        {
            'content': record.content,
            'note_url': record.url_title,
            'parent': record.get_parent(),
            'children': children
        }
    )
