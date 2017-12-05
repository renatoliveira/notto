from django.shortcuts import render, redirect
from django.http import Http404
from django.views.decorators.csrf import csrf_protect
from .models import Note
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
    A note
    '''
    note = None
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
                            'note_url': note_name
                        }
                    )
                note = Note(
                    content=request.POST['content'],
                    url_title=note_name
                )
                note.save()
        else:
            if request.method == 'GET':
                note = notes[0]
            elif request.method == 'POST':
                note = notes[0]
                note.content = request.POST['content']
                print(note.content)
                note.save()
    except Note.DoesNotExist:
        note = Note(
            content='',
            url_title=note_name
        )
    return render(
        request,
        'note.html',
        {
            'content': note.content,
            'note_url': note.url_title
        }
    )
