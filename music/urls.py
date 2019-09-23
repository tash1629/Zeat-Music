from django.urls import path
from django.urls import re_path
from . import views
from django.views.generic.detail import DetailView

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'), # index is a variable for /music/


    # /music/<pk>/    (music followed by an ID)
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'), #creating album_id var

    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),


]
