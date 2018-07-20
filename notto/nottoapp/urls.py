'''
Notto URLs
'''
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('n/<str:note_name>.pdf', views.html2pdf),
    path('n/<str:note_name>', views.note, name='note'),
    re_path(r'n/^(?P<note_name>)', views.note, name='note'),

    path('logout', views.logout_user, name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
]
