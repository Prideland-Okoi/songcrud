from django.urls import path
from . import views

app_name = 'musicapp'

urlpatterns = [
        path("", views.index, name = 'musicapp'),
        path('musicapp/albums-store/', views.albumsstore, name = 'albums-store'),
        path('musicapp/blog/', views.blog, name = 'blog'),
        path('musicapp/contact/', views.contact, name = 'contact'),
        path('musicapp/elements/', views.elements, name = 'elements'),
        path('musicapp/event/', views.event, name = 'event'),
        path('musicapp/login/', views.login, name = 'login'),
]
