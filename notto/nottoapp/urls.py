from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:note_name>', views.note, name='note')
]
