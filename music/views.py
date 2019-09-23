from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
#generic views

class IndexView(generic.ListView):
    #specify what template we are using
    template_name = 'music/index.html' # plugging list of albums into this album
    context_object_name = 'all_albums'  #default name is object_list

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album # looking at the details of an album
    template_name = 'music/detail.html' # plugging album into this template

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']