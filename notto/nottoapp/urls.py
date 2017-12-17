'''
Notto URLs
'''
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:note_name>.pdf', views.html2pdf),
    path('<str:note_name>', views.note, name='note'),
    re_path(r'^(?P<note_name>)', views.note, name='note')
]
