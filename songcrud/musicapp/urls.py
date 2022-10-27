from django.urls import path
from . import views

app_name = 'musicapp'

urlpatterns = [
        path("", views.index, name = 'musicapp'),
        path("", views.albumsstoreview, name = 'albums-store'),
        path("", views.blogview, name = 'blog'),
        path("", views.contactview, name = 'contact'),
        path("", views.elementsview, name = 'elements'),
        path("", views.eventview, name = 'event'),
        path("", views.login, name = 'login'),
]
